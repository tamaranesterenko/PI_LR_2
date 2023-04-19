from sympy import *
n=symbols('n')
print(limit((3*2**n+2*4**n-3)/(4*2**n+3*4**n-2), n, oo))
