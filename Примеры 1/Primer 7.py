from sympy import *
x = Symbol("X")
k = limit((1+5*x)/(3+x)/x, x, oo)
print(k)
b = limit((1+5*x)/(3+x)-k*x, x, oo)
print(b)
print(solve(3+x))
print(limit((1+5*x)/(3+x), x, -3, '-'))
print(limit((1+5*x)/(3+x), x, -3, '+'))

