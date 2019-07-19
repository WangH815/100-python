from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):  # 继承Thread类
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):  # 重写run()方法
        print('开始下载%s...' % self._filename)
        time_download = randint(5, 10)
        sleep(time_download)
        print('%s下载完成！耗时%ds.' % (self._filename, time_download))


def main():
    start = time()
    t1 = DownloadTask(' Python教程.pdf ')
    t1.start()
    t2 = DownloadTask(' 小电影.avi ')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2fs.' % (end - start))


if __name__ == '__main__':
    main()
