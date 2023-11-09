# -*- coding: utf-8 -*-
"""
Description : test4中 1234567891234567会被拆成
['1', '2', '3', '4']
['5', '6', '7', '8']
['9', '1', '2', '3']
['4', '5', '6', '7']
这样不符合实际记忆中8-9不拆开的特性，助记词是一个后天技巧，但是先天记忆记不住太长的东西，而切换思维，
天然停顿就是个助记词
助记词相当于一个概念神经元，助记词之间也遵循联想关系


date：          2023/11/05
"""




def main():
    target = '1234567891234567'
    memory = remember(target)
    recall(memory)


if __name__ == '__main__':
    main()
