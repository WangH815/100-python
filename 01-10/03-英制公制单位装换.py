value = float(input('请输入长度：'))
unit = str(input('请输入单位 "cm" 或 "inch"：'))

if unit == 'cm':
    print('%f英寸 = %f厘米' % (value/2.54,value))
elif unit == 'inch':
    print('%f英寸 = %f厘米' % (value,value*2.54))
else:
    print('单位输入错误...')