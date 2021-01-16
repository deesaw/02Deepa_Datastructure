# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:13:10 2021

@author: deesaw
"""


def selection_sort(arr):
    
    # For every slot in array
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax=0 

        for location in range(1,fillslot+1):
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location

        arr[fillslot],arr[positionOfMax]= arr[positionOfMax], arr[fillslot] 

arr = [3,5,2,7,6,8,12,40,21]
selection_sort(arr)
print(arr)
