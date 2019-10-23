#!/usr/bin/env python
from __future__ import print_function
from random import randint, shuffle
from math import sqrt

# LIB GENETIC


def _iterate(pool, fit, mut, cros):
    nextpool = []
    for ind in pool:
        nextpool.append(ind)
        nextpool.append(mut(ind))
    for i in range(10):
        for j in range(10):
            nextpool.append(cros(pool[i], pool[j]))
    return sorted(list(set(nextpool)), key=fit)[: min(len(pool), len(nextpool))]


def genetic_algorithm(size, generations, individual, fitness, mutate, crossover):
    pool = [individual() for _ in range(size)]
    for _gen in range(generations):
        pool = _iterate(pool, fitness, mutate, crossover)
    return pool[:5]


# / LIB GENETIC


ALPHABET = "0123456789abcdefghi"
MAP = [
    (59.913869, 10.752245, "oslo"),
    (60.391263, 5.322054, "bergen"),
    (58.969976, 5.733107, "stavanger"),
    (48.856614, 2.352222, "paris"),
    (51.507351, -0.127758, "london"),
    (52.520007, 13.404954, "berlin"),
    (40.416775, -3.703790, "madrid"),
    (52.370216, 4.895168, "amsterdam"),
    (52.011577, 4.357068, "delft"),
    (51.924420, 4.477733, "rotterdam"),
    (41.902783, 12.496366, "rome"),
    (52.229676, 21.012229, "warsaw"),
    (29.760427, -95.369803, "houston"),
    (55.755826, 37.617300, "moscow"),
    (37.566535, 126.977969, "seoul"),
    (-33.868820, 151.209296, "sydney"),
    (-35.280937, 149.130009, "canberra"),
    (36.753768, 3.058756, "alger"),
    (33.513807, 36.276528, "damascus"),
]


def index(idx):
    val = ord(idx)
    if val < 97:
        idx = val - 48  # 0-9
    else:
        idx = val - 97 + 10  # a-z
    return MAP[idx]


def dist(c1, c2):
    d0 = (c1[0] - c2[0]) ** 2
    d1 = (c1[1] - c2[1]) ** 2
    return sqrt(d0 + d1)


def coord(idx):
    return index(idx)[0], index(idx)[1]


def idist(idx1, idx2):
    return dist(coord(idx1), coord(idx2))


def tsp_fitness(order):
    """order = [4, 2, 0, 1, 6, 3, 5]"""
    return sum([idist(order[i - 1], order[i]) for i in range(1, len(order))])


def tsp_individual():
    x = list(ALPHABET[: len(MAP)])
    shuffle(x)  # inplace
    return tuple(x)


def tsp_mutate(order):
    order = list(order)
    e1 = randint(0, len(order) - 1)
    e2 = randint(0, len(order) - 1)
    t = order[e1]
    order[e1] = order[e2]
    order[e2] = t
    return tuple(order)


def tsp_crossover(o1, o2):
    N = len(o1)  # == len(o2)
    t = randint(1, N - 2)
    child = list(o1[:t])
    for i in range(N):
        if o2[i] not in child:
            child.append(o2[i])
    return tuple(child)


def _scatter(opt=None):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    x = [e[1] for e in MAP]
    y = [e[0] for e in MAP]
    n = [e[2] for e in MAP]
    ax.scatter(x, y)
    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    if opt is not None:
        for i in range(len(opt) - 1):
            pt1 = index(opt[i])
            pt2 = index(opt[i + 1])
            ax.plot((pt1[1], pt2[1]), (pt1[0], pt2[0]), "ro-")
    plt.show()


if __name__ == "__main__":
    import sys

    GENERATIONS = int(sys.argv[1])
    SIZE = int(sys.argv[2])

    top5 = genetic_algorithm(
        SIZE, GENERATIONS, tsp_individual, tsp_fitness, tsp_mutate, tsp_crossover
    )
    city = lambda x: index(x)[2]
    print(" ".join(map(city, top5[0])))
    print(tsp_fitness(top5[0]))
    _scatter(top5[0])
