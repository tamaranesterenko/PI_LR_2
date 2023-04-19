from sympy import *
x=symbols('x')
print(limit(((7*x**4+3)/(7*x**4-3))**(3*x**4-6),x,oo))
