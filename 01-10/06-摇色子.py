from random import randint

def roll_dice(n = 2):  # 默认参数，参数没有给的时候使用默认参数2
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a = 0, b = 0, c = 0):
    return a + b + c

def adds(*args):   # 不定长参数
    total = 0
    for var in args:
        total += var
    return  total

print(roll_dice())   # 默认调用
print(roll_dice(3))  # 含参调用

print(add())
print(add(1))
print(add(c = 12, a = 56, b = 78))  # 参数名给出的情况下，参数顺序无要求

print(adds(1, 2, 3, 4))