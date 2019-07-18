import requests  # 需要执行 pip install requests 安装
import json

def main():
    # 通过get请求获取数据
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_json = json.loads(resp.text)  # 将str转为json
    for news in data_json['newslist']: # 查找title
        print(news['title'])

if __name__ == '__main__':
    main()