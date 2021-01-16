# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:59:27 2021

@author: deesaw
"""


def largestcontinuoussum(arr):
    maxsum=currsum=arr[0]
    for a in arr[1:]:
        currsum=max(currsum+a,a)
        maxsum=max(currsum,maxsum)
        print(a,currsum,maxsum)
    return maxsum

print(largestcontinuoussum([90,99,90,90,99]))