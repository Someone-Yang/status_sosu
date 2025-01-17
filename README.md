# 探针索斯！

一款使用 Python Flask 和 Psutil 进行数据展示和采集的轻量设备探针索斯！。

## 安装

环境：

- 一台能运行 Python 的设备（例如云服务器）
- 不支持虚拟主机

1. 克隆本仓库

```
git clone https://github.com/Someone-Yang/status_sosu
```

2. 按需配置

3. 转到程序目录，运行主程序 `app.py`

```
cd ./status_sosu
python ./app.py
```

4. 直接暴露端口或使用 Nginx 等服务器转发端口，以便被测端可以正常访问

被测端需要使用 [status_sosu_client](https://github.com/Someone-Yang/status_sosu_client) 上传状态信息。

## 更新

拉取本仓库或覆盖安装

```
git pull
```

## 配置

在根目录中有一个配置文件 `config.yml`，类似下文。

```
host:
  # 密钥，被测端需要和此处密钥填写一致
  secret: "faputa"
  # 网页端口
  port: 5000
client:
  # 一个名字代表一个需要展示的被测端
  # 被测端 clientname 需要与此处设置一致
  demo:
```