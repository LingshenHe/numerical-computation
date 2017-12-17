# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:36:51 2017

@author: Lingsheng He
"""

import numpy as np
def f(x):
    return np.exp(-x**(2))
a=np.zeros(100)
b=np.zeros(100)
c=np.zeros(100)
d=np.zeros(100)
a[0]=(f(0)+f(0.8))/2
for i in range(1,3):
    a[i]=a[i-1]/2
    for j in range(2**(i-1)):
        a[i]+=f((j+0.5)*0.8/(2**(i-1)))*0.8/2**(i)
for i in range(3):
    b[i]=4*a[i+1]/3-a[i]/3
for i in range(2):
    c[i]=16*b[i+1]/15-b[i]/15
d[0]=64*c[1]/63-c[0]/63
i=4
while i>1:
    a[i]=a[i-1]/2
    for j in range(2**(i-1)):
        a[i]+=f((j+0.5)*0.8/(2**(i-1)))*0.8/2**(i)
    b[i-1]=4*a[i]/3-a[i-1]/3
    c[i-2]=16*b[i-1]/15-b[i-2]/15
    d[i-3]=64*c[i-2]/63-c[i-3]/63
    print(d[i-3],i)
    if abs(d[i-3]-d[i-4])<0.5*10**(-6):
        break
    i+=1
print('end')
    
