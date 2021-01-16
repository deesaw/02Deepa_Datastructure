# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:59:11 2021

@author: deesaw
"""


def fact(n):
    '''
    Returns factorial of n (n!).
    Note use of recursion
    '''
    # BASE CASE!
    if n == 0:
        return 1
    
    # Recursion!
    else:
        print(f"{n}*fact({n-1})")
        return n * fact(n-1)
    
print(fact(5))