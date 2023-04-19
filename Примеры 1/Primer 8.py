from sympy import *
import math as m
x = Symbol("X")
print(limit(1/factorial(x)/(1/factorial(x+1)), x, oo))
