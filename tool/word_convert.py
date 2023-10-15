# -*- coding: utf-8 -*-
# 碰到某些文件有乱码之类的问题
import re


def remove_error_code(byte_string, charset):
    for try_times in range(100):
        try:
            result = byte_string.decode(charset)
            break
        except Exception as e:
            stre = str(e)
            index = re.search('in position (\d+)', stre).group(1)
            if index:
                index = int(index)
                byte_string = byte_string[:index] + byte_string[index + 1:]
    print(try_times)
    return result


def encode_convert():
    with open('/Users/mengzhihao/work/py3/artificial_consciousness/articles/big_txt/安徒生童话故事集.txt', mode='rb') as f:
        all = f.read()
        rs = remove_error_code(all, 'gbk')
        with open('/Users/mengzhihao/work/py3/artificial_consciousness/articles/big_txt/atsth.txt', 'w') as f:
            f.write(rs)


def remove_blank():
    with open('/Users/mengzhihao/work/py3/artificial_consciousness/articles/big_txt/atsth.txt') as f:
        contents = f.read()
        contents = re.sub("\s", '', contents)
        print(contents)


if __name__ == '__main__':
    # encode_convert()
    remove_blank()
