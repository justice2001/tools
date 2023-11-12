import json
import os
import shutil
from dotenv import load_dotenv
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

def monitor_process(monitor):
    print("\rUPLOADING .... ({} %)".format(round(monitor.bytes_read/monitor.len*100,2)), end="")


# 获取基本变量
load_dotenv()
ALIST_URL = os.getenv("ALIST_URL")
ALIST_USERNAME = os.getenv("ALIST_USERNAME")
ALIST_PASSWORD = os.getenv("ALIST_PASSWORD")
UPLOAD_DIR = os.getenv("UPLOAD_DIR")
UPLOAD_FILE = os.getenv("UPLOAD_FILE")
COMPRESS_FORMAT = os.getenv("COMPRESS_FORMAT")
SAVES_DIR = os.getenv("SAVES_DIR")

COMPRESS_MAP = {
    "zip": ".zip",
    "gztar": ".tar.gz"
}


# check save dir exist
if (not os.path.exists(SAVES_DIR)):
    print("CAN NOT FOUND WORLD FOLDER: {}".format(SAVES_DIR))
    exit(0)

# compress file use provided format
if (not (COMPRESS_FORMAT in ['zip', 'gztar'])):
    print("INVALID COMPASS FORMAT ({})".format(COMPRESS_FORMAT))
    exit(0)

# If file exist, remove it
filename = UPLOAD_FILE + COMPRESS_MAP[COMPRESS_FORMAT]
if os.path.exists(filename):
    print("REMOVING EXIST COMPRESS PACK.....")
    os.remove(filename)


print("COMPASSING WORLD FOLDER.....")
shutil.make_archive(UPLOAD_FILE, COMPRESS_FORMAT, SAVES_DIR)

# 使用账户登陆到alist
auth_request = requests.post(ALIST_URL+'/api/auth/login', json={
    "username": ALIST_USERNAME,
    "password": ALIST_PASSWORD
})
auth_json = json.loads(auth_request.text)
token = auth_json['data']['token']

if not token:
    print("GET ALIST TOKEN FAILED!")
    exit()

# 列出目录文件，并搜寻是否存在存档文件
folder_request = requests.post(ALIST_URL+"/api/fs/list", json={
    "path": UPLOAD_DIR
}, headers={
    "Authorization": token 
})

folder_list = json.loads(folder_request.text)["data"]["content"]
for item in folder_list:
    if item["name"]==filename:
        print("FILE EXIST, REMOVING....")
        requests.post(ALIST_URL+"/api/fs/remove", json={
            "names": [UPLOAD_DIR+filename]
        }, headers={
            "Authorization": token 
        })
        break

# 上传文件
file = MultipartEncoderMonitor.from_fields(fields={
    "file": (filename, open(filename, "rb"))
}, callback=monitor_process)
upload_req = requests.put(ALIST_URL+"/api/fs/form", data=file, headers={
    "Authorization": token,
    "File-Path": UPLOAD_DIR+filename,
    "Content-Type": file.content_type
})
print()
print(upload_req.text)