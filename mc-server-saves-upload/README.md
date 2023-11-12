# 💾 Minecraft存档备份脚本

> 🚧 该脚本正在努力开发中.... 🚧

该脚本用于将服务器的存档文件打包并上传至指定的alist服务器。

## 如何使用

1. 将`.env.example`文件复制为`.env`
2. 按照下面的提示配置`.env`文件
3. 执行`python upload.py`

## `.env`配置内容

```properties
# Alist URL
ALIST_URL=https://alist.example.com
# 认证用户
ALIST_USERNAME=admin
# 认证密码
ALIST_PASSWORD=password
# 存储路径
UPLOAD_DIR=/
# 存储文件名
UPLOAD_FILE=saves
# 压缩格式 可选zip/tar.gz
COMPRESS_FORMAT=tar.gz
# 存档路径
SAVES_DIR=world
```