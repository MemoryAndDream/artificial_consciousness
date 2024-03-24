# -*- coding: utf-8 -*-
"""
Description : 大脑 负责记忆 情感
大脑本来应该是最复杂的器官，但是目前调整架构，先用最简单的模型。毕竟婴儿本来就比较简单
第一阶段：不需要做出什么动作，能哭，能笑就好了。心情和表情本能关联
参考前面的经验，简单用dict表示事件链接关系，加上疲劳机制，事件驱动
date：          2024/1/3
"""
from organs.organ import Organ


class Brain(Organ):
    def __init__(self, body=None, name='brain'):
        super().__init__(body, name)
        self.nerons = []
        self.output = []  # 输出信号

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

    def feel(self, feeling):
        # 接收其他器官的直接感触 比如饿，饱，痛

        pass
