import functools
from copy import copy

import collections


class frozendict(dict):
    def __hash__(self):
        return id(self)


@functools.lru_cache(1000 * 1000)
def TSP(v, S, dist):
    mindist = 10 ** 10

    if not S:
        return 0

    for u in S:
        T = S - set([u])
        mindist = min(mindist, dist.get((v, u), 10 ** 10) + TSP(u, T, dist))
    return mindist


edges = [
    ("a", "b", 4),
    ("b", "c", 2),
    ("c", "d", 1),
    ("d", "e", 1),
    ("e", "f", 1),
    ("f", "a", 1),
    ("f", "b", 3),
    ("f", "c", 10),
    ("e", "b", 8),
    ("e", "c", 5),
]

vertices = frozenset([a for (a, _, _) in edges] + [b for (_, b, _) in edges])
dist = {}
for u, v, c in edges:
    dist[(u, v)] = dist[(v, u)] = c

start = "a"
S = frozenset(vertices - set("a"))
res = TSP(start, S, frozendict(dist))
print(res)
