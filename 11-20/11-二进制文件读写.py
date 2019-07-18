def main():
    try:
        with open('../../tmp/1.txt', 'rb') as f1:  # 二进制读模式打开文件，使用相对路径
            data = f1.read()                       # 读取
        with open('../../tmp/2.txt', 'wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print('文件不存在...')
    except IOError as e:
        print('文件读写出错...')
    print('操作完成...')


if __name__ == '__main__':
    main()
