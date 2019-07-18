import json


def main():
    mydict = {  # 创建dict
        'name': 'wangh',
        'age': 27,
        'qq': 123456,
        'friends': ['Lucy', 'Tiny'],  # value为list
        'cars': [  # value为list
            {'brand': 'BYD', 'max_speed': 180},  # list元素为dict
            {'brand': 'Audi', 'max_speed': 260},
            {'brand': 'Benz', 'max_speed': 280}
        ]
    }
    try:
        with open('../../tmp/data.json', 'w', encoding='utf-8') as f:
            json.dump(mydict, f)           # json数据写入到本地文件中（序列化）,反序列化使用load和loads
            data_str = json.dumps(mydict)  # json数据转为json
    except IOError as e:
        print(e)
    print(data_str)
    print('操作完成...')


if __name__ == '__main__':
    main()
