class interval(object):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def __repr__(self):
        return '[{}, {}]'.format(self._left,
                                 self._right)

    def __add__(self, other):
        if isinstance(other, interval):
            return interval(self._left + other._left,
                            self._right + other._right)
        else:
            return interval(self._left + other,
                            self._right + other)

    def __radd__(self, other):
        try:
            return self + other
        except:
            return NotImplemented

    def __mul__(self, other):
        return interval(self._left * other,
                        self._right * other)

    def __iter__(self):
        yield self._left
        yield self._right


def main():
    import pint
    unit = pint.UnitRegistry()
    a = interval(1 * unit('m'), 2 * unit('ft'))
    b = a + interval(3* unit('m'),unit('m')* 4)
    print(b * 10)


if __name__ == '__main__':
    main()
