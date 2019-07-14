import sys

def main():
    list1 = [1, 5, 3, 7, 100]   # 构建列表，由[]构成
    print(list1)                # 打印列表
    print(len(list1))           # 列表长度
    print(list1[3])             # 列表指定元素
    print(list1[1:5:2])         # 切片，与字符串切片类似

    list1.append(200)           # 追加元素
    list1 += [3, 4]             # 同上，区别在于会产生新的列表
    list1.insert(1, 400)        # 指定位置插入元素

    list1.remove(3)             # 删除指定位置元素
    del list1[2]                # 同上
#    list1.clear()              # 清空列表元素

    print(sorted(list1))        # 排序，默认为升序。不改变原列表
    # 降序排序
    print(sorted(list1, reverse=True))
    list1.sort()                # 排序，默认为升序。改变原列表
    list1.sort(reverse=True)    # 降序，同上

    # 按长度排序（字符串列表），默认为升序
    print(sorted(['df','as','a','asd'], key=len))

    # 创建列表
    list2 = [x for x in range(1,10)]
    # 创建列表，类似完全交换
    list2 = [x + y for x in 'abc' for y in '123']
    # 生成器创建列表容器，一次性生成全部元素，比较消耗内存
    list2 = [x ** 2 for x in range(1,1000)]
    print(sys.getsizeof(list2))   # 查看对象占用内存字节数
    # 不占额外内存，实际产生生成器对象，获取数据须通过计算，需要一定时间
    list2 = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(list2))  # 查看对象占用内存字节数
    print(list2)


if __name__ == '__main__':
    main()