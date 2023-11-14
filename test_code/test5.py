# -*- coding: utf-8 -*-
"""
Description : 探索如何学习加法 死记硬背个位数字相加


date：          2023/11/14
"""


class neurons:
    def __init__(self, path=[]):
        self.path = path
        self.next = 0  # 下一个待激活单元的序号 比如 1+1=2 在输入了1+1= 之后就是2
        self.activate = 0  # 激活强度 匹配的序列越多，强度越高

    def input(self, input_str):
        if input_str == self.path[self.next]:  # 序列匹配则强度+1 没有考虑时间参数，比较粗糙
            self.activate += 1
            self.next += 1


class brain():
    def __init__(self):
        self.neurons = []

    def learn(self, knowledges):
        # 分段学习 输入为字符串数组
        for knowledge in knowledges:
            self.neurons.append(neurons(knowledge))

    def test(self, question):
        # 回忆逻辑： 
        for c in question:
            for neuron in self.neurons:
                neuron.input(c)
        sorted_result = sorted(self.neurons, key=lambda n: n.activate, reverse=True)
        result = sorted_result[0]
        print(result.path[result.next])


def gen_knowledge():
    knowledges = []
    for i in range(10):
        for j in range(10):
            print(f"{i}+{j}={i + j}")
            knowledges.append([str(i), '+', str(j), '=', str(i + j)])
    return knowledges


def test():
    xiaoming = brain()

    xiaoming.learn(gen_knowledge())
    xiaoming.test(['6', '+', '9', '='])


if __name__ == '__main__':
    test()
