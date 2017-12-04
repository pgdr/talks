#!/usr/bin/env python
class memoize(dict):
    def __init__(self, fun):
        self.fun = fun
    def __call__(self, *args):
        return self[tuple(args)]
    def __missing__(self, args):
        y = self[args] = self.fun(*args)
        return y

@memoize
def edit(s, t):
    if abs(len(s) - len(t)) > 3:
        return 10
    if not s:
        return len(t)
    if not t:
        return len(s)
    c = 0 if s[-1] == t[-1] else 1
    return min(
        1 + edit(s, t[:-1]),
        1 + edit(s[:-1], t),
        c + edit(s[:-1], t[:-1])
    )

def corpus(fname='corpus.txt'):
    with open(fname, 'r') as f:
        return map(lambda x: x.strip(), f.readlines())

def argmin(elt, collection, dist):
    c_score = 10**10
    c_elt   = None
    for w in collection:
        d = dist(elt, w)
        if d < c_score:
            c_score = d
            c_elt = w
    return w,d

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 3:
        print(edit(argv[1], argv[2]))
    elif len(argv) == 2:
        w = argv[1]
        c = corpus()
        print('Corpus: %d words' % len(c))

        best, score = argmin(w, c, edit)
        if score > 0:
            print('Did you mean: %s (dist=%d)' % (best, score))
        else:
            print('Ok: %s' % w)
    else:
        exit('Usage: corpus w1 w2')
