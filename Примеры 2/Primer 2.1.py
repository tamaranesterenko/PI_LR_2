import sympy
n = sympy.symbols('n')
print(sympy.limit((6*n**2+1)/(7*n**2-3*n+9), n, sympy.oo))
