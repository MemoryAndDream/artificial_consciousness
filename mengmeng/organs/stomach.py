# -*- coding: utf-8 -*-
"""
Description :
date：          2023/12/22
"""
from organs.organ import Organ
class Stomach(Organ):
    def __init__(self, body=None, name='stomach'):
        super().__init__(body,name)


    def handle(self, event):
        if event.name == 'time_pass':
            self.body.status.hp -= 1

    def eat(self, food):
        self.body.status.hp += 1