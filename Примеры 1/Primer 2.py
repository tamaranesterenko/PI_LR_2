from sympy import *
x = Symbol("X")
print(limit(sin(x)/x, x, 0))
print(limit((1+x)**(1/x), x, 0))
print(limit((1+1/x)**x, x, oo))
