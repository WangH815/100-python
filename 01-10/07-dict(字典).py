# dict（字典）相当于java中的map，以 key:value 的形式

def main():
    scores = {'张三': 75, '李四': 67, '王五': 89, '王五2': 89} # 创建字典
    print(scores['李四'])      # 按key获取value，key不存在会有异常
    print(scores.get('a'))     # 同上，key不存在时返回 None
    print(scores.get('a', 6))  # 同上，key不存在时返回指定值6

    # 遍历字典
    for elem in scores:
        print('%s --> %d' % (elem, scores[elem]))

    scores['张三'] = 76             # 修改或新增value
    scores['张三'] = None           # value置空
    scores.update(张三=77, 刘六=99)  # 同上
    scores.popitem()                # 删除最后一个元素，出栈
    scores.pop('王五')              # 按key删除元素，key不存在产生异常
    scores.pop('王五2', 90)         # 按key：value删除元素，key存在则可以删除，key或者value不匹配都不会报错
    scores.pop('王五3', None)       # 同上，报错
    scores.clear()                  # 清空字典

    print(scores)


if __name__ == '__main__':
    main()
