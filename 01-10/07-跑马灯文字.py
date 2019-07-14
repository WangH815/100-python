import os
import time

def main():
    txt = '上海欢迎你....'       # 文字构建
    while True:                 # 无限循环
        os.system('cls')        # 清屏
        print(txt)              # 打印文字
        time.sleep(2)           # 每2s输出一次
        txt = txt[1:] + txt[0]  # 构建循环文字

if __name__ == '__main__':
    main()