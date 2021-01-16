# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:49:38 2021

@author: deesaw
"""


class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c