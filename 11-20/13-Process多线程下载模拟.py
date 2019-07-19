from multiprocessing import Process  # 支持跨平台多线程编程
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())  # 获取进程号
    print('开始下载%s...' % filename)
    time_download = randint(5, 10)  # 模拟下载时间
    sleep(time_download)
    print('%s下载完成！耗时%ds' % (filename, time_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=(' Python教程.pdf ',))
    p1.start()
    p2 = Process(target=download_task, args=(' 小电影.avi ',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗时%.2fs.' % (end - start))


if __name__ == '__main__':
    main()
