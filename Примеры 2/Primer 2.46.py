from sympy import *
x=symbols('x')
print(limit(cos(x**5)**((7+2*x**5)/x**10),x,0))
