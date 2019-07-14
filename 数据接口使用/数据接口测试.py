import tushare as ts

pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181231',
                   fields='exchange,cal_date,is_open,pretrade_date',
                   is_open='0')
data = pro.stock_basic(exchange='',
                       list_status='L',
                       fields='ts_code,symbol,name,area,industry,list_date')

data = str(data)
print(data)

with open('data.txt', 'w') as f:
    f.write(data)
