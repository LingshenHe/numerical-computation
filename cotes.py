# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:24:02 2017

@author: Lingsheng He
"""
import numpy as np
def f(x):
    return 1/((x**(3)+1)**(0.5))
n=1
s1=1
while n>=1:
    s=0
    for i in range(n):
        x0=i/n
        s+=1/(90*n)*(7*f(x0)+32*f(x0+1/(4*n))+12*f(x0+2/(4*n))+32*f(x0+3/(4*n))+7*f(x0+1/n))
    if abs(s-s1)/63<0.5*10**(-6):
        break
    s1=s
print(s)
