from math import sqrt


def is_prim(n):    # 判断是否是素数
    assert n > 0   # 断言，要求n必须大于0
    for factor in range(2, int(sqrt(n)) + 1):  # 缩小取数范围
        if n % factor == 0:                    # 取是否能整除
            return False
    return True if n != 1 else False           # 去掉1


def main():
    files = ('../../tmp/a.txt', '../../tmp/b.txt', '../../tmp/c.txt')   # 文件名元组(tuple)，有序不可变
    fs_list = []                          # 空列表(list)，有序可变
    try:
        for file in files:
            fs_list.append(open(file, 'w', encoding='utf-8'))  # 创建文件
        for num in range(1, 10000):
            if is_prim(num):
                if num < 100:
                    fs_list[0].write(str(num) + '\n')  # 写入文件
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
    print('操作完成...')


if __name__ == '__main__':
    main()
