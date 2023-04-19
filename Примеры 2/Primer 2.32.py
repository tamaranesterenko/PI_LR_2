from sympy import *
x=symbols('x')
print(limit((9-3*6**(6+x))/(5-5*6**(x+8)), x, oo))
