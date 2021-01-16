# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:54:13 2021

@author: deesaw
"""


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def printdeque(self):
        print(self.items)

d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.size())
print(d.size())
print(d.printdeque())
print(d.removeFront() + ' ' +  d.removeRear())
