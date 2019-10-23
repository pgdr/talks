#!/usr/bin/env python
from __future__ import print_function
from random import randint, shuffle
from copy import deepcopy
from math import sqrt

# LIB GEN
def _iterate(pool, size, fitness, mutate, crossover):
    for i in range(size // 2):
        pool.append(mutate(pool[i]))

    for i in range(size // 2):
        for j in range(size // 2):
            pool.append(crossover(pool[i], pool[j]))

    pool = sorted(set(pool), key=fitness)[:size]
    return pool


def genetic(size, generations, individual, fitness, mutate, crossover):
    pool = [individual() for _ in range(size)]
    for _ in range(generations):
        pool = _iterate(pool, size, fitness, mutate, crossover)
    return pool


# / LIB GEN

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


def randpos():
    return randint(0, len(MAP) - 1)


def individual():
    ind = deepcopy(MAP)
    shuffle(ind)
    return tuple(ind)


def dist(p1, p2):
    x = (p1[0] - p2[0]) ** 2
    y = (p1[1] - p2[1]) ** 2
    return sqrt(x + y)


def fitness(ind):
    return sum(dist(ind[i], ind[i + 1]) for i in range(len(ind) - 1))


def mutate(ind):
    a, b = randpos(), randpos()
    ind = list(ind)
    ind[a], ind[b] = ind[b], ind[a]
    return tuple(ind)


def crossover(ind1, ind2):
    idx = randpos()
    ind = list(ind1)[:idx]
    for e in ind2:
        if e not in ind:
            ind.append(e)
    return tuple(ind)


def _scatter(opt=None):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    fig, ax = plt.subplots()
    x = [e[1] for e in MAP]
    y = [e[0] for e in MAP]
    n = [e[2] for e in MAP]
    ax.scatter(x, y)
    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    if opt is not None:
        for i in range(len(opt) - 1):
            pt1 = opt[i]
            pt2 = opt[i + 1]
            ax.plot((pt1[1], pt2[1]), (pt1[0], pt2[0]), "ro-")
    plt.show()


if __name__ == "__main__":
    print(len(MAP))
    pool = genetic(30, 2000, individual, fitness, mutate, crossover)
    best = pool[0]
    print(fitness(best), best)
    _scatter(best)
