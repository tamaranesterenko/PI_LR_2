from sympy import *
import math as m
import numpy
from numpy import inf
n=symbols('n')
print(limit((7-n+n**2)/(3*n-6)-(2-5*n+n**2)/(3*n+8),n,inf))
