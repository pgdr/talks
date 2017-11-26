## Decorations & context managers


---
### Abstract

Once you've learnt the basics of Python,

the first things to learn that really separates Python from other languages are

*decorators* and *context managers*.

+++

**Decorators** are functions that wrap and possibly modify functions.

They may alter the input to a function, or alter the output of the function.

They may do stuff before, and after, the function call.

They may change the storage of a function, etc.

+++

**Decorators** allow you to write a function the way it is supposed to be
written

and extend the functionality in a very natural way.

+++

If you've ever thought

> _"I must remember to clean up later"_,

Python will help you with a context manager.

You have probably seen the `with open` construct.

We go into more details what **context managers** are and how to define your own
`with`.


---
### Introduction

We will talk about two advanced

simple Python features making coding more fun

(and more safe and more sane and everything).


---
### Decorators


---
#### Fibonacchi

```python
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
```


+++

Here is awesome 1/3:

```python
class memoize:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return self.fun(x)
```

+++

```python
class memoize:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return self.fun(x)


sq = memoize(lambda x: x**2)

sq(7)        # short for sq.__call__(7)
             #           memoize.__call__(sq, 7)
```



+++

Here is awesome 2/3:

```python
class memoize(dict):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        if x not in self:
            self[x] = self.fun(x)
        return self[x]
```

+++

Here is awesome 3/3:

```python
class memoize(dict):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return self[x]

    def __missing__(self, x):
        y = self[x] = self.fun(x)
        return y
```


+++

Using memoized `fib`

```python
class memoize(dict):
    def __init__(self, fun):
        self.fun = fun
    # ...

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

fib = memoize(fib)  # overwrites the `fib` name
```


+++

`@` is syntactic sugar

```python
class memoize(dict):
    def __init__(self, fun):
        self.fun = fun
    # ...

@memoize
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
```





---
#### Decorators in Everest
---

In Everest we had a couple of validator functions:

```python
def is_valid_realization(r):
    return r > 0

def is_f77(s):
    return len(s) <= 8
```

+++

```python
def is_valid_realization(r):
    return r > 0
```

wanted:
1. output _why_ it is False
2. a validator should return True or False?

How to come around it so it is
1. easy to use right
2. hard to use incorrectly?

+++

Enter decorators.

+++

Suppose the following was possible:

```python
val = is_f77('SOMESTRING')
if not val:
    print('Validation error: %s' % val.msg)  # no such .msg?
```

+++

We implemented a _decorator_ used like

```python
@validation('asserting that r > 0')
def is_valid_realization(r):
    return r > 0

@validation('s has length at most 8')
def is_f77(s):
    return len(s) <= 8
```

+++

```python
val = is_f77('SOMESTRING')
if not val:
    print('Validation error: %s' % val.msg)  # no such .msg?
```

gives

```
Validation error: s has length at most 8 for s=SOMESTRING
```


---
#### Decorator implementation
---


So how do we implement a decorator?

First we made a class that wraps a bool, and contains a msg:

+++

```python
class Validation(object):
    def __init__(self, value, msg=''):
        self.value = value
        self.msg = msg

    def __bool__(self):
        return self.value

    @classmethod
    def true(cls):
        return Validation(True)

    @classmethod
    def false(cls, msg=''):
        return Validation(False, msg=msg)
```

+++

`__bool__` is  just so we can evalute

* if `is_f77` returns `True`
  * output `Validation.true()`
* else
  * output `Validation.false(err_msg)`.


+++
#### The decorator!

```python
def validator(msg):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            if res is True:
                return Validation.true()
            return Validation.false(msg='FAIL '
                                    msg
                                    ' for x=' + str(*args))
        return wrapper
    return real_decorator
```






---
### Context managers

(_the dispose pattern_)
---

Have you ever written a line of code, an action, where you thought

> _"Oh, I must remember to revert the action later"_?

The famous action/counter-action pattern is hard to work with, tedious, and
error prone.


---

Examples are
1. `f = open(fname)`
2. `conn = db.open_connection()`
3. `lock.acquire()`
4. `os.chdir(new_path)`
5. `grid.enable_active_indexing_mode()`

+++

These all have counter-actions
1. `f.close()`
2. `conn.close()`
3. `lock.release()`
4. `os.chdir(old_dir)` (you stored `old_dir`, right?)
5. `grid.disable_active_indexing_mode()` (or was it already enabled before the
   _action_?)

+++

These are examples that are
* _hard to use correctly_ and
* _easy to use incorrectly_.

If the API developer forces you to work this way, they are not doing their job.


+++

If we forget to
`1.`  close the file, we risk running out of OS file descriptors and die
+++
`2.`  close the DB connection, we overload the server, may not correctly flush queries
+++
`3.`  release the lock, we might end up in a deadlock state
+++
`4.`  revert the current working directory, this may crash
+++
`5.`  revert back the state of the object we got, caller may be very surprised, even mad
+++
A _context manager_ is a construct that allows you to forget about the second
part.

---

```python
with open('fname', 'r') as f:
    f.write('Hello, world\n')

    f   # f is open
f       # f is closed
```

How does this work?

---

We will use an example from jokva; `with pushd`.

`pushd` (and `popd`) is a Linux command that changes your directory (works like
`cd`), but remembers where you came from.

You can run `popd` to return to the previous directory.

When `pushd` is called, the directory is pushed onto a stack (`dirs`) and when
`popd` is called, it is popped off the stack.

+++

We want to have this functionality:

```python
with pushd('~/some/path'):
    print(os.cwd())  # returns ~/some/path
    do_stuff()
    call_functions()
os.cwd()  # here we are back to the old cwd
```


---
#### Classical context manager

The with statement is achieved through the use of a context manager.

A context manager in Python is simply anything that has the `__enter__` and
`__exit__` functions.

+++

* on entry to `with` (open file, acquire lock..)
  * `__enter__` function is called.
* when `with` scope ends
  * `__exit__` function is called.

The API developer only implements these 2
* _much_ simpler to use correctly,
* _much_ harder to use incorrectly.


---
#### Context managers via decorators

Context managers use decorators with

```python
@contextlib.contextmanager
```

make a function
1. _containing one `yield` statement_
2. and decorate it with `contextlib.contextmanager`.

+++

```python
# taken from Komodo by jokva

@contextlib.contextmanager
def pushd(path):
    prev = os.getcwd()

    os.chdir(path)

    yield  # give control to calling scope

    os.chdir(prev)
```

+++

If we would implement an `active_indexing_mode` in `EclGrid`, we could simply
write:

```python
@contextlib.contextmanager
def ai(self):
    """Temporarily enable active indexing mode."""
    old_mode = self.active_indexing_mode
    self.active_indexing_mode = True

    yield

    self.active_indexing_mode = old_mode
```

---

Finally, we added, in Everest, a temp area working dir in < 15 lines:


```python
@contextlib.contextmanager
def tmp(path=None, teardown=True):
    cwd = os.getcwd()
    fname = tempfile.NamedTemporaryFile().name

    if path:
        shutil.copytree(path, fname)
    else:
        os.mkdir(fname)

    with pushd(cwd):
        yield fname  # give control to caller scope

    if teardown:
        shutil.rmtree(fname)
```

+++

With this, you can copy and goto a completely new directory in `tmp` with

```python
with tmp('test_data/my_case'):
    do_tests()
```

+++


```python
with tmp('test_data/my_case', teardown=False) as pth:
    # we are in /tmp
    print('work area=%s' % pth)
    do_tests()
```

+++

Then, of course, you can make a decorator
```python
def tmpdir(path):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            with tmp(path):
                return function(*args, **kwargs)

        return wrapper

    return real_decorator
```

so you can use it like this to make a function run with a given `cwd`:

+++

```python
@tmpdir('tests/test_data/case1')
def test_run_case1(self):
    self.assertEqual(fname, x)
```
