def is_leap(year):  # 假设 year 为4位数字
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(date):  # 假设 date 为数字或字符串，可加验证代码
    #
    year = int(str(date)[:-4])
    month = int(str(date)[-4:-2])
    day = int(str(date)[-2:])

    Cumulative = (0, 0, 1, -1, 0, 0, 1, 1, 2, 3, 3, 4, 4)
    Cumulative_leap = (0, 0, 1, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5)

    totol = 30 * (month - 1) + day
    if is_leap(year):
        return totol + Cumulative_leap[month]
    else:
        return totol + Cumulative[month]


if __name__ == '__main__':
    print(is_leap(2004))
    print(which_day('20160301'))
    print(which_day('20161231'))
    print(which_day(40708))
    print(which_day('00040708'))

