import math
from sympy import *
x = Symbol("X")
print(limit(x**x/factorial(x)/((x+1)**(x+1)/factorial(x+1)), x, oo))
