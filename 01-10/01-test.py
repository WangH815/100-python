x = 1
y = 2

(x, y) = (y, x) if x > y else (x, y)

print(x, y)


print('a>b') if x > y else print('a<b')
'''
等价于
'''
if x > y:
    print('a>b')
else:
    print('a<b')
