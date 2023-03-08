from pulp import *

problema = LpProblem("Ejercicio_1", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)

problema += 3*x1 + 4*x2 + 2*x3
problema += x1 + x2 + x3 >= 15
problema += x2 + x3 >= 10

problema.solve()

print("El valor optimo se encuentra en x1 = {}, x2 = {}, x3 = {}".format(x1.varValue,x2.varValue,x3.varValue))
print("Con un minimo de Z = {}".format((3*x1.varValue + 4*x2.varValue + 2*x3.varValue)))