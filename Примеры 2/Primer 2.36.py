from sympy import *
x=symbols('x')
print(limit((sqrt(x**2+1)-sqrt(x**2+5))*atan(3*x**4-1), x, oo))
