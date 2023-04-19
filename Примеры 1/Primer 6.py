from sympy import *
x = Symbol("X")
print(solve(x**3-9*x**2+14*x))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 0, '-'))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 0, '+'))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 2, '-'))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 2, '+'))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 7, '-'))
print(limit(abs((x-2)*(x-7)/(x**3-9*x**2+14*x)), x, 7, '+'))


