import math

a = float(input('请三角形输入边长a：'))
b = float(input('请三角形输入边长b：'))
c = float(input('请三角形输入边长c：'))

if a + b > c and b + c > a and a + c > a:
    print('三角形周长是：%.2f' % (a + b + c))
    p = (a + b + c)/2
    print('三角形面积是：%.2f' % math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print('不能构成三角形...')