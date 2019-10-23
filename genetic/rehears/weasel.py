#!/usr/bin/env python
from __future__ import print_function
from random import randint


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


TARGET = "methinks it is like a weasel"

# util
ALPHABET = "abcdefghijklmnopqrstuvwxyz "


def randchar():
    return ALPHABET[randint(0, len(ALPHABET) - 1)]


def randpos():
    return randint(0, len(TARGET) - 1)


# /util


def weasel_individual():
    return "".join(randchar() for _ in range(len(TARGET)))


def weasel_fitness(ind):
    return sum(0 if TARGET[i] == ind[i] else 1 for i in range(len(TARGET)))


def weasel_mutate(ind):
    n = list(ind)
    n[randpos()] = randchar()
    return "".join(n)


def weasel_crossover(ind1, ind2):
    idx = randpos()
    return ind1[:idx] + ind2[idx:]


if __name__ == "__main__":
    GENERATIONS = 500
    SIZE = 50
    top5 = genetic_algorithm(
        SIZE,
        GENERATIONS,
        weasel_individual,
        weasel_fitness,
        weasel_mutate,
        weasel_crossover,
    )
    for ind in top5:
        print(ind, weasel_fitness(ind))
