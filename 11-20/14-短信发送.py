import urllib.parse
import http.client
import json


def main():
    host = '106.ihuyi.com'  # 使用互亿短信平台
    sms_send_uri = '/webservice/sms.php?method=Submit'
    params = urllib.parse.urlencode({'account': '用户名',
                                     'password': '密码',
                                     'content': '您的验证码是134123',
                                     'moble': '18812341234',
                                     'format': 'json'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    json_str = response_str.decode('utf-8')
    print(json.loads(json_str))
    conn.close()


if __name__ == '__main__':
    main()
