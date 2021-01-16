# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:28:13 2021

@author: deesaw
"""


class Stack:
    
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def stackp(self):
        print(self.items)

s=Stack()
print(s.isEmpty())
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
s.push('6')
s.stackp()
s.pop()
print(s.size())