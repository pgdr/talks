#!/usr/bin/env python
from __future__ import print_function
from random import randint
from copy import deepcopy as cp

SIZE = 3000
GENS = 1000

# GENETIC ALGORITHM
def _iterate(pool, mut, cros, fit):
    nextpool = []
    for p in pool:
        nextpool.append(mut(p))
    for i in range(10):
        for j in range(10):
            nextpool.append(cros(pool[i], pool[j]))
    return sorted(list(set(nextpool)), key=fit)[: min(len(pool), len(nextpool))]


def genetic_algorithm(generator, mut, cros, fit):
    pool = [generator() for _ in range(SIZE)]
    for i in range(GENS):
        pool = _iterate(pool, mut, cros, fit)
        if fit(pool[0]) == 0:
            break
        print(pool[0], fit(pool[0]))
    return pool


# END GENETIC ALGORITHM

# UTIL
def randchar():
    return ALPHABET[randint(0, len(ALPHABET) - 1)]


def randpos():
    return randint(0, len(ss) - 1)


# END UTIL

# INDIVIDUALS
ALPHABET = [" "] + map(chr, range(ord("a"), ord("z") + 1))
ss = "methinks it is like a weasel"


def individual():
    x = []
    for i in range(len(ss)):
        x.append(randchar())
    return "".join(x)


def mutate(ind):
    ind = list(ind)
    ind[randpos()] = randchar()
    return "".join(ind)


def crossover(ind1, ind2):
    pos = randpos()
    return ind1[:pos] + ind2[pos:]


def fitness(ind):
    return sum(1 if ind[i] != ss[i] else 0 for i in range(len(ss)))


if __name__ == "__main__":
    pool = genetic_algorithm(individual, mutate, crossover, fitness)
    print(fitness(pool[0]), pool[0])
