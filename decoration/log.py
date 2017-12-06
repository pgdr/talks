#!/usr/bin/env python
from __future__ import print_function

from xmas import xmasdecorator

@xmasdecorator
def log(msg):
    print(msg)


def main(txt):
    log(txt)

if __name__ == '__main__':
    from sys import stdin
    d = []
    for x in stdin:
        d.append(x.strip())
    d = ' '.join(d).replace('\n', ' ')
    d = d.replace('  ', ' ')
    log(d)
