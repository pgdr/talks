class interval(object):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def __repr__(self):
        return "[{}, {}]".format(self._left, self._right)

    def __add__(self, other):
        if isinstance(other, interval):
            return interval(self._left + other._left, self._right + other._right)
        else:
            return interval(self._left + other, self._right + other)

    def __radd__(self, other):
        try:
            return self + other
        except:
            return NotImplemented

    def __mul__(self, other):
        return interval(self._left * other, self._right * other)


def main():
    import pint
    from uncertainties import ufloat

    unit = pint.UnitRegistry()
    m = unit("m")
    s = unit("s")

    a = interval(ufloat(10, 1) * m, 2 * s)
    b = a + interval(3 * m, 4 * s)
    print(b * 10)


if __name__ == "__main__":
    main()
