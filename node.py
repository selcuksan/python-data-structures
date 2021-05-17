class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

    def get_link_node(self):
        return self.link_node

    def get_value(self):
        return self.value


node1 = Node("node1")
node2 = Node("node3")
node3 = Node("node2")

node1.set_link_node(node2)
node2.set_link_node(node3)


def printNodes(node):
    if node == None:
        print('node yok')
        return 1
    elif node.get_link_node() == None:
        print(node.get_value())
        return 1
    else:
        print(node.get_value())
        printNodes(node.get_link_node())


printNodes(node1)
