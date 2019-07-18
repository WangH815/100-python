import re


def main():
    pt = re.compile(r'(?<=\D)1[3457]\d{9}(?=\D)')
    data = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pt, data)
    print(mylist)
    print()
    # 通过迭代器获取匹配对象的内容
    for tmp in pt.finditer(data):
        print(tmp.group())

    print()
    m = pt.search(data)
    while m:
        print(m.group())
        m = pt.search(data, m.end())


if __name__ == '__main__':
    main()
