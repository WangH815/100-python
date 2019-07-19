from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    server = socket(family=AF_INET, type=SOCK_STREAM) # 基于IPv4的TCP套接字
    server.bind(('192.168.2.3', 6789))                # 绑定IP和端口
    server.listen(512)                                # 开启监听
    print('服务器开始监听...')
    while True:
        client, addr = server.accept()                   # 获取连接到服务器的的客户端信息
        print(str(addr) + '连接到了服务器...')
        client.send(str(datetime.now()).encode('utf-8')) # 向客户端发送数据
        client.close()                                   # 断开连接


if __name__ == '__main__':
    main()
