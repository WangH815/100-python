from math import sqrt


def is_prim(n):
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    files = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for file in files:
            fs_list.append(open(file, 'w', encoding='utf-8'))
        for num in range(1, 10000):
            if is_prim(num):
                if num < 100:
                    fs_list[0].write(str(num) + '\n')
                elif num < 1000:
                    fs_list[1].write(str(num) + '\n')
                else:
                    fs_list[2].write(str(num) + '\n')
    except IOError as ex:
        print(ex)
        print('文件写入出错...')
    finally:
        for fs in fs_list:
            fs.close()
    print('文件写入成功...')


if __name__ == '__main__':
    main()
