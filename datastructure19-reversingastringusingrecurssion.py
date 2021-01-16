# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:44:47 2021

@author: deesaw
"""


def reverse(s):
    
    # Base Case
    if len(s) <= 1:
        return s

    # Recursion
    print(1)
    return reverse(s[1:]) + s[0]
print(reverse('hello worldddddddddddddddddddddddddddddddddddddddddd'))