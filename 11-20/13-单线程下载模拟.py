from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_download = randint(5, 10)
    sleep(time_download)
    print('%s下载完成！耗时%ds' % (filename, time_download))


def main():
    start = time()
    download_task(' Python教程.pdf ')
    download_task(' 小电影.avi ')
    end = time()
    print('总共耗费了%.2fs' % (end - start))


if __name__ == '__main__':
    main()
