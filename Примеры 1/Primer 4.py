from sympy import *
x = Symbol("X")
print(limit((5**x-5*7**x)/(4*5**x-3*7**x), x,oo))
print(limit((7*8**x+2*9**x)/(6*8**x-6*9**x), x, -oo))
print(limit(sqrt(x*(x+3))-sqrt(x**2+9), x, -oo))


