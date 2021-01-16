# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:32:08 2021

@author: deesaw
"""


def fib_rec(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursion
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(20))

# Instantiate Cache information
n = 100
cache = [None] * (n + 1)

def fib_dyn(n):
    
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Check cache
    if cache[n] != None:
        return cache[n]
    
    # Keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]


print(fib_dyn(20))

def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):

        a, b = b, a + b
        
    return a
print(fib_iter(10))