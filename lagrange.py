from functools import reduce

def lagrange(f, nodes):
    def L(x):
        s = 0
        n = len(nodes)
        for j in range(n):
            product = lambda x, y: x * y
            top = reduce(product, [x - nodes[i][0] for i in range(n) if i != j])
            bottom = reduce(product, [nodes[j][0] - nodes[i][0] for i in range(n) if j != i])
            s += (top * nodes[j][1]) / bottom
        return s
    
    return lambda x: L(x)