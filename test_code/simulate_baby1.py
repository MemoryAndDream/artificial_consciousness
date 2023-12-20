# -*- coding: utf-8 -*-
"""
Description : 模拟宝宝，初始状态没有捋清楚思路，所以只能说是模拟
"""


class Baby:
    def __init__(self):
        # 宝宝的自我，由他拥有的东西决定
        self.born()

    def born(self):
        self.name = ''
        self.memory = []
        self.mom = ''
        self.hungry = None  #

    def emotion(self):
        options = ['happy', 'sad', 'fear']

    def operation(self):
        options = ['cry', 'shout', 'speak', 'eat', 'sleep', 'think']

    def senses(self):
        options = ['listen', 'see']

    def status(self):
        options = ['hungry', 'sleepy', 'lonely']


def live():
    baby = Baby()
    for day in  range(365):
        baby.senses()
        baby.emotion()
        baby.operation()


'''
想想看要怎么养宝宝
首先，宝宝会饿，饿了的本能就是哭
哭了就要喂
宝宝能看见喂的人是谁
吃东西饱了本能就会高兴

'''

