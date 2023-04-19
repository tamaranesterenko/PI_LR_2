import sympy
n = sympy.symbols('n')
print(sympy.limit((-3*n**3+4*n**2-8*n-6)/(4*n**2+2*n), n, sympy.oo))
