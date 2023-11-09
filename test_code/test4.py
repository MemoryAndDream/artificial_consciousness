# -*- coding: utf-8 -*-
"""
Description : 原型代码4 继续优化基于双词记忆的记忆模型。增加助记词。 这次为了简化记忆。只记录13812342234 助记词先用人工助记词，再尝试自然助记词
# 测试发现不对劲，结果变成13423423423423423423
date：          2023/10/31
"""

myphone = '13812342234'
rem = ['start','1','3','8','next','1','2','3','4','last','2','2','3','4','end']
def f_forget(d):
    return 1 / (1.5 ** d)

# 记忆
forget_length = 4
last_words = ['']*forget_length
words_dicts = {}
for this_word in rem:
    distance = forget_length
    for old_word in last_words:
        if old_word not in words_dicts:
            words_dicts[old_word] = {}
        if not this_word in words_dicts[old_word]:
            words_dicts[old_word][this_word] =  f_forget(distance)
        else:
            activate_count = words_dicts[old_word][this_word]
            words_dicts[old_word][this_word] = activate_count + f_forget(distance)
        distance-=1

    last_words.pop(0)
    last_words.append(this_word)


# 回忆

input = 'start'
previous_words = ['']*forget_length
previous_words[-1] = input
for i in range(20):
    last_word = previous_words[-1]
    if not words_dicts[last_word]:
        break
    else:
        max_exciting, next_word = 0, ''
        for word in words_dicts[last_word]:
            exciting = 0
            for d in range(1, forget_length+1, 1):
                old_word = previous_words[-d]
                if not old_word:
                    continue
                activate_count = words_dicts[old_word].get(word,  0)
                if activate_count:
                    exciting += activate_count

            # 这里不对！回忆要和记忆的逻辑整合！不能只看上一个词 代码整合一下
            if exciting > max_exciting:
                max_exciting, next_word = exciting, word
        previous_words.pop(0)
        previous_words.append(next_word)
        print(next_word, end='')