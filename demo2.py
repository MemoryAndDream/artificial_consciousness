# -*- coding: utf-8 -*-
"""
Description : 记忆模拟实验
date：          2023/8/18
"""

class route:
    def __init__(self,start,end):
        self.activate_count = 0
        self.last_activate_at = 0
        self.start = start
        self.end = end

    def active(self):
        if self.cal():
            self.activate_count += 1


    def cal(self):
        return True


class concept:
    def __init__(self,id):
        self.id =id

# 记忆abcd，0为起始点
def mod1():
    concept1 = concept('0')
    concept2 = concept('a')
    concept3 = concept('b')
    concept4 = concept('c')
    route1 = route(concept1.id,concept2.id)



if __name__ == '__main__':
    mod1()