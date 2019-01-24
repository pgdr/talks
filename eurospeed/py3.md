Python 3 and asyncio

---

**New in Python 3**

+++

`breakpoint`
* instead of
 * `import pdb; pdb.set_trace()`
 * `# pidb/pudb/pdbpp/ipython`
* set
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

```
@dataclass
class Position:
  name: str
  latitude: float = 0.0
  longitude: float = 0.0
```
* ...
 * `@dataclass(frozen, order, eq, repr, init)`

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
