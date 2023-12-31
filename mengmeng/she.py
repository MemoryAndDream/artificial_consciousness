# -*- coding: utf-8 -*-
"""
Description :
date：          2023/12/22
"""


class Body:
    def __init__(self):
        self.status = {}
        self.create_body()



    def create_body(self):
        from organs.stomach import Stomach
        self.stomach = Stomach(self)




class MengMeng:
    def __init__(self):
        self.body = Body()

    def live(self):
        # As time goes by, she lives
        self.get_input()
        self.do_something()
        self.refresh_status()



    def get_input(self):
        pass


    def do_something(self):
        # eat
        event = {}
        self.body.stomach.handle(event)

    def refresh_status(self):
        pass


if __name__ == '__main__':
    meng_meng = MengMeng()
    meng_meng.live()
    print(meng_meng.body.status)