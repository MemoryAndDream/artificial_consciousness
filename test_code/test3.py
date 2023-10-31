# -*- coding: utf-8 -*-
"""
Description : 原型代码3 简化多词关系为双词关系
abc:
-a -b -ab -bc -abc -c

date：          2023/10/15
"""
import jieba
import re
import math
import sys


def read_file():
    with open('../articles/big_txt/atsth.txt',encoding='utf8') as f:
        contents = f.read()
        contents = re.sub("\s", '', contents)
        words = jieba.cut(contents, cut_all=False)
        return words


def f_tired(t):  # 不疲劳容易死循环
    return t / 10 if t < 10 and t > 0 else 1


def f_strengthen(count):  # 与衰减冲突!!但是不加这个会导致助词权重过大 需要重新设计关系！
    return 1 - math.e ** -count


def f_link(linked):
    return 10 if linked else 1


def f_forget(d):
    return 1 / (1.5 ** d)  # 2的话前面所有词相加都不如最近的词，1则是失去顺序性


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
    print(input)
    output_dicts = {}
    previous_words = ['', '', '', '', '', input]
    for i in range(100):
        # 不断输出下一个最强词。
        last_word = previous_words[-1]
        if not words_dicts[last_word]:
            break
        else:
            max_exciting, next_word = 0, ''
            for word in words_dicts[last_word]:  # 这里简化计算，从和最近一个词有联系的词里算
                exciting = 0
                for d in range(1, 7, 1):
                    old_word = previous_words[-d]
                    if not old_word:
                        continue

                    t, activate_count = words_dicts[old_word].get(word, [0, 0])
                    if activate_count:
                        exciting += f_tired(i - t) * f_strengthen(activate_count) * f_tired(
                            i - output_dicts.get(word, 0))  # 注意，记的时候已经计算过距离衰减了，回忆的时候就不用了

                # 这里不对！回忆要和记忆的逻辑整合！不能只看上一个词 代码整合一下
                if exciting > max_exciting:
                    max_exciting, next_word = exciting, word
            words_dicts[last_word][next_word][0] = i  # 先不考虑回忆中记忆s
            output_dicts[last_word] = i
            previous_words.pop(0)
            previous_words.append(next_word)
            print(next_word, end='')


def main():
    words_dicts = new_learn()
    input = '北极'
    # a = words_dicts['北极']
    # b = words_dicts['光照']
    first_read(words_dicts, input)
    # c = 3
    # # 北极的 1.3 北极在 0.4
    # 光照的
    # 1.3
    # 光照在
    # 2.8


if __name__ == '__main__':
    main()

# 北极 光照 -的/在
