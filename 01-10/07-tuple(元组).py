#与列表类似，区别在于元素不能修改

def main():
    t = ('a', 12, True, '胜多负少') # 定义元组
    list1 = list(t)                # 元组转列表，其他类似

if __name__ == '__main__':
    main()