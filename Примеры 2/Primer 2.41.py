from sympy import *
x=symbols('x')
print(limit((7*x+sin(2*x))/(sin(4*x)+asin(7*x)),x,0))
