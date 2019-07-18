import re


def main():
    pope = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    data_list = re.split(r'[，。,.]',pope)
    while '' in data_list:
        data_list.remove()
    print(data_list)

if __name__ == '__main__':
    main()