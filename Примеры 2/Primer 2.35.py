from sympy import *
x=symbols('x')
print(limit(1/(sqrt(2*x**2+2*x-3)-sqrt(2*x**2-5*x-5)),x,-oo))
