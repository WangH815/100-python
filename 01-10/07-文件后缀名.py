def get_suffix(file_name, is_dot = False):
    pos = file_name.rfind('.')             #从右往左查找你一个出现 . 的位置
    if 0 < pos < len(file_name) - 1:
        index = pos if is_dot else pos + 1 # 确定返回值是否带 .
        return file_name[index:]
    else:
        return ''

if __name__ == '__main__':
    print(get_suffix('asdasda.asdf'))