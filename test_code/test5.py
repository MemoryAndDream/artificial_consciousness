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


class neuron_chain():
    def __init__(self):
        self.content = []
        self.name = ''
        self.id = id(self)

    def append(self, w):
        self.content.append(w)


class token():
    def __init__(self, previous, next, name=''):
        self.previous = previous
        self.next = next
        self.name = name


def remember(target):
    neuron_chains = []
    neuron_chain_now = neuron_chain()
    max_remeber_length = 4
    neuron_chains.append(token(None, neuron_chain_now.id, 'start'))
    for s in target:
        print(s)
        if len(neuron_chain_now.content) + 1 > max_remeber_length:
            neuron_chains.append(neuron_chain_now)
            last_chain_id = neuron_chain_now.id
            neuron_chain_now = neuron_chain()
            neuron_chains.append(token(last_chain_id, neuron_chain_now.id, 'next'))
        neuron_chain_now.append(s)
    neuron_chains.append(neuron_chain_now)
    last_chain_id = neuron_chain_now.id
    neuron_chains.append(token(last_chain_id, None, 'end'))
    return neuron_chains


def recall(memory):
    # 记忆索引 为了方便运算 先将所有chain构成dict
    memory_dict = {}
    token_name_dict = {}
    token_start_dict = {}
    for object in memory:
        if type(object) == type(neuron_chain()):
            memory_dict[object.id] = object
        else:
            token_name_dict[object.name] = object  # 同名token索引困难，就当记混了
            token_start_dict[object.previous] = object

    # 从name为start的token开始回忆
    token = token_name_dict['start']
    next_token = token
    while next_token and next_token.next:
        chain = memory_dict[next_token.next]
        print(chain.content)
        if token_start_dict[chain.id]:
            next_token = token_start_dict[chain.id]


def main():
    target = '1234567891234567'
    memory = remember(target)
    recall(memory)


if __name__ == '__main__':
    main()
