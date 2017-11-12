class memoize(dict):
    """Memoization wrapper for any unary function."""
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return self[x]

    def __missing__(self, x):
        print('computing fun(%s)' % x)
        y = self[x] = self.fun(x)
        return y


def memoized(f):
    return memoize(f)


@memoized
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
