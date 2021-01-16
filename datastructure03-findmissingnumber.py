# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:29:53 2021

@author: deesaw
"""
import collections

def findnum(arr1,arr2):
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    for a,b in zip(arr1,arr2):
        if a!=b:
            return a
    return arr1[-1]
        


def findnum2(arr1,arr2):
    d=collections.defaultdict(int)
    for a in arr2:
        d[a]+=1
    print(d)
    for b in arr1:
        if d[b]==0:
            print(d)
            return b
        else:
            d[b]-=1
            
        
    
print(findnum2([1,5,6,6,9],[1,5,6,9]))