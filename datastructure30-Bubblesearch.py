# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:47:36 2021

@author: deesaw
"""


def bubble_sort(arr):
    # For every element (arranged backwards)
    length=len(arr)-1
    for n in range(length):
        for k in range(length-n):
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1] = arr[k+1],arr[k]
arr = [3,2,13,4]
bubble_sort(arr)
print(arr)
def bubble_sort(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        print(n)
        for k in range(n):
            print(k,end=' ')
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1] = arr[k+1],arr[k]
arr = [3,2,13,4,6,5,7,8,1,20]
bubble_sort(arr)
print(arr)