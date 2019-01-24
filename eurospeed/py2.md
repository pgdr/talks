# Python 2 is dead

---

**case study**

* a large django project

---

**why**

+++

**stick**

* jan 2020
* pandas, numpy, django, scipy are dropping

+++

**carrot**

* unicode
* better iterations
 * `range` (`xrange`)
 * `dict.keys` (`dict.iterkeys`)
 * `map` (`itertools.imap`)
* restrictions on comparators (`'foo' > 4`)
* advanced unpacking `a, *b, c = range(5)`
* keyword-only arguments
 * `def f(*,a): return a`
 * `f(2)` → `TypeError: f() takes 0 positional arguments`
* _f-strings_ (Python 3.6) `f'{round(0.5)} → 0`
* _asyncio_ ?!

+++

**tools**

* `caniusepython3 -r req.txt`
* `2to3`
 * (`print`, `input`, module renames, ...?)
 * puts `list()` around iterators
 * adds `()` after `print` statements
* `modernize`
* `tox`
* `pylint -py3k`
* `python -3 ?`

+++

**gotchas**

* rounding (banker's)
* `Exception.message` is replaced with `str(e)`
* `hash(·)` is randomized per process
* pickling in py2, unpickling in py3 fails (_obviously_)
* sorting works (or doesn't(?), but behaves)
