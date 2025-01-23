
```markdown
# LinuxControl

**LinuxControl** 是一个基于网络的远程控制工具，允许 Linux 系统远程控制 Windows 机器。通过简单的脚本和命令行输入，用户可以执行命令、管理文件和控制 Windows 系统的操作，无需额外的代理或 VPN 配置。

## 功能

- 通过 IPv6 协议远程连接和控制 Windows 系统。
- 执行 Windows 系统上的命令。（暂未开发）
- 支持远程文件传输。（暂未开发）
- 支持截图功能。（暂未开发）
- 简单易用的命令行界面。

## 安装

### 依赖项

**重要提示：** 本项目需要 Python 3 环境，请确保使用 **Python 3.x** 版本。您可以使用以下命令检查当前安装的 Python 版本：

```bash
python --version
# 或者
python3 --version
```

如果没有安装 Python 3，请访问 [Python 官网](https://www.python.org/downloads/) 下载并安装。

安装 Python 3 后，确保你已安装项目的依赖库。在项目目录下运行以下命令安装依赖项：

```bash
pip3 install -r requirements.txt
```

### 设置 Linux 服务器端

1. 下载并解压项目文件到 Linux 系统。
2. 编辑 `config.py` 文件，设置 Windows 主机的相关信息（如 IP 地址、端口号等）。
3. 运行服务器端脚本：

```bash
python3 s.py
```

这将启动监听服务，等待来自 Windows 客户端的连接。

### 设置 Windows 客户端

1. 下载并解压项目文件到 Windows 系统。
2. 编辑 `config.py` 文件，设置 Linux 服务器的相关信息。
3. 运行客户端脚本：

```bash
python3 c.py
```

客户端将连接到 Linux 服务器，等待接收命令。

## 使用方法

### 在 Linux 上执行命令

1. 运行 `s.py` 脚本，等待 Windows 客户端连接。
2. 在 Linux 终端输入命令进行控制：

```bash
Enter command to execute on Windows (or type 'exit' to quit): dir
```

3. 在 Windows 客户端上，终端会显示执行结果。

### 在 Windows 上执行命令

1. 运行 `c.py` 脚本，连接到 Linux 服务器。
2. 输入命令：

```bash
Enter command to execute (or type 'exit' to quit): ipconfig
```

3. 命令结果会显示在 Linux 服务器端终端。

### 退出程序

- 在任何时刻，输入 `exit` 以退出程序。

## 注意事项

- 本工具要求 Python 3 环境，**不支持 Python 2**。
- 该工具基于 IPv6 协议工作，确保两台机器都支持 IPv6。
- 默认端口为 9999，您可以根据需要修改端口号。
- 本工具仅支持 Windows 和 Linux 环境。

## 联系方式

如果你遇到任何问题，或者有任何建议，欢迎通过以下方式联系我：

- 邮箱：zhaowenda2000@gmail.com
- GitHub：github.com/lichengyi1993
```

### 关键更新：
1. **Python 3 强调**：
   - 在 "安装" 部分明确要求使用 Python 3，提供了检查 Python 版本的命令。
   - 明确指出本工具 **不支持 Python 2**。
   
2. **使用 `python3`**：
   - 在所有运行命令的示例中使用 `python3`，确保用户使用正确的 Python 版本来运行脚本。

这样可以有效地避免用户误用 Python 2，确保项目能够正确运行。
