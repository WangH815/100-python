class Student(object):

    def __init__(self, name, age):  # 用于初始化class
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s。' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看《熊出没》。' % self.name)
        else:
            print('%s可以看岛国大片。' % self.name)


def main():
    stu1 = Student('wangh', 27)
    stu1.study('Python')
    stu1.watch_movie()
    print('============================')
    stu2 = Student('王大锤', 17)
    stu2.study('拼音')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
