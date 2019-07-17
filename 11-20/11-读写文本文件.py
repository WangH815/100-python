def main():
    try:  # try except finally 语句
        with open('1.txt', 'r', encoding='utf-8') as f:  # with 语句打开文件
            print(f.read())
    except FileNotFoundError:
        print('文件不存在...')
    except LookupError:
        print('指定文件编码错误...')
    except UnicodeDecodeError:
        print('文件解码错误...')
    finally:
        pass


if __name__ == '__main__':
    main()
