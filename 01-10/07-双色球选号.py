from random import randrange, randint, sample


def display(balls):
    for index, ball in enumerate(balls):  # index表示循环次数，enumerate()为枚举对象
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')   # 数字格式化
    print()


def random_select():
    red_balls = [x for x in range(1, 34)]  # 红球号码生成器
    selected_balls = []
    selected_balls = sample(red_balls, 6)  # 生成6个不重复红球，还可考虑使用set实现
    selected_balls.sort()                  # 对红球进行排序
    selected_balls.append(randint(1, 16))  # 追加一个蓝球
    return selected_balls


if __name__ == '__main__':
    n = int(input('请输入注数：'))
    for _ in range(n):
        display(random_select())
