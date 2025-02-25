# -*- coding: utf-8 -*-

# 音乐记忆系统，只记录1-7音符输入
# 目标：记忆一些简谱，后面听到一曲开头，就能哼出后续

class Node:
    def __init__(self,name):
        self.id=id(self)
        self.name=name
        print(self.id)
        self.ms = {} # 神经末梢
        self.st = {} # 树突


    def connect(self,next_id):
        if next_id not in self.ms:
            self.ms[next_id] = 0 # 统计链接次数
        self.ms[next_id] += 1



    def act(self):
        pass

class Link:
    def __init__(self):
        pass

def init():
    # 后面还是得数学化，不然hard code不完
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1m = Node('1m')
    n2m = Node('2m')
    n3m = Node('3m')
    n4m = Node('4m')

def input():



def main():
    pass


if __name__ == '__main__':
    main()



