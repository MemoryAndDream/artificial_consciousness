# -*- coding: utf-8 -*-
"""
Description : 原型代码2 增加数据量测试单链记忆模型，以及测试记忆与回忆同时进行
date：          2023/10/15
"""
import jieba
import re
import math


def read_file():
    with open('/Users/mengzhihao/work/py3/artificial_consciousness/articles/big_txt/atsth.txt') as f:
        contents = f.read()
        words = jieba.cut(contents, cut_all=False)
        return words


def f_tired(t):
    return t / 10 if t < 10 and t > 0 else 1


def f_strengthen(count):
    return 1 - math.e ** -count


def f_link(linked):
    return 10 if linked else 1


def learn():
    words_dicts = {}
    words = read_file()
    last_word = ''
    t = 0
    for word in words:
        word = word.strip()
        if re.match(r'[\u4e00-\u9fa5\w，。]+', word):
            # print(word)
            # t += 1 # 长期记忆先不计算疲劳
            if word not in words_dicts:
                words_dicts[word] = {}
            if last_word:
                # 记录下一个词的激活时间，激活次数
                if not word in words_dicts[last_word]:
                    words_dicts[last_word][word] = [t, 1]  # [t,n]
                else:
                    activate_count = words_dicts[last_word][word][1]
                    words_dicts[last_word][word] = [t, activate_count + 1]
            last_word = word
    return words_dicts


def first_read(words_dicts, input):
    last_word = input
    print(input)
    output_dicts = {}

    for i in range(100):
        # 不断输出下一个最强词。如果思维中断了，那就从最近几个词找。
        if not words_dicts[last_word]:
            break
        else:
            max_exciting, next_word = 0, ''
            for word in words_dicts[last_word]:
                t, activate_count = words_dicts[last_word][word]
                exciting = f_tired(i - t) * f_strengthen(activate_count) * f_tired(i - output_dicts.get(word, 0))

                if exciting > max_exciting:
                    max_exciting, next_word = exciting, word
            words_dicts[last_word][next_word] = [i, words_dicts[last_word][next_word][1] + 1]
            last_word = next_word
            output_dicts[last_word] = i
            print(next_word, end='')


def main():
    words_dicts = learn()
    input = '北极'
    first_read(words_dicts, input)


if __name__ == '__main__':
    main()
    # 感觉单链效果很糟糕，还是要先多词试试 改进到3词链接模型
