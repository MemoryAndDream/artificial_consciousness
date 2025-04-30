# 多余链接模型测试，目标是可以实现重复单词的记忆
# 本来是打算简谱的，但是搞简谱有点麻烦，所以用单词记忆好像也行， 比如 good apple
# 学习过程为：看一个'apple'，以及apple这个单词一个个字母输入
# 期望结果：按顺序输出apple


# 由于是带抽象的，所以不能按阈值激活，而是只能作比较器

class Node:
    def __init__(self,name,depth=0): # id 必须为唯一
        self.id=id(self)#
        self.name=name
        # self.id = name
        self.active_level = 0
        self.link_dict = {}
        self.depth = depth


    def is_blank_node(self):
        return False if self.link_dict else True

    def init_connect(self, next_node, strength=100):
        link = Link(self.id,next_node.id, strength)
        self.link_dict[next_node] = link
        return link

    def act(self): # 激活下级node，将本次链接强度加入
        for next_node, link in self.link_dict.items():
            next_node.active_level += link.strength

    def has_empty_sub_node(self):
        for sub_node in self.link_dict:
            if sub_node.is_blank_node():
                return sub_node
        return None






class Link:
    def __init__(self,source_id,target_id,strength,active_at=0):
        self.source_id = source_id
        self.target_id = target_id
        self.strength = strength
        self.active_at = active_at



class Mind:
    def __init__(self):
        self.all_links = []
        self.all_nodes = {}
        self.time_stamp = 0


    def add_node(self, node_name='') -> Node:
        node = Node(node_name)
        self.all_nodes[node.id]=node
        return node

    def init_connect(self,node1:Node, node2:Node):
        self.all_links.append(node1.init_connect(node2))

    def add_init_node(self, node_name='') -> Node:
        node = self.add_node(node_name)
        self.init_sub_nodes(node)
        return node

    def init_sub_nodes(self, node: Node):
        # 创建初始化的2层节点
        level_1_node_name = node.name + '_1'
        level_2_node_name = node.name + '_2'
        node_1 = self.add_node(level_1_node_name)
        node_2 = self.add_node(level_2_node_name)
        self.init_connect(node, node_1)
        self.init_connect(node_1, node_2)

    def activate_node(self, init_node: Node):
        # init node被视为接收输入的node,所以处理事件只需要激活这一类node即可
        init_node.act() # 这里根据链接激活下游节点

        # 产生新的空白节点和基于附近时间激活的新链接
        # 需要迭代计算
        if not init_node.has_empty_sub_node(): # 需要注意不要无限拉长空白节点链的长度
            new_empty_node = self.add_node()
            init_node.init_connect(new_empty_node)



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
                link.active_at = self.time_stamp
        if not find_link:
            link = Link(source_id, target_id, strength)
            self.all_links.append(link)


    def timepass(self, target_id):
        # 计算这一时间发生的神经元活动
        # 先简化为当前只有一个target被激活
        for link in self.all_links:
            if link.active_at > self.time_stamp - 3:
                self.create_or_strenth_link(link.source_id,target_id) # 这里其实要优化，越近的加强越大
        self.time_stamp += 1

    def get_node_by_name(self,node_name) -> Node: # 中间过程实际上都应该只用id，最后print再用name
        for node_id in self.all_nodes:
            if self.all_nodes[node_id].name == node_name:
                return self.all_nodes[node_id]


def progress(baby_mind:Mind):
    apple = baby_mind.add_init_node('apple')
    a = baby_mind.add_init_node('a')
    p = baby_mind.add_init_node('p')
    l = baby_mind.add_init_node('l')
    e = baby_mind.add_init_node('e')


    # 训练事件 看见apple，然后依次输入 a p p l e

    for retry in range(10):
        baby_mind.activate_node(apple)
        baby_mind.activate_node(a)
        baby_mind.activate_node(p)
        baby_mind.activate_node(p)
        baby_mind.activate_node(l)
        baby_mind.activate_node(e)



def detect_links(baby_mind:Mind):
    for link in baby_mind.all_links:
        print(link.source_id, link.target_id, link.strength)


def test_apple(baby_mind:Mind):
    # 事件， 看到苹果
    print('event start')








def main():
    baby_mind = Mind()
    progress(baby_mind)


    detect_links(baby_mind)










if __name__ == '__main__':
    main()