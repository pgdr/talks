#!/usr/bin/env python
# pypy?

import contextlib
from datetime import datetime as dt


@contextlib.contextmanager
def timed():
    start = dt.now()
    print("I'm timing you ... ")
    yield
    end = dt.now()
    print('Yay!!')
    d = ((end - start) * 1000).total_seconds()
    print('%d ms' % d)


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def cubic(n):
    s = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s += 1
    return s


def main(n):
    with timed():
        s = fib(n)
    return s


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit('Usage: timed n')
    n = int(argv[1])
    main(n)
