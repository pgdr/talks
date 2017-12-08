from math import sqrt
import logging

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



def reflow(text):
    """Return triangular textarea as a list of strings and base length."""
    data = tuple(map(len, text))
    N = len(data)
    B = int(sqrt(2 * sum(data)))  # lower bound on base of triangle
    OPT = INF
    while OPT >= INF:
        B += 1
        OPT, split = cost(N-1, B, data)
    logging.info('acc penalty: %d' % OPT)

    prev_split = N
    b = B
    result = []

    while split > 0:
        b -= 2
        result.append(' '.join(text[split:prev_split]))
        prev_split = split
        OPT, split = cost(split-1, b, data)
    logging.info('base size:   %d' % B)
    logging.info('tri height:  %d' % len(result))
    return result, B


def spaces(s):
    s = s.strip()
    return s.count(' ')

def add_spacing(s, b):
    """Add spaces in a line s to get closer to b characters."""
    rem = lambda s_, b_: b_ - len(s_)  # remaining characters
    orig = ''.join(list(s))
    if (rem(s,b)) > s.count('. '):
        s = s.replace('. ', '.  ')
    if (rem(s,b)) > 2*spaces(s) > 0:
        s = s.replace(' ', '   ')
        logging.debug('double-spaced: "%s"' % s)
    if (rem(s,b)) > spaces(s) > 0:
        s = s.replace(' ', '  ')
    if (rem(s,b)) > s.count('. '):
        s = s.replace('. ', '.  ')

    sidepad = rem(s,b)//2
    s = ' '*sidepad + s + ' '*sidepad
    if rem(s,b) > 0:
        s = s + ' '*rem(s,b)
    logging.debug('\n%s\n%s\n%s\n%s\n' % ('='*b, orig, s, '='*b))


    return s

def triangle(text):
    """Returns triangle of text"""
    result, B = reflow(text)

    ret = []

    for i,b in enumerate(range(B, 0, -2)):
        line = ' ' + ' '*b + ' '
        if i < len(result):
            s = result[i]
            logging.debug('stretch penalty %2d for "%s".' % (b-len(s), s))
            s = add_spacing(s, b)
            line = ' %s ' % s
            evenpad = ' ' if (B%2)==1 else ''
        ret.append(' '*i + '/' + evenpad + line + '\\')
    ret.reverse()
    return ret


def treeangle(text):
    """Generates a christmas tree containing the text."""
    text.insert(0, '')
    final = triangle(text)  # the triangle is upside down
    base = len(final[-1])
    final.append('-'*base)
    final.append(' '*(base//2-2) + '| |')          # foot


    final.insert(0,' '*(base//2-4) + '___/\\___')  #  the star
    final.insert(1,' '*(base//2-4) + '\\      /')  #  the star
    final.insert(2,' '*(base//2-4) + '/__  __\\')  #  the star
    final.insert(3,' '*(base//2-4) + '   \\/')     #  the star

    final.insert(4,' '*(base//2-3) + '  /\\')      #  the top
    final.insert(5,' '*(base//2-2) + '/  \\')      #  the top

    return '\n'.join(final)



def xmasdecorator(fun):
    def wrapper(text):
        text = treeangle(text.split())
        res = fun(text)
        return res
    return wrapper
