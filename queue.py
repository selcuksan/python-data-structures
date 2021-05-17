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


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0

    def printQueue(self, my_queue):
        if my_queue.head == my_queue.tail:
            print(my_queue.head.get_value())
            return True
        else:
            print(my_queue.head.get_value())
            my_queue.head = my_queue.head.get_next_node()
            return self.printQueue(my_queue)


my_queue = Queue(10)
my_queue.enqueue('node8')
my_queue.enqueue('node9')
my_queue.enqueue('node10')
my_queue.enqueue('node2')
my_queue.enqueue('node3')
my_queue.enqueue('node4')
my_queue.enqueue('node5')
my_queue.enqueue('node6')
my_queue.enqueue('node7')

my_queue.printQueue(my_queue)