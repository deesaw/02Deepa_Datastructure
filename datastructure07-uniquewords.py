# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:16:46 2021

@author: deesaw
"""


def uniquestr(string):
    return len(set(string))==len(string)

print(uniquestr('abcde'))