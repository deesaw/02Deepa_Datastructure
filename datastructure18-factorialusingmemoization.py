# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:01:50 2021

@author: deesaw
"""


factorial_memo = {}

def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]

print(factorial(15))

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
    
def factorial(k):
    
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

factorial = Memoize(factorial)

print(factorial(1))
print(factorial(5))
print(factorial(15))
print(factorial.memo)