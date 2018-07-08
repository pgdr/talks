#!/usr/bin/env python
from __future__ import print_function
from random import shuffle
from math import sqrt
from random import randint
from distributed import Client
import time

POOLSIZE = 1 * 1000
STABILITY = 100
WORKERS = 3 * 10 # num * cores

ALPHABET = '0123456789abcdefghi'
MAP = [
    (59.913869,  10.752245,  'oslo'),
    (60.391263,  5.322054,   'bergen'),
    (58.969976,  5.733107,   'stavanger'),
    (48.856614,  2.352222,   'paris'),
    (51.507351,  -0.127758,  'london'),
    (52.520007,  13.404954,  'berlin'),
    (40.416775,  -3.703790,  'madrid'),
    (52.370216,  4.895168,   'amsterdam'),
    (52.011577,  4.357068,   'delft'),
    (51.924420,  4.477733,   'rotterdam'),
    (41.902783,  12.496366,  'rome'),
    (52.229676,  21.012229,  'warsaw'),
    (29.760427,  -95.369803, 'houston'),
    (55.755826,  37.617300,  'moscow'),
    (37.566535,  126.977969, 'seoul'),
    (-33.868820, 151.209296, 'sydney'),
    (-35.280937, 149.130009, 'canberra'),
    (36.753768,  3.058756,   'alger'),
    (33.513807,  36.276528,  'damascus'),
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

def tour(order):
    """order = [4, 2, 0, 1, 6, 3, 5]"""
    return sum([idist(order[i-1], order[i]) for i in range(1, len(order))])


def individual():
    x = list(ALPHABET[:len(MAP)])
    shuffle(x)  # inplace
    return tuple(x)

def mutate(order):
    order = list(order)
    e1 = randint(0, len(order)-1)
    e2 = randint(0, len(order)-1)
    t = order[e1]
    order[e1] = order[e2]
    order[e2] = t
    return tuple(order)

def crossover(o1, o2):
    N = len(o1) # == len(o2)
    t = randint(1, N-2)
    child = list(o1[:t])
    for i in range(N):
        if o2[i] not in child:
            child.append(o2[i])
    return tuple(child)

def iterate(pool):
    nextgen = []
    for elt in pool:
        nextgen.append(elt)
        nextgen.append(mutate(elt))
        nextgen.append(mutate(elt))
    for i in range(len(pool)//10):
        j = randint(0, len(pool)//10)
        nextgen.append(crossover(pool[i], pool[j]))
    for i in range(len(pool)//10):
        j = randint(0, len(pool)//20)
        nextgen.append(crossover(pool[i], pool[j]))
    for i in range(len(pool)//10):
        j = randint(0, len(pool)//30)
        nextgen.append(crossover(pool[i], pool[j]))
    return nextgen

def submit(client, num, pool):
    results = [client.submit(iterate, pool) for i in range(num)]
    while not all(result.done() for result in results):
        time.sleep(0.1)
        status = ['|' if result.done() else ' ' for result in results]
        print('[{}]'.format(''.join(status)))
    pools = [result.result() for result in results]
    nextpool = set()
    for p in pools:
        nextpool.update(set(p))
    return list(nextpool)

def main():
    client = Client('10.224.36.16:8786')
    pool = [individual() for _ in range(POOLSIZE)]
    stable = 0
    gen = 0
    best = 10**10 # inf
    while stable < STABILITY:
        gen += 1
        pool = submit(client, WORKERS, pool)
        newlen = len(pool)
        #pool = iterate(pool)
        pool = sorted(list(set(pool)), key=tour)
        nextsize = min(POOLSIZE, len(pool))
        pool = list(pool[:nextsize])
        curr = tour(pool[0])
        if curr < best:
            stable = 0
            best = curr
        else:
            stable += 1
        print(gen, pool[0], curr, len(pool), stable, newlen)
    city = lambda x: index(x)[2]
    print(' '.join(map(city, pool[0])))


if __name__ == '__main__':
    from sys import argv
    main()
