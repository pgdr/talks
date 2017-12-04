#!/usr/bin/env python
from pandas import DataFrame
from ecl.ecl import EclSum


class memoize(dict):
    """Memoization wrapper for unary function."""

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        return self[args]

    def __missing__(self, args):
        y = self[args] = self.fun(*args)
        return y


@memoize
def edit(s, t):
    """Compute edit distance of string s and t."""
    if not s:
        return len(t)  # the shortest edit is to add t
    if not t:
        return len(s)  # the shortest edit is to add s

    c = 0 if s[-1] == t[-1] or s[-1] == '*' or t[-1] == '*' else 1

    del_s = edit(s[:-1], t)       # delete last from s
    del_t = edit(s, t[:-1])       # delete last from t
    del_b = edit(s[:-1], t[:-1])  # delete both

    return min(del_s + 1,
               del_t + 1,
               del_b + c)

def to_pandas(kw, smry):
    lst = list(smry[kw])
    split = (map(lambda x: x.days,  lst),
             map(lambda x: x.value, lst))
    return DataFrame({'days': split[0],
                      'value': split[1]})

def find_closest(kw, keys):
    best_score = 10**10
    matches = None
    for key in keys:
        dist = edit(kw, key)
        if dist < best_score:
            matches = []
            best_score = dist
        if dist <= best_score:
            matches.append(key)
    return best_score, matches


def load_smry(fname):
    """Returns (smry,list of keywords)."""
    smry = EclSum(fname)
    return smry, list(smry.keys())


def lookup(smry, keys, kw):
    """Prints kw vector or "did you mean".  """
    if kw in keys:
        print(to_pandas(kw, smry))
    else:
        score, match = find_closest(kw, keys)
        if score <= 4:
            print('Did you mean (score: %d): \n\t%s' % (score,
                                                        '\n\t'.join(match)))
        else:
            print('No such keyword.  Try [L]ist to see keywords.')


def interactive(smry, keys):
    """Interactive smry inspector."""
    kw = None
    while kw != 'q':
        kw = raw_input('Enter kw (q to exit): ').upper().strip()
        if kw in ('Q', 'QUIT'):
            return
        if kw in ('L', 'LIST'):
            print('\n\t'.join(keys))
            continue
        if kw in ('H', 'HELP'):
            print('Commands: Q (quit), L (list), H (this)')
            continue
        lookup(smry, keys, kw)


if __name__ == '__main__':
    from sys import argv
    if len(argv) not in (2, 3):
        exit("""usage: smryinspect.py NORNE_ATW2013.UNSMRY
       smryinspect.py NORNE_ATW2013.UNSMRY FOPR
        """)

    smry, keys = load_smry(argv[1])
    if len(argv) == 2:
        try:
            interactive(smry, keys)
        except EOFError:
            exit('\n')
    else:
        lookup(smry, keys, argv[2].upper().strip())
