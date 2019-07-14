def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b #先计算右侧再赋值给左侧
        yield a         #含有 yield 的为生成器，会保存每次执行的值

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()