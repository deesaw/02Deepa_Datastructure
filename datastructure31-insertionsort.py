# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:50:51 2021

@author: deesaw
"""


def insertion_sort(arr):
    for i in range(1,len(arr)):
        position=i
        currentvalue=arr[i]
        
        while position >0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=currentvalue
arr=[3,5,2,7,6,8,12,40,21]
insertion_sort(arr)
print(arr)