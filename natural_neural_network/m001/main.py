# 1 不由自主发出声音，正好是妈妈
# 2 听到自己发出的妈妈声音
# 3 妈妈来了
# 。。。
# 4 最后妈妈来了会主动喊妈妈


# 三点模型测试
# 万事开头难，坚持难

GLOBAL_TIMESTAMP = 0
ALL_LINKS = []


class Node:
    def __init__(self,name):
        self.id=id(self)
        self.name=name
        print(self.id)
        self.ms = {} # 神经末梢


    def connect(self,next_id,strength=1):
        if next_id not in self.ms:
            self.ms[next_id] = 0 # 统计链接次数
        self.ms[next_id] += strength

    def act(self):
        pass

class Link:
    def __init__(self,source,target):
        self.source = source
        self.target = target

def progress():
    global GLOBAL_TIMESTAMP

    eye1 = Node('eye1')
    eye2 = Node('eye2')
    eye3 = Node('eye3')
    mouth1 = Node('mouth1')
    mouth2 = Node('mouth2')
    mouth3 = Node('mouth3')
    ear1 = Node('ear1')
    ear2 = Node('ear2')
    ear3 = Node('ear3')

    # 自然连接
    eye1.connect(eye2,100)
    eye2.connect(eye3,100)
    mouth1.connect(mouth2,100)
    mouth2.connect(mouth3,100)
    ear1.connect(ear2,100)
    ear2.connect(ear3,100)

    # 训练事件
    # 不由自主喊妈妈，激活顺序： mouth1-2,2-3
    mouth1.connect(mouth2)
    GLOBAL_TIMESTAMP+=1
    mouth2.connect(mouth3)
    GLOBAL_TIMESTAMP+=1
    # 然后耳朵收到信号 ear1-2,2-3
    ear1.connect(ear2)
    GLOBAL_TIMESTAMP+=1
    ear2.connect(ear3)
    GLOBAL_TIMESTAMP+=1

    # 这时候如果妈妈来了 eye1-2,2-3
    eye1.connect(eye2)
    GLOBAL_TIMESTAMP += 1
    eye2.connect(eye3)
    GLOBAL_TIMESTAMP += 1

    # 在这个过程中如何根据时间先后加强连接
    # 逻辑： 最近激活的前几个神经元会连接到本次的目标神经元， 强度根据时间




def main():
    pass




if __name__ == '__main__':
    main()