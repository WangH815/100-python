class Person(object):
    __slots__ = ('_name', '_age')  # 限制当前类只能绑定这两个属性，对子类无影响

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # 访问器getter方法
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter  # 修改器setter方法
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 8:
            print('%s正在玩泥巴...' % self._name)
        else:
            print('%s正在踢足球...' % self._name)


def main():
    person = Person('王大锤', 8)
    person.play()
    person.age = 10  # 调用修改器
    person.play()
#    person.name = 'wangh'  # 会报错，无法修改


if __name__ == '__main__':
    main()
