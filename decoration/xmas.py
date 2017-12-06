INF = 10**10
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
def lc(i, j, b, data):
    c = sum(data[i:j+1]) + (j - i)
    if c > b:
        return INF
    return b - c

@memoize
def cost(j, b, data):
    if b <= 0:
        return INF, 0
    if j == 0:
        return lc(j,j,b, data), 0

    best = INF
    best_idx = j
    for i in range(1, j+1):
        c, _ = cost(i-1, b-2, data)
        c += lc(i,j,b, data)
        if c < best:
            best = c
            best_idx = i
    return best, best_idx



def get_matrix(text):
    data = tuple(map(len, text))
    N = len(data)

    B = 0
    OPT = INF
    while OPT >= INF:
        B += 1
        OPT, split = cost(N-1, B, data)

    prev_split = N
    b = B
    result = []

    while split > 0:
        b -= 2
        result.append(' '.join(text[split:prev_split]))
        prev_split = split
        OPT, split = cost(split-1, b, data)
    return result, B

def triangle(text):
    result, B = get_matrix(text)

    ret = []

    for i,b in enumerate(range(B, 0, -2)):
        pad = ' ' + ' '*b + ' '
        if i < len(result):
            s = result[i]
            pad = ' '
            pad += ' '* ((b - len(s)) // 2)
            pad += s
            pad += ' '* ((b - len(s)) // 2)
            pad += ' '
            if (len(s) % 2) != 0:
                pad += ' '
        ret.append(' '*i + '/' + pad + '\\')
    return ret


def treeangle(text):
    final = triangle(text)
    final.reverse()
    final.append('-'*len(final[-1]))
    final.append(' '*(len(final[0])-5) + '| |')
    final.insert(0,' '*(len(final[0])-5) + '/  \\')
    final.insert(0,' '*(len(final[0])-5) + '  /\\')
    final.insert(0,' '*(len(final[0])-5) + '   \\/')
    final.insert(0,' '*(len(final[0])-5) + '/__  __\\')
    final.insert(0,' '*(len(final[0])-8) + '\\      /')
    final.insert(0,' '*(len(final[0])-8) + '___/\\___')
    return '\n'.join(final)



def xmasdecorator(fun):
    def wrapper(text):
        text = treeangle(text.split())
        fun(text)
    return wrapper
