'''
用户名：字母数字下划线构成，长度为6~20
QQ号：5~12位数字构成，首位不为0
'''

import re


def main():
    username = input('请输入用户名：')  # 输入用户名
    qq = input('请输入QQ号：')          # 输入QQ号
    # re.match用于匹配查找
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)  # 匹配不上m1为None
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    print(m1, m2)
    if not (m1 and m2):
        print('用户名或QQ号非法...')


if __name__ == '__main__':
    main()
