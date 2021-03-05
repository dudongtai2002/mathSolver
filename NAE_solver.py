"""
General Template solver to solve nash equilibrium with 2 player
"""


import nashpy
import numpy as np
A = np.array([[3, 4, -1],[-2, -1, 2]])
B = -A     # zero-sum game
fvsc = nashpy.Game(A, B)
eqs = fvsc.support_enumeration()
print(*eqs)

# check gain table
"""
A\B
     3,-3   4,-4   -1,1
     -2,2   -1,1   2,-2
"""