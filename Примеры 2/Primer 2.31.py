from sympy import *
x=symbols('x')
print(limit((3*x+9)/(2*cos(2*x)+6*x-3), x, oo))
