# -*- coding: utf-8 -*-
"""
Description :
date：          2023/7/5
"""

neuron = 123




class Neuron:
    # 连接强度 = 长期连接强度 * 疲劳修正 * 短期激活修正
    # cs = lcs * tm * sac
    def __init__(self, path):
        self.created_at = 0
        self.lcs = 1 # 长期连接强度 暂定 f(x) = x
        self.tm = 1 # 疲劳修正 暂定 f(x) =
        self.sac = 1 # 短期激活修正 暂定 f(x) =
        self.path = path

    def cal(self):
        self.cs = self.lcs * self.tm * self.sac
        return self.cs

    def activate(self):
        pass



class Mind():
    def __init__(self):
        self.neurons = []

    def remember(self, inputs):
        t = 0
        full_path = ''
        for s in inputs:
            print(s)
            full_path = full_path+s
            new_neuron = Neuron(full_path)

            # 联想及遗忘
            self.associate(new_neuron)

            self.neurons.append(new_neuron)
            t+=1

        for neuron in self.neurons:
            print(neuron.path,neuron.cal())

    def associate(self,path):
        # 联想 比对路径相似性
        for neuron in self.neurons:
            old_path = neuron.path

            print(old_path)

        pass

    def forget(self):
        pass

    def sing(self,):
        pass

def main():
    new_one = Mind()
    xiaoxinxin = '01155665'
    new_one.remember(xiaoxinxin)
    new_one.sing()


if __name__ == '__main__':
    main()







