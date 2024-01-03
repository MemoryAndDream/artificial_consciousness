# -*- coding: utf-8 -*-
"""
Description : 事件驱动思考和活动，时间流逝也是一种时间
date：          2023/12/31
"""
class Event:
    def __init__(self, name=''):
        self.name = name

class TimePassEvent(Event):
    def __init__(self):
        super().__init__('time_pass')

class SadEvent(Event):
    def __init__(self):
        super().__init__('cry')


