from sympy import *
n=symbols('n')
print(limit(((8*n-5)/(8*n-1))**(9*n-5), n, oo))
