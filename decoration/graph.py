#!/usr/bin/env python
from __future__ import print_function
import ast
import inspect

class Graph(object):
    def __init__(self, name='', V=None, E=None):
        self.V = V
        if V is None:
            self.V = set()

        self.E = E
        if E is None:
            self.E = set()
        self.name = name

    def __call__(self):
        return self

    def __repr__(self):
        return 'Graph({},\n      V={},\n      E={})'.format(self.name,
                                                            sorted(self.V),
                                                            sorted(self.E))

def _parse_edge(expr):
    edge = None
    if isinstance(expr.left, ast.BinOp):
        edge = _parse_edge(expr.left)
    if edge is not None:
        return tuple(list(edge) + [expr.right.id])
    return expr.left.id, expr.right.id

def graph(func):
    tree = ast.parse(inspect.getsource(func))
    fdef = tree.body[0]
    body = fdef.body
    name = fdef.name

    edges = set()
    vertices = set()
    for path_expr in body:
        path = _parse_edge(path_expr.value)
        for i in range(1, len(path)):
            u, v = path[i-1], path[i]
            edges.add((u,v))
            vertices.add(u)
            vertices.add(v)

    G = Graph(name, vertices, edges)

    def _wrapper():
        return G
    return _wrapper

@graph
def c4():
    a-b-c-d-a

G = c4()
print(G)


@graph
def peterson():
    A-B-C-D-E-A
    a-c-e-b-d-a
    a-A
    b-B
    c-C
    d-D
    e-E

P = peterson()
print(P)
