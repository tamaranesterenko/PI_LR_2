from sympy import *
x = Symbol("X")
print(limit(1/x, x, 0, '-'))
print(limit((2**x-1)/(x**2-3*x), x, 3, '+'))
print(limit((2**x-1)/(x**2-3*x), x, 3, '-'))

