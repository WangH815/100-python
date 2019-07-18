import time


def main():
    with open('../../tmp/1.txt', 'r', encoding='utf-8') as f:
        print(f.read())            # 一次读取所有内容

    with open('../../tmp/1.txt', 'r', encoding='utf-8') as f:
        for line in f:             # 逐行读取,带有换行符 \n
            print(line, end='')    # 不换行，如不使用end会输出空行
            time.sleep(0.5)        # 每隔0.5s输出一次
        print()

    with open('../../tmp/1.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()      # 读取到列表中
    print(lines)


if __name__ == '__main__':
    main()
