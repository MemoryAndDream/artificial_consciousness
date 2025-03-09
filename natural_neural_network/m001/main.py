# 1 不由自主发出声音，正好是妈妈
# 2 听到自己发出的妈妈声音
# 3 妈妈来了
# 。。。
# 4 最后妈妈来了会主动喊妈妈


# 三点模型测试
# 万事开头难，坚持难

# 初期的事件已经可以训练出具体神经网络了，但是问题是后续事件不好触发，还是应该定义一个神经元的整体，这样才能定位出输入输出


class Node:
    def __init__(self,name): # 为了方便研究，就用name当成id好了
        # self.id=id(self)#
        self.name=name
        self.id = name


    def init_connect(self, next_node,strength=100):
        link = Link(self.id,next_node.id, strength)
        return link

    def act(self):
        pass

class Link:
    def __init__(self,source_id,target_id,strength,active_at=0):
        self.source_id = source_id
        self.target_id = target_id
        self.strength = strength
        self.active_at = active_at

class Mind:
    def __init__(self):
        self.all_links = []
        self.all_nodes = []
        self.time_stamp = 0

    def add_node(self, node_name='') -> Node:
        node = Node(node_name)
        self.all_nodes.append(node)
        return node

    def init_connect(self,node1:Node, node2:Node):

        self.all_links.append(node1.init_connect(node2))


    def create_or_strenth_link(self, source, target, strength=1):
        find_link = False
        if isinstance(source,Node):
            source_id = source.id
            target_id = target.id
        else:
            source_id, target_id = source,target
        for link in self.all_links:
            if link.source_id == source_id and link.target_id == target_id:
                find_link = True
                link.strength = link.strength+1
        if not find_link:
            link = Link(source_id, target_id, strength)
            self.all_links.append(link)


    def timepass(self, target_id):
        # 计算这一时间发生的神经元活动
        # 先简化为当前只有一个target被激活
        for link in self.all_links:
            if link.active_at > self.time_stamp -3:
                self.create_or_strenth_link(link.source_id,target_id) # 这里其实要优化，越近的加强越大
        self.time_stamp += 1

    def get_node(self,node_name) -> Node:
        for node in self.all_nodes:
            if node.name == node_name:
                return node


def progress(baby_mind:Mind):
    eye1 = baby_mind.add_node('eye1')
    eye2 = baby_mind.add_node('eye2')
    eye3 = baby_mind.add_node('eye3')
    mouth1 = baby_mind.add_node('mouth1')
    mouth2 = baby_mind.add_node('mouth2')
    mouth3 = baby_mind.add_node('mouth3')
    ear1 = baby_mind.add_node('ear1')
    ear2 = baby_mind.add_node('ear2')
    ear3 = baby_mind.add_node('ear3')

    # 自然连接
    baby_mind.init_connect(eye1,eye2)
    baby_mind.init_connect(eye2, eye3)
    baby_mind.init_connect(mouth1, mouth2)
    baby_mind.init_connect(mouth2, mouth3)
    baby_mind.init_connect(ear1, ear2)
    baby_mind.init_connect(ear2, ear3)

    # 训练事件
    # 不由自主喊妈妈，激活顺序： mouth1-2,2-3
    baby_mind.create_or_strenth_link(mouth1, mouth2)


    baby_mind.create_or_strenth_link(mouth2, mouth3)
    
    baby_mind.timepass(mouth3.id)
    # 然后耳朵收到信号 ear1-2,2-3
    baby_mind.create_or_strenth_link(ear1,ear2)
    baby_mind.timepass(ear2.id)
    baby_mind.create_or_strenth_link(ear2,ear3)
    baby_mind.timepass(ear3.id)

    # 这时候如果妈妈来了 eye1-2,2-3
    baby_mind.create_or_strenth_link(eye1,eye2)
    baby_mind.timepass(eye2.id)
    baby_mind.create_or_strenth_link(eye2,eye3)
    baby_mind.timepass(eye3.id)




def detect_links(baby_mind:Mind):
    for link in baby_mind.all_links:
        print(link.source_id, link.target_id, link.strength)

def test_event1(baby_mind: Mind):
    # 测试事件 通过对神经冲动的追踪反映思维
    # 事件： 妈妈出现了
    eye1 = baby_mind.get_node('eye1')
    eye1.act()

def test_mind(baby_mind:Mind):
    # 测试回忆 其实也是事件
    # 事件，听到妈妈这个词
    pass


def main():
    baby_mind = Mind()
    progress(baby_mind)
    # test_event1(baby_mind)

    detect_links(baby_mind)
    # 测试结果： eye1 会引发mouth3 和ear3的输出
    # ear1 会引发mouth3
    # 没有引发eye3的 可能是因为没有进一步学习与回忆，或者说，看到妈妈能喊妈妈，但是听到则还想不到，存在先后顺序问题，这就是顺序记忆，看到妈妈在说话之后

    # 要进一步学习需要先看到妈妈，然后回忆引发动作








if __name__ == '__main__':
    main()