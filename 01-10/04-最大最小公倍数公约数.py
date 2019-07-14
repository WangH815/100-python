import sys

x = int(input('请输入一个正整数:'))
y = int(input('请输入另一个正整数:'))

if x < 1 or y < 1:
    print('输入的不是正整数...')
    sys.exit()

if x > y:
    x, y = y, x

for i in range(x, 0, -1):  # -1 表示以一递减
    if x % i == 0 and y % i == 0:
        print('两个数的最大公约数是：',i)
        print('两个数的最小公倍数是：',x * y / i)
        break
