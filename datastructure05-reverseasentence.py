# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:49:56 2021

@author: deesaw
"""


def revasentence(sente):
    a=' '.join(reversed(sente.split()))
    return a
def revasentence2(sente):
    a=' '.join(sente.split()[: :-1])
    return a

def revasentence3(sente):
    b=[]
    for a in sente.split():
        b.append(a)
    return ' '.join(b[ : :-1])
        
        

print(revasentence3("This is a test sente   "))