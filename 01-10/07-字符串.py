def main():
    string = 'hello, Python! '
    print(string)
    print(len(string))
    print(string.strip())         # 去除首尾空格
    print(string.capitalize())    # 首字母大写
    print(string.upper())
    print(string.find('lo'))      # 查找子串，返回位置
    print(string.index('lo'))     # 同上，找不到会有异常
    print(string.startswith('h')) # 判断是否以指定字符串开头
    print(string.endswith(' '))   # 判断是否以指定字符串结尾
    print(string.center(50, '*')) # 指定总长度，并左右填充星号
    print(string.rjust(50, '*'))  # 同上，左填充。右填充同理

    print(string.isdigit())      # 判断字符串是否由数字构成
    print(string.isalpha())      # 判断字符创是否由字母构成
    print(string.isalnum())      # 判断字符创是否由字母数字构成

    #字符串切片
    str1 = '123abcd '
    # 正向位置是  0  1  2  3  4  5  6
    # 反向位置是 -7 -6 -5 -4 -3 -2 -1
    # 切片语法  str[起始位置:截至位置:步长]  , 切片范围按数学集合可表示 [起始位置,截至位置)
    # 起始位置和截至位置默认是字符串开始和结束位置，其余按照正反向位置确定
    # 步长默认是1，表示正向以步长为1截取，负数则表示反向截取
    # 这三个参数都可以省略

    print(str1[2])             # 去指定位置字符，位置从0开始
    print(str1[1:])            # 截取指定位置之后的子串
    print(str1[-2:])           # 同上，指定位置反向
    print(str1[:3])            # 截取指定位置之前的子串
    print(str1[2:5])           # 截取指定位置之间的子串
    print(str1[-5:-2])         # 同上
    print(str1[5:1:-1])        # 反向截取指定位置之间，此时需要注意位置参数
    print(str1[::-1])          # 反向输出字符串
    print(str1[:])             # 完整切片


if __name__ == '__main__':
    main()