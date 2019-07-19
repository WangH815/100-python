from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclent = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = '123.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclent.send(json_str.encode('utf-8'))  # 文件编码
            self.cclent.close()

    server = socket()
    server.bind('192.168.2.3', 5678)
    server.listen(512)
    print('服务器开始监听...')
    with open('123.jpg', 'rb') as f:
        data = b64encode(f.read().decode('utf-8'))  # 文件解码
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
