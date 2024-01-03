# -*- coding: utf-8 -*-
"""
Description : 大脑 负责记忆 情感
大脑本来应该是最复杂的器官，但是目前调整架构，先用最简单的模型。毕竟婴儿本来就比较简单


date：          2024/1/3
"""
from organs.organ import Organ
class Brain(Organ):
    def __init__(self, body=None, name='brain'):
        super().__init__(body,name)
        self.nerons = []
        self.output = [] # 输出信号


    def handle(self, event):
        if event.name == 'time_pass':
            self.think()
        elif event.name == 'see':
            self.see()
        elif event.name == 'hear':
            self.hear()

    def think(self):
        pass


    def see(self):
        pass

    def hear(self):
        pass