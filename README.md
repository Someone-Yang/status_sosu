# 探针索斯！

一款使用 Python Flask 和 Psutil 进行数据展示和采集的轻量设备探针索斯！

## 安装

环境：

- 一台能运行 Python 的设备（例如云服务器）
- 不支持虚拟主机

0. 我们使用uv管理本项目**包括python本身在内**的依赖，若你没有uv，请先[下载安装uv](https://docs.astral.sh/uv/getting-started/installation/)

> Linux / macOS 安装uv： `curl -LsSf https://astral.sh/uv/install.sh | sh`

1. 克隆本仓库

```
git clone https://github.com/Someone-Yang/status_sosu
```

2. 按需配置

3. 转到程序目录，运行主程序 `app.py`

```
cd ./status_sosu
uv run ./app.py
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
web:
  # 设置主题，模板保存在 templates 目录
  theme: "mdui"
  # 以下全部为模板可配置字段
  title: "Status Sosu!"
  mdui-primary-color: "indigo"
client:
  # 一个名字代表一个需要展示的被测端
  # 被测端 clientname 需要与此处设置一致
  demo:
    # 设备名
    name: "Nanachi"
    # 是否显示系统信息及可选自定义系统名
    system:
      display: True
      custom: "Custom system name"
    # 是否显示处理器信息及可选自定义处理器名
    processor:
      display: True
      custom: "Custom CPU name"
    # 架构信息，同理
    machine:
      display: True
      custom: "DMA66"
    # CPU使用率
    cpu-usage:
      display: True
    # 内存使用率
    mem-usage:
      display: True
    # 硬盘使用率
    disk:
      display: True
    # 网络数据
    network:
      display: True
  # 再举例标记一个 test 的机器
  test:
    name: "Another test server"
    system:
      display: True
      custom: "Better than nothing"
    # 自定义名称留空就不是自定义了
    processor:
      display: True
      custom: ""
    machine:
      display: False
      custom: ""
    cpu-usage:
      display: True
    mem-usage:
      display: True
    disk:
      display: False
    network:
      display: True
```
