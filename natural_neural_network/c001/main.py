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
    def __init__(self, connected_neuron, init_weight=1):
        self.connected_neuron = connected_neuron
        self.weight = init_weight

class Neuron:
    def __init__(self, name=''):
        self.synapses = []
        self.name = name

    def connect(self, neuron, weight=1):
        synapse = Synapse(neuron, weight)
        self.synapses.append(synapse)

    def activate(self):
        # 神经元激活
        pass

    def stimulate(self):
        # 刺激神经元
        pass


# 从底层一步步往上定义 定义方式：底层为l1o1

def born():
    l1o1 = Neuron('eat')
    l1o2 = Neuron('see')
    l1o3 = Neuron('run')

    l2o1 = Neuron()
    l2o1.connect(l1o1,2)
    l2o1.connect(l1o2)

    l2o2 = Neuron()
    l2o2.connect(l1o1)
    l2o2.connect(l1o2,2)
    l2o2.connect(l1o3)

    l2o3 = Neuron()
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




if __name__ == '__main__':
    main()