# -*- coding: utf-8 -*-
"""
Description : 模拟宝宝，初始状态没有捋清楚思路，所以只能说是模拟
"""


class baby:
    def __init__(self):
        # 宝宝的自我，由他拥有的东西决定
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
