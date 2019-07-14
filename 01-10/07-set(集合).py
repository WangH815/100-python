# 集合元素不重复

def main():
    set1 = {1, 2, 'a', 4, 4}  # 创建后自动去重
    set2 = set(range(1, 10))  # 同上
    set1.add('1')             # 追加元素
    set1.remove(1)            # 删除元素，元素不存在会有异常
    set1.discard(11)          # 同上，无异常
    set1.update([8, 10])      # 更新列表将列表中元素追加到集合中

    for elem in set2:         # 遍历集合
        print(elem ** 2, end=' ')  # ** 用于str和num，用于str表示复制多次，用于num表示乘法运算
    print()

    set3 = set((1, 2, 3, 4))   # 元组转集合
    print(set3.pop())          # 删除栈顶元素
    print(set3.pop())
    print(set1 & set2)              # 交集
    print(set1.intersection(set2))  # 同上
    print(set1 | set2)              # 并集
    print(set1.union(set2))         # 同上
    print(set1 - set2)              # 差集，即set1去除交集
    print(set1.difference(set2))    # 同上
    print(set1 ^ set2)              # 对称差集，即并集去除交集
    print(set1.symmetric_difference(set2))  # 同上
    print((set1 | set2) - (set1 & set2))    # 同上

    print(set2 <= set1)         # 判断set2是否是set1的子集
    print(set2.issubset(set1))  # 同上
    print(set2 >= set1)         # 判断set2是否是set1的超集
    print(set2.issuperset(set1))    # 同上

    print(set1)
    print(set2)


if __name__ == '__main__':
    main()