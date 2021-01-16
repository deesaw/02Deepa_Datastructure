# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:17:09 2021

@author: deesaw
"""


def merge_sort(arr):
    
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        #print(lefthalf,righthalf,len(lefthalf),len(righthalf))
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
        print("::::::::::::::::::::::",str(arr))
arr = [3,2,5,4,7,6,8,9,1]
merge_sort(arr)
print(arr)