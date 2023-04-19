from sympy import *
x=symbols('x')
print(limit((1-cos(7/x))/(ln(1+6/x)*(exp(4/x)-1)),x,oo))
