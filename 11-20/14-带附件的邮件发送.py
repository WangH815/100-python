from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    message = MIMEMultipart()
    text_content = MIMEText('数据见附件', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', utf - 8)
    message.attach(text_content)

    with open('path/附件.zip', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=附件.rar'
        message.attach(txt)
    with open('path/附件.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=附件.xlsx'
        message.attach(xls)

    smtper = SMTP('smtp.163.com')
    sender = 'a@163.com'
    receivers = ['b@163.com', 'b@163.com']
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('发送完成')


if __name__ == '__main__':
    main()
