from sympy import *
x=symbols('x')
print(limit((x**2+4*x+3)/(x**2+8*x+15), x, oo))
