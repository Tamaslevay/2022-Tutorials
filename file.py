# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import sin


print("levay")

def f1(x):
    function = x**3
    return function

def f2(x):
    function = 3*x**2-2*x
    return function

def f3(x):
    function = sin(x)
    return function

input = [-5,-4,-3,-2,1,0,1,2,3,4,5]
output1 = []
output2 = []
output3 = []

for i in input:
    output1.append(f1(i))
    output2.append(f2(i))
    output3.append(f3(i))

print("my y-values")
print("y=x^3:", output1)
print("y=3x^2-2x", output2)
print("y=sin(x)", output3)

