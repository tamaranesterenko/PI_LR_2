from sympy import *
n=symbols('n')
print(limit(((3**n-1)/(3**n+3))**(3**n-7), n, oo))
