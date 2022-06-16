from math import cos
from dichotomy import dichotomy_method

from lagrange import lagrange

f = lambda x: x**3 - 5*x**2 + 4*cos(x) + 0.092
h = 0.1
nodes = [[-1, f(-1)]]
print('Table of nodes:')
print(f'i = 0\tx = {nodes[0][0]:.1f}\ty = {nodes[0][1]:.6f}')
for i in range(1, 10):
    x = nodes[0][0] + i * h
    y = f(x)
    nodes.append([x, y])
    print(f'i = {i}\tx = {x:.1f}\ty = {y:.6f}')

Lx = lagrange(f, nodes)
a, b = -1, 0
eps = 1e-3
dichotomy_method(Lx, a, b, eps)

reverse_nodes = list([i[1], i[0]] for i in nodes)
Ly = lagrange(f, reverse_nodes)
print(f'Ly(0) = {Ly(0)}')