from pulp import *

problema = LpProblem("Ejercicio_2", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)

problema += 7*x1 + 2*x2 + 5*x3 + 4*x4
problema += 2*x1 + 4*x2 + 7*x3 + x4 >= 5
problema += 8*x1 + 4*x2 + 6*x3 + 4*x4 >= 8
problema += 3*x1 + 8*x2 + 1*x3 + 4*x4 >= 4

problema.solve()

print("El valor optimo se encuentra en x1 = {}, x2 = {}, x3 = {}, x4 = {}".format(x1.varValue,x2.varValue,x3.varValue,x4.varValue))
print("Con un minimo de Z = {}".format((7*x1.varValue + 2*x2.varValue + 5*x3.varValue + 4*x4.varValue)))