# -*- coding: utf-8 -*-
'''
单眼虫（c001）：
1个眼点
1个痛觉感受器
1个食物感受器
1个逃跑器官
神经网络结构：
眼点 痛觉感受器
  神经网络
  逃跑器官
环境：
眼点有刺激时容易出现痛觉
期望行为：
眼点有刺激时跑路

食物 眼  痛
| X | X |
o   o   o
| X | X |
o(吃)o  o(逃跑)



实验：
食 眼 食 眼 痛
痛 眼 痛 眼 食物
食物 食物 食物 食物 眼 痛 眼 痛

'''

class Synapse:
    def __init__(self, from_neuron, to_neuron, init_weight=1): # from to 是神经冲动传导方向 连接是从源头(高层)连接底层
        self.from_neuron = from_neuron
        self.to_neuron = to_neuron
        self.weight = init_weight

class Neuron:
    def __init__(self, name=''):
        self.after_synapses = []
        self.forward_synapses = []
        self.name = name

    def connect(self, neuron, weight=1): # after 是下游神经元 forward是上游 感觉有问题啊
        synapse = Synapse(self, neuron, weight)
        self.after_synapses.append(synapse)
        neuron.forward_synapses.append(synapse)

    def activate(self):
        # 神经元激活 1 根据刺激强化下游树突 2 刺激下层神经元
        for sy in self.after_synapses:
            sy.weight = sy.weight*1.5
            all_sys = sy.from_neuron.forward_synapses
            for sy in all_sys:
                sy.weight = sy.weight*0.9



    def stimulate(self):
        # 刺激神经元
        pass

    def print_synapses(self):
        # print('sy name',self.name)
        for sy in self.forward_synapses:
            print(sy.from_neuron.name,' to ', sy.to_neuron.name, sy.weight)
        for sy in self.after_synapses:
            print(sy.from_neuron.name,' to ', sy.to_neuron.name, sy.weight)

# 从底层一步步往上定义 定义方式：底层为l1o1

def born():
    l1o1 = Neuron('eat')
    l1o2 = Neuron('see')
    l1o3 = Neuron('run')

    l2o1 = Neuron('l2o1')
    l2o1.connect(l1o1,2)
    l2o1.connect(l1o2)

    l2o2 = Neuron('l2o2')
    l2o2.connect(l1o1)
    l2o2.connect(l1o2,2)
    l2o2.connect(l1o3)

    l2o3 = Neuron('l2o3')
    l2o3.connect(l1o2)
    l2o3.connect(l1o3,2)

    l3o1 = Neuron('mouth')
    l3o1.connect(l2o1,2)
    l3o1.connect(l2o2)


    l3o2 = Neuron('eye')
    l3o2.connect(l2o1)
    l3o2.connect(l2o2,2)
    l3o2.connect(l2o3)

    l3o3 = Neuron('tail')
    l3o3.connect(l2o2)
    l3o3.connect(l2o3,2)

    # test1  食 眼 食 眼 痛
    l3o1.activate()
    l3o2.activate()
    l3o1.activate()
    l3o2.activate()
    l3o1.activate()
    l3o2.activate()
    l3o1.activate()
    l3o2.activate()
    l3o3.activate()

    l2o1.print_synapses()
    l2o2.print_synapses()
    l2o3.print_synapses()





if __name__ == '__main__':
    born() # 1只有走完全流程才有共同作用部分，单层是没有用的
    # 似乎吃和痛没有构成互斥，完全是在独立加强，的确符合自觉