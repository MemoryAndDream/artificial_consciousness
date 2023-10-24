# -*- coding: utf-8 -*-
"""
Description : 原型代码2 增加数据量测试n词链记忆模型，以及测试记忆与回忆同时进行
abc:
-a -b -ab -bc -abc -c

先做句子内部记忆，句子之间先不做
date：          2023/10/15
"""
import jieba
import re
import math


def read_file():
    with open('/Users/mengzhihao/work/py3/artificial_consciousness/articles/big_txt/atsth.txt') as f:
        contents = f.read()
        contents = re.sub("\s", '', contents)
        words = jieba.cut(contents, cut_all=False)
        return words


def f_tired(t):
    return t / 10 if t < 10 and t > 0 else 1


def f_strengthen(count):
    return 1 - math.e ** -count


def f_link(linked):
    return 10 if linked else 1


def learn():
    # 3词链模型，但是出现标点截止
    words_dicts = {}
    words = read_file()
    first_word = ''
    second_word = ''
    third_word = ''
    t = 0
    for i in range(len(words)):
        this_word = words[i]
        if re.match(r'[\u4e00-\u9fa5\w，。?!]+', this_word):
            # print(word)
            # t += 1 # 长期记忆先不计算疲劳
            if word not in words_dicts:
                words_dicts[word] = {}
            if first_word:
                # 记录下一个词的激活时间，激活次数
                if not word in words_dicts[last_word]:
                    words_dicts[last_word][word] = [t, 1]  # [t,n]
                else:
                    activate_count = words_dicts[last_word][word][1]
                    words_dicts[last_word][word] = [t, activate_count + 1]
            last_word = word
    return words_dicts


def new_learn():
    # 1 句子根据标点拆成词组
    words_dicts = {}  # abc:1, ab:1, ac:1 b:1 bc:1 c:1
    words = read_file()
    index = 0
    for word in words:
        index += 1
        if not re.match(r'[，。?!]+', word):
    # 记忆


def first_read(words_dicts, input):
    last_word = input
    print(input)
    output_dicts = {}

    for i in range(20):
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
