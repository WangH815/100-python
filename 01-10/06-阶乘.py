def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

m = int(input('请输入一个正整数：'))

if m > 0:
    print('这个正整数的阶乘是：', factorial(m))
else:
    print('输入非法...')