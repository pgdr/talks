#!/usr/bin/env python
from __future__ import print_function

try:
    from functools32 import lru_cache
except ImportError:
    from functools import lru_cache

from math import sqrt
import logging

INF = 10**10


def lc(i, j, b, data):
    c = sum(data[i:j + 1]) + (j - i)
    if c > b:
        return INF
    return (1 + (b - c))**2


@lru_cache(maxsize=10**8)
def cost(j, b, data, remaining):
    """Cost of placing a newline after j given b characters per line.

    Return the score and the index of the next newline (backwards).
    """
    if remaining < 0:
        return INF, 0
    if b <= 0:
        return INF, 0
    if j == 0:
        return lc(j, j, b, data), 0

    best = INF
    best_idx = j
    for i in range(1, j + 1):
        c, _ = cost(i - 1, b, data, remaining-1)
        c += lc(i, j, b, data)
        if c < best:
            best = c
            best_idx = i
    return best, best_idx


def reflow(text):
    """Return textarea as a list of strings and square size."""
    data = tuple(map(len, text))  # (list of word lengths)
    logging.debug('Actual data we use for DP: %s' % str(data))
    N = len(data)
    logging.info('N=%d' % N)
    B = int(sqrt(sum(data)))  # lower bounds of square
    OPT = INF
    while OPT >= INF:
        logging.debug('Testing size B=%d' % B)
        B += 1
        OPT, split = cost(N, B, data, B)
    logging.info('acc penalty: %d' % OPT)

    prev_split = N
    b = B
    result = []

    while split > 0:
        result.append(' '.join(text[split:prev_split]))
        prev_split = split
        OPT, split = cost(split - 1, b, data, b)
    logging.info('base size:   %d' % B)
    logging.info('tri height:  %d' % len(result))
    return result, B


def spaces(s):
    s = s.strip()
    return s.count(' ')


def _add_intersentence_spacing(s, b):
    rem = lambda s_, b_: b_ - len(s_)  # remaining characters
    for c in '.!?;:':
        pre = '%s ' % c
        post = '%s  ' % c
        if (rem(s, b)) >= s.count(pre):
            s = s.replace(pre, post)
    return s


def _add_spacing(s, b):
    """Add spaces in a line s to get closer to b characters."""
    rem = lambda s_, b_: b_ - len(s_)  # remaining characters
    orig = ''.join(list(s))
    s = _add_intersentence_spacing(s, b)
    if (rem(s, b)) > 2 * spaces(s) > 0:
        s = s.replace(' ', '   ')
        logging.debug('double-spaced: "%s"' % s)
    if (rem(s, b)) > spaces(s) > 0:
        s = s.replace(' ', '  ')
    if (rem(s, b)) > s.count('. '):
        s = s.replace('. ', '.  ')

    s += ' ' * rem(s, b)
    logging.debug('\n%s\n%s\n%s\n%s\n' % ('=' * b, orig, s, '=' * b))

    return s


def triangle(text):
    """Returns triangle of text"""
    result, B = reflow(text)

    ret = []

    for i in range(len(result)):
        s = result[i]
        logging.debug('stretch penalty %2d for "%s".' % (B - len(s), s))
        s = _add_spacing(s, B)
        line = '| %s |' % s
        ret.append(line)
    ret.reverse()
    return ret


def square(text):
    """Generates a square containing the text."""
    text = text.split()
    text.insert(0, '')
    final = triangle(text)
    base = len(final[-1])
    final = ['-' * base] + final
    final.append('-' * base)

    return '\n'.join(final)


def main(text):
    print(square(text))


if __name__ == '__main__':
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    from sys import argv
    if len(argv) > 1:
        main(' '.join(argv[1:]))
    else:
        from sys import stdin
        d = []
        for x in stdin:
            d.append(x.strip())
        d = ' '.join(d).replace('\n', ' ').replace('=', ' ')
        while '  ' in d:
            d = d.replace('  ', ' ')
        main(d)
