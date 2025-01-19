# 探针索斯！

一款使用 Python Flask 和 Psutil 进行数据展示和采集的轻量设备探针索斯！

## 安装

环境：

- 一台能运行 Python 的设备（例如云服务器）
- 不支持虚拟主机

0. 我们使用 UV 管理本项目**包括 Python 本身在内**的依赖，若运行服务端的设备没有 UV，建议先[下载安装 UV](https://docs.astral.sh/uv/getting-started/installation/)

> Linux / macOS 安装uv： `curl -LsSf https://astral.sh/uv/install.sh | sh`

1. 克隆本仓库

```
git clone https://github.com/Someone-Yang/status_sosu
```

2. 按需配置

请在本项目根目录 `config.yml` 配置文件中设置服务端（展示端）密钥、端口等必须信息，以便客户端（被测端）正确上传数据。

3. 转到程序目录，运行主程序 `app.py`

```
cd ./status_sosu
uv run ./app.py
```

如果追求 *“极致的轻量化”* 没有安装 UV，也可以在拥有相关库时直接使用 Python3 运行
```
python3 ./app.py
```

4. 直接暴露端口或使用 Nginx 等服务器转发端口，以便被测端可以正常访问

被测端需要使用 [status_sosu_client](https://github.com/Someone-Yang/status_sosu_client) 上传状态信息。

## 更新

拉取本仓库或覆盖安装

```
git pull
```

## 配置

在根目录中有一个配置文件 `config.yml`。每次修改后**需要重启服务端生效**。

配置功能见文件中的注释。
