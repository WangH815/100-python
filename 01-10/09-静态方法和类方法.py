from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod  # 声明为静态方法
    def is_vaild(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_vaild(a, b, c):  # 通过静态方法访问
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())          # 通过实例访问
        print(Triangle.area(t))  # 通过类实例作为参数访问类方法，效果同上
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    main()
