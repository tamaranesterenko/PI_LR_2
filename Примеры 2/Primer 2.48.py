from sympy import *
x=symbols('x')
print(limit(9*(1-x**(1/7))/(x**(1/8)-1), x, 1))
