# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:03:17 2021

@author: deesaw
"""


import collections

def strcomp(string):
    stringc=collections.Counter(string)
    strfi=''
    l=len(string)
    if l==0:
        return ''
    if l==1:
        return string +'1'
    for a in string:
        if a not in strfi:
            strfi=strfi+a+str(stringc[a])
        
    return strfi
        
        

print(strcomp('AABBB'))