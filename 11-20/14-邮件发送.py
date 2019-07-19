from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'a@163.com'                                    # 发送人
    receivers = ['b@163.com', 'b@163.com']                  # 收件人
    message = MIMEText('Python邮件正文', 'plain', 'utf-8')   # 邮件正文
    message['From'] = Header('王大锤', 'utf-8')              #
    message['To'] = Header('WangH', 'utf-8')
    message['Subject'] = Header['示例邮件']                  # 主题
    smtper = SMTP('smtp.163.com')                           # 指定smtp服务器
    smtper.login(sender, 'password')                        # 登录
    smtper.sendmail(sender, receivers, message.as_string()) # 发送邮件
    print('邮件发送成功...')


if __name__ == '__main__':
    main()
