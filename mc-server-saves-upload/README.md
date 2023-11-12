# 💾 Minecraft存档备份脚本

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

## TODO

- [ ] MCDR插件，实现在服务器内使用命令执行
- [ ] 定时执行脚本
- [ ] 执行失败时发送邮件/信息
- [ ] 支持中文目录
- [ ] 支持后台执行

## CHANGELOG

**v1.0:**

- 自动压缩存档文件，支持zip和tar.gz两种格式
- 能够自动上传至alist
- 支持自定义目录、文件名
- 支持展示上传进度
- 自动删除alist中已经存在的存档文件

## 开发者信息

💻 开发: zhengyi59