import time


def main():
    with open('1.txt', 'r', encoding='utf-8') as f:
        print(f.read())  # 一次读取所有内容

    with open('1.txt', 'r', encoding='utf-8') as f:
        for line in f:   # 逐行读取
            print(line, end='')
            time.sleep(0.5)
        print()

    with open('1.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取到列表中
    print(lines)


if __name__ == '__main__':
    main()
