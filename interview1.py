# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:02:09 2021

@author: deesaw
"""

list = ['a', 'b', 'c', 'd', 'e']
print (list[10:])
def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    return x * y

print(product(3, 3))
print((var for var in range(10, 20)))
# Example - enumerate function 
alist = ["apple","mango", "orange"] 
astr = "banana"
  
# Let's set the enumerate objects 
list_obj = enumerate(alist) 
str_obj = enumerate(astr) 
  
print("list_obj type:", type(list_obj))
print("str_obj type:", type(str_obj))

print((enumerate(alist)) )  
# Move the starting index to two from zero
#print(list(enumerate(astr, 2)))
x = 9
def fn(): 
    y = 3
    z = y + x
    # Calling the globals() method
    z = globals()['x'] = z
    return z
       
# Test Code     
ret = fn() 
print(x)

class Test: 
    aclass = 'programming' # A class variable 
    def __init__(self, ainst): 
        self.ainst = ainst # An instance variable 
  
# Objects of CSStudent class 
test1 = Test(1) 
test2 = Test(2) 
  
print(test1.aclass)
print(test2.aclass)
print(test1.ainst)
print(test2.ainst)
test2.aclass='1111111111111'
print(test1.aclass)
print(test2.aclass)
print(test1.ainst)
print(test2.ainst)
# A class variable is also accessible using the class name
Test.aclass='1111111111111'
print(Test.aclass)

print(test1.aclass)
print(test2.aclass)
print(test1.ainst)
print(test2.ainst)

a=1
b=a
print(a,b)
a=2
print(a,b)

weekdays = ['sun','mon','tue','wed','thu','fri']
print(weekdays[0::2],weekdays[1::2])
listAsDict = dict(zip(weekdays[0::2], weekdays[1::2]))
print(listAsDict)
import re
sentence = 'Learn Python Programming'
test = re.match(r'(.*) (.*?) (.*)', sentence)
print(test.group())