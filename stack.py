class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def printQueue(self, my_stack):
        if my_stack.top_item.next_node == None:
            print(my_stack.top_item.get_value())
            return True
        else:
            print(my_stack.top_item.get_value())
            my_stack.top_item = my_stack.top_item.get_next_node()
            return self.printQueue(my_stack)


# Defining an empty node stack
my_stack = Stack(6)


my_stack.push("node1")
my_stack.push("node2")
my_stack.push("node3")
my_stack.push("node10")
my_stack.push("node5")
my_stack.push("node6")

my_stack.push("node4")

my_stack.printQueue(my_stack)
