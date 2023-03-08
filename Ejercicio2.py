from pulp import *

problema = LpProblem("Ejercicio_2", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

problema += 5*x1 + 10*x2
problema += 3*x1 + 1*x2 >= 40
problema += x1 + x2 >= 20
problema += 5*x1 + 3*x2 >= 90

problema.solve()

print("El valor optimo se encuentra en x1 = {}, x2 = {}".format(x1.varValue,x2.varValue))
print("Con un minimo de Z = {}".format((5*x1.varValue + 10*x2.varValue)))