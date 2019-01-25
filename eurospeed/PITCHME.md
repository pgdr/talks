# Python 2 is dead

---

**case study**

* a large django project

---

# why

+++

**stick**

* jan 2020
* pandas, numpy, django, scipy are dropping

+++

**carrot**

* (it's a better language)
* unicode
* better iterations
 * `range` (`xrange`)
 * `dict.keys` (`dict.iterkeys`)
 * `map` (`itertools.imap`)

+++

**carrott**

* restrictions on comparators (`'foo' > 4`)
* advanced unpacking
 * `a, *b, c = range(5)`
* keyword-only arguments

```
def f(*,a): return a
f(2) → TypeError: f() takes 0 positional arguments
```

+++

**carrott**

* _f-strings_ (Python 3.6)
 * `f'{round(0.5)} → 0`
* _asyncio_ ?!

+++

# tools

* `caniusepython3 -r req.txt`
 * `🎉  You have 0 projects blocking you from using Python 3!`
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
* `/`

---

**New in Python 3**

+++

# breakpoint()

+++

`breakpoint`

instead of

```
import pdb; pdb.set_trace()

import IPython.embed; embed()

# pidb/pudb/pdbpp/ipython
```

+++

`breakpoint`

set

* `PYTHONBREAKPOINT=IPython.embed` or
* `PYTHONBREAKPOINT=print`
* ... with `breakpoint(a, end='hmm')` (why?)

+++

**data classes**

* old options
 * `collections.namedtuple`
 * `attrs` project (pypi)
 * Class
* data class
 * gives `__lt__`, `__eq__`, `__repr__`

+++

```
@dataclass
class Position:
  name: str
  latitude: float = 0.0
  longitude: float = 0.0
```

params:

`@dataclass(frozen, order, eq, repr, init)`

+++

**module** `__getattr__`, `__dir__`

* `__getattr__`: e.g. for manually issuing deprecation warnings
* `__dir__`: e.g. for manually sorting and other stuff

+++

**postpone** eval of annotation

```
class Node:
    def __init__(self, left: Node, right: Node):
        pass
```

+++

**postpone** eval of annotation

```
class Node:
    def __init__(self, left: 'Node', right: 'Node'):
        pass
```


+++

**time** functions with nanosecond resolution

* (after 104 days, you lose precision)

`time.time()`

+++

**show** deprecation warning in `__main__`

by default

as we missed in ert

+++

**context** variables

* several contexts in asynchronous runs

`contextvar`


+++

**new**

utf-8 mode and `python -X dev`

+++

**dict** keeps insertion order

+++

**keywords**

`async` & `await` are keywords

+++

**setuptools** resources

`importlib.resources` (any file from fs or elsewhere)

improves on `pkg_resources`

---

**On** Asyncio

+++

**Hi** I'm Yuri

+++

`Tulip` and `Twisted`

+++

**In 3.4**

* provisional support
* low-level (features, protocols, transports, callbacks)
* coroutines via `yield from`
* high-level API (streams)

+++

**In 3.5**

* `async` / `await`
* more APIs
* `uvloop` / `Curio`

+++

**In 3.6**

* async generators
* `get_event_loop `
* new low-level APIs
* `Trio`

+++

**In 3.7**

* `contextvars`
* asyncio's code uses `async`/`await`
* `asyncio.run`
* third-party event loops support
* `asyncio.run(f())` (fixed, was e.g. `run_until_complete(f())`)
* `async`/`await` for everything
