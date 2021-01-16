# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:26:10 2021

@author: deesaw
"""
a=[1,2,9,8,99]
def sum(lista,sums):
  sums=int(sums)
  sumdict={}
  for i in lista:
    if ((sums-i) in lista):
      if i not in sumdict and (sums-i) not in sumdict:
        sumdict[i]=sums-i
        print(f'{i} and {sums-i} add upto {sums}')

sum(a,10)

def sumof2(arr,summ):
    dicsum={}
    for a in arr:
        b=summ-int(a)
        if b in arr:
            if a not in dicsum and b not in dicsum:
                dicsum[a]=b
    return dicsum
aa=sumof2(a,10)
print(aa)