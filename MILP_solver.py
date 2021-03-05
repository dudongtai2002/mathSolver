# With Gurobi+free academic license>=9.0.2 Cvxpy>=1.0.25
# Note python install gurobi (not included in requirement.txt):
# pip3 install -i https://pypi.gurobi.com gurobipy
import cvxpy as cp

# Create two scalar optimization variables.
x = cp.Variable()
y = cp.Variable()

# Create constraints.
constraints = [0.2*x + 0.5*y <= 90,
              4*x + 2*y <= 800,
              x >=0,
              y >=0]

# Form objective.
obj = cp.Maximize(x*30 + y*20)

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)

