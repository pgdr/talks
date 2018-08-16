import math

class ufloat(object):
    def __init__(self, value, uncertainty):
        self._value = value
        self._uncertainty = uncertainty

    def __repr__(self):
        return '{} +/- {}'.format(self._value,
                                  self._uncertainty)


    def __iadd__(self, other):
        print('fast add')
        self._value += other
        return self

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = ufloat(other, 0)
        if isinstance(other, ufloat):
            return ufloat(self._value + other._value,
                          self._uncertainty + other._uncertainty)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other  # commutes

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = ufloat(other, 0)
        if isinstance(other, ufloat):
            return ufloat(self._value * other._value,
                          self._uncertainty + other._uncertainty)
        else:
            return NotImplemented


class unit(object):
    def __init__(self, u=None):
        if isinstance(u, unit):
            self._u = u._u
        else:
            self._u = u
            self.normalize()

    def normalize(self):
        def norm():
            if not '/' in self._u:
                return False
            num, den = self._u.split('/')
            for idx, k in enumerate(num):
                if k in den:
                    num = num[:idx] + num[idx+1:]
                    idx = den.index(k)
                    den = den[:idx] + den[idx+1:]
                    self._u = num + '/' + den
                    return True
            return False
        while norm():
            pass

    def __mul__(self, other):
        ss = self._u.split('/')
        os = other._u.split('/')
        if len(ss) == 1:
            ss = ss + ['']
        if len(os) == 1:
            os = os + ['']
        nnum = ss[0] + os[0]
        nden = ss[1] + os[1]
        return unit(nnum + '/' + nden)

    def __repr__(self):
        return self._u

class dimensional(object):
    def __init__(self, val, dim):
        self._val = val
        self._dim = unit(dim)

    def __repr__(self):
        return '{} "{}"'.format(self._val, self._dim)

    def __mul__(self, other):
        if isinstance(other, dimensional):
            return dimensional(self._val * other._val,
                               self._dim * other._dim)
        try:
            return dimensional(self._val * other, self._dim)
        except:
            return NotImplemented



def main():
    D = dimensional
    x = D(ufloat(42.,1), 'm/ss')
    t = D(15, 's')

    print(x*t)

if __name__ == '__main__':
    main()
