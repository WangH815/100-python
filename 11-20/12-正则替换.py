import re


def main():
    data = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', data, flags=re.IGNORECASE)
    print(purified)


if __name__ == '__main__':
    main()
