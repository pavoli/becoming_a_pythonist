# coding: utf-8
__author__ = 'polly'


class Stack(object):

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return not self.lst

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if not self.is_empty():
            print self.lst.pop()
        else:
            return []

    def __str__(self):
        return str(self.lst)


class Queue(object):
    def __init__(self):
        self.lst = []

    def is_empty(self):
        return not self.lst

    def enqueue(self, item):
        self.lst.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            print self.lst.pop()
        else:
            return []

    def __str__(self):
        return str(self.lst)

'''
example for Stack()
'''
stack = Stack()
print stack.is_empty()      # True
stack.push(10)
stack.push(30)
stack.push(0)
stack.push(1)
print stack.is_empty()      # False
print stack                 # [10, 30, 0, 1]
stack.pop()                 # 1
print stack                 # [10, 30, 0]

'''
example for Queue()
'''
queue = Queue()
print queue.is_empty()      # True
queue.enqueue('1')
queue.enqueue('44')
print queue                 # ['44', '1']
queue.dequeue()             # 1
print queue                 # ['44']
