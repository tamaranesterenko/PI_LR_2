from sympy import *
x=symbols('x')
print(limit(x*(sqrt(5*x**2+6)-sqrt(5*x**2-6)),x,-oo))
