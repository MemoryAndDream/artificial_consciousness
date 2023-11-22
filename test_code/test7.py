# -*- coding: utf-8 -*-
'''
想想人类是先学会数数的
这些测试的目的是验证记忆模型，而不是直接出结果


数数逻辑： 物体抽象为个，然后x个
这里学习字母的数数

人类视觉的一些抽象可以直接当做已知的抽象概念联系
比如空格分隔出的都是一个词

感觉还是要建立完整brain模型，再研究怎么训练
'''


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
    for i in range(ord('a'), ord('z') + 1):  # 实际人类通过视觉提取特征，这里没有视觉，所以只能先学习字母的抽象
        for j in range(10):
            print(chr(i) * j, f'{j}个{chr(i)}')
            knowledges.append([chr(i)] * j + [j, '个', chr(i)])  # 可能还需要学习本身的概念

    return knowledges


def test():
    xiaoming = brain()

    xiaoming.learn(gen_knowledge())
    xiaoming.test(['a'])
    xiaoming.test(['a'])
    xiaoming.test(['a'])
    xiaoming.test(['a'])
    xiaoming.test(['a'])
    xiaoming.test(['b'])
    xiaoming.test(['b'])  # 缺少遗忘逻辑，导致不能重置


if __name__ == '__main__':
    test()
