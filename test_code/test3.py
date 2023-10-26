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


def f_tired(t):  # 不疲劳容易死循环
    return t / 10 if t < 10 and t > 0 else 1


def f_strengthen(count):
    return 1 - math.e ** -count


def f_link(linked):
    return 10 if linked else 1


def f_forget(d):
    return 1 / (2 ** d)


def new_learn():
    # 先不考虑标点，测试跨词模型，跨度4词,先不添加助记词
    words_dicts = {}  # abc:1, ab:1, ac:1 b:1 bc:1 c:1
    words = read_file()
    index = 0
    last_words = ['', '', '', '', '', '']
    t = 0  # 先不考虑疲劳
    for this_word in words:
        this_word = this_word.strip()
        if not re.match(r'[\u4e00-\u9fa5\w，。]+', this_word):
            continue
        index += 1
        if index < 7:  # 从第7个词开始记 前面几个先不记了
            pass
        else:
            distance = 6
            for old_word in last_words:
                if old_word not in words_dicts:
                    words_dicts[old_word] = {}
                    # 记录下一个词的激活时间，激活次数
                if not this_word in words_dicts[old_word]:
                    words_dicts[old_word][this_word] = [t, f_forget(distance)]  # [t,n]
                else:
                    activate_count = words_dicts[old_word][this_word][1]
                    words_dicts[old_word][this_word] = [t, activate_count + f_forget(distance)]

                distance -= 1

        last_words.pop(0)
        last_words.append(this_word)

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
                # 这里不对！回忆要和记忆的逻辑整合！不能只看上一个词 代码整合一下
                if exciting > max_exciting:
                    max_exciting, next_word = exciting, word
            words_dicts[last_word][next_word] = [i, words_dicts[last_word][next_word][1] + 1]
            last_word = next_word
            output_dicts[last_word] = i
            print(next_word, end='')


def main():
    words_dicts = new_learn()
    input = '北极'
    first_read(words_dicts, input)


if __name__ == '__main__':
    main()
