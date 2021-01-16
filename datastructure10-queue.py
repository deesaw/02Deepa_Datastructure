# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:36:49 2021

@author: deesaw
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def printq(self):
        print(self.items[: :-1])

q = Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.printq()
print(q.dequeue())