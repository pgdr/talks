## Decorations & context managers

(cc-by-sa 4.0)

> Program into Your Language, Not in It

-- Code complete

---
### Python being Python

* *decorators*
* *context managers*

+++

**Decorators** wrap & modify functions.

They may
* alter the input to a function
* alter the output of a function.

+++

**Decorators** allow you to
* write code as supposed
* extend the functionality
  * (with minimal change)

+++
... finally ...
+++

If you've ever thought

> _«I must remember to clean up later»_

Let's see **context managers** fix it


---

### Decorators

---

#### Decorators in Everest

+++

Had validator functions:

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
1. output _why_
2. should return `True`/`False`

wanted:
1. easy to use right
2. hard to use incorrectly?

+++

Wanted:

```python
val = is_f77('SOMESTRING')
if not val:
    print('Validation error: %s' % val.msg)  # no such .msg?
```

+++

We got:

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
    print('Validation error: %s' % val.msg)

# gives


Validation error: s has length at most 8 for s=SOMESTRING
```

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


+++

Other uses of decorators

* `@login_required`
* `@app.route`
* `@validate_config`
* `@lru_cache`
* `@logging`
* `@debug`
* `@timit`

---
### Context managers

(_the dispose pattern_)
---

Did you
* write a line of code,
* an action,
* where you thought

> _«Oh, I must remember to revert the action later»_

+++

> _«Oh, I must remember to revert the action later»_

... pattern is
* hard to work with,
* tedious, and
* error prone.


+++

Examples are
1. `f = open(fname)`
2. `conn = db.open_connection()`
3. `lock.acquire()`
4. `os.chdir(new_path)`
5. `grid.enable_active_idx`

+++

These all have counter-actions
1. `f.close()`
2. `conn.close()`
3. `lock.release()`
4. `os.chdir(old_dir)` (`old_dir`?)
5. `grid.disable_active_idx` (or?)

+++

These are examples that are
* _hard to use correctly_ and
* _easy to use incorrectly_.

+++

```python
lock.acquire()
raise Exception('dang')
lock.release()
```

---

```python
with open(fname, 'r') as f:
    f.write('Hello, world\n')

    f   # f is open
f       # f is closed
```

How does this work?

+++

Example:

* `with pushd`

+++

* `pushd` (and `popd`) is
  * a Linux command
  * changes your directory
    * `cd`
  * but remembers where you where
* `popd` returns
* `pushd` is a stack (`dirs`)

+++

Want:

```python
with pushd('~/some/path'):
    os.cwd()          # prints ~/some/path
    do_stuff()
    call_functions()
os.cwd()              # we are back to old wd
```


---
#### Classical context manager

A context manager must have
*  `__enter__()` and
* `__exit__()` functions.

+++

* on entry to `with` (open file, acquire lock..)
  * `__enter__` function is called.

+++

* on entry to `with` (open file, acquire lock..)
  * `__enter__` function is called.
* when `with` scope ends
  * `__exit__` function is called.

+++

The API developer only implements these 2
* _much_ simpler to use correctly,
* _much_ harder to use incorrectly.


---
#### Context managers via decorators

+++

Context managers use decorators

```python
@contextlib.contextmanager
```

+++

Make a function

1. containing _one_ `yield` statement
2. decorated `@contextmanager`

+++

```python
## From Komodo by jokva

@contextmanager
def pushd(path):
    prev = os.getcwd()

    os.chdir(path)

    yield  # give control to calling scope

    os.chdir(prev)
```


---

In Everest: temporary working dir

+++

Changes and copies dir, yields, deletes

```python
@contextlib.contextmanager
def tmp(path=None, teardown=True):
    cwd = os.getcwd()
    fname = NamedTemporaryFile()

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

Bonus:  make `tmp` a decorator as well

+++

```python
def tmpdir(path):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            with tmp(path):
                return function(*args, **kwargs)

        return wrapper

    return real_decorator
```

so you can use it like this:

+++

```python
@tmpdir('tests/test_data/case1')
def test_run_case1(self):
    self.assertEqual(fname, x)
```

---

## Conclusion

---

Decorators let you

* write nice code
* extend written code
* modify functions, no overhead

+++

Context managers let you

* exception safe context
* rids of action/reaction pattern
* use decorators to make them

---

this is the end
