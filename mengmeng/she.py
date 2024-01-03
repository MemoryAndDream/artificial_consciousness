# -*- coding: utf-8 -*-
"""
Description : 组装模块
date：          2023/12/22
"""

from event import *

class Status():
    def __init__(self):
        self.hp = 100  # 饥饿值
        self.happy = 50  # 心情


class Body:
    def __init__(self):
        self.create_body()
        self.status = Status()


    def create_body(self):
        from organs.stomach import Stomach
        self.stomach = Stomach(self)




class MengMeng:
    def __init__(self):
        self.body = Body()
        self.events = []

    def live(self, events=[]):
        # As time goes by, she lives
        self.get_input(events)
        self.do_something()
        self.refresh_status()



    def get_input(self,events):
        # 接受外来的所有事件
        self.events.extend(events)


    def do_something(self):
        # eat
        for event in self.events:
            self.body.stomach.handle(event)

        self.events = []

    def refresh_status(self):
        if self.body.status.hp < 50:
            self.body.status.happy -= 1
        if self.body.status.happy<50:
            self.events.append(SadEvent())


if __name__ == '__main__':
    import pickle,os
    cache = 'mengmeng.plk'
    if os.path.exists(cache):
        with open(cache, 'rb') as r:
            meng_meng = pickle.load(r)
    else:
        meng_meng = MengMeng() #
    for i in range(10):
        meng_meng.live([TimePassEvent()])
        print(meng_meng.body.status.hp)
    with open(cache,'wb') as f:
        pickle.dump(meng_meng, f)

