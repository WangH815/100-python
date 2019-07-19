from socket import socket


def main():
    client = socket()                         # 创建套接字，默认使用IPv4和TCP
    client.connect(('192.168.2.3', 6789))     # 连接服务器
    print(client.recv(1024).decode('utf-8'))  # 接收数据
    client.close()                            # 断开连接


if __name__ == '__main__':
    main()
