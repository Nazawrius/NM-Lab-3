from math import cos

import matplotlib.pyplot as plt
import numpy as np

from dichotomy import dichotomy_method
from lagrange import lagrange
from prohonka import method_prohonky

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
x = np.linspace(-1, 1, 1000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, Lx(x), label='Lx')

a, b = -1, 0
eps = 1e-3
dichotomy_method(Lx, a, b, eps)

reverse_nodes = list([i[1], i[0]] for i in nodes)
Ly = lagrange(f, reverse_nodes)
y = np.linspace(-3, 4.5, 1000)
x = [Ly(i) for i in y]
ax.plot(x, y, label='Ly')
ax.set_xlabel('x')
ax.set_ylabel('y') 
ax.legend()
plt.show()
print(f'Ly(0) = {Ly(0):.6f}')

A = [[4, 1] + [0] * 6]
for i in range(6):
    A.append([0] * i + [1, 4, 1] + [0] * (5 - i))
A.append([0] * 6 + [1, 4])

f = [6/h**2*(nodes[i+1][1] - nodes[i-1][1]) for i in range(1, 9)]

c = [0] + method_prohonky(A, f) + [0]

d = [None] + [(c[i] - c[i - 1])/h for i in range(1, 10)]

a = [node[1] for node in nodes]

b = [None] + [h*c[i]/2 - h**2*d[i]/6 + (a[i] - a[i - 1])/h for i in range(1, 9)]

string = lambda n: f'{n:.5f}' if n < 0 else '+ ' + f'{n:.5f}'
r_string = lambda n: f'{n:.5f}' if n >= 0 else '+ ' + f'{abs(n):.5f}'
for i in range(1, 9):
    print(f's{i} = {a[i]:.5f} {string(b[i])}(x {r_string(nodes[i][0])}) {string(c[i]/2)}(x {r_string(nodes[i][0])})^2 {string(d[i]/6)}(x {r_string(nodes[i][0])})^3, {nodes[i - 1][0]:.2f} <= x <= {nodes[i][0]:.2f}')