from sympy import *
n=symbols('n')
print(limit((4*5**n-5*6**n)/(4*6**n+5**n), n, oo))
