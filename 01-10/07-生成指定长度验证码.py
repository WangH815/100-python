import random
import string

def gen_code(code_len=4):      # 默认长度为4
    all_chars = string.digits + \
                string.ascii_letters + \
                string.punctuation         # 生成含有所有的数字字母和符号的字符串
    all_chars1 = string.printable          # 同上
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    print(gen_code(10))
    print(gen_code(10))
    print(gen_code(10))
    print(gen_code(10))
    print(gen_code(10))