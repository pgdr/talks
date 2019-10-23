#!/usr/bin/env python

class memoize(dict):
    def __init__(self, fun):
        self.fun = fun
    def __call__(self, x):
        return self[x]
    def __missing__(self, x):
        y = self[x] = self.fun(x)
        print('computing f(%d) = %d' % (x,y))
        return y

sq = memoize(lambda x: x**2)

for i in range(4):
    print(sq(i))
for i in range(10):
    print(sq(i))
