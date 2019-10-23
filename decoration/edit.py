#!/usr/bin/env python


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

    c = 0 if s[-1] == t[-1] else 1

    del_s = edit(s[:-1], t)  # delete last from s
    del_t = edit(s, t[:-1])  # delete last from t
    del_b = edit(s[:-1], t[:-1])  # delete both

    return min(del_s + 1, del_t + 1, del_b + c)


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 3:
        exit("usage: edit string1 string2")
    print(edit(argv[1], argv[2]))
