## Decorations & context managers

(cc-by-sa 4.0)

> Program into Your Language, Not in It

-- Code complete

---
### Abstract

When mastered Python basics,

*decorators* and *context managers*.

+++

**Decorators** are functions that wrap/modify functions.

They may
* alter the input to a function
* alter the output of the function.

+++

**Decorators** allow you to
* write code as supposed
* extend the functionality

+++

If you've ever thought

> _"I must remember to clean up later"_,

Let's see **context managers** (Python `with`)


---
### Decorators
---

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

* Django uses `@login_required`
* Flask uses `@app.route`
* `@validate_json` or `@validate_config`
* Add signed messages with `@signed(secret_key)`
* Wrap text in html (literally decorate)
* Decorate your UI component (textarea with scrollbar)
* timing, sleeping, debugging, logging



---
### Context managers

(_the dispose pattern_)
---

Did you
* write a line of code,
* an action,
* where you thought

> _"Oh, I must remember to revert the action later"_?

... pattern is
* hard to work with,
* tedious, and
* error prone.


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



---

```python
with open('fname', 'r') as f:
    f.write('Hello, world\n')

    f   # f is open
f       # f is closed
```

How does this work?

---

We will use an example from Komodo; `with pushd`.

+++

`pushd` (and `popd`) is
* a Linux command
* changes your directory
  * `cd`
* but remembers where you where

Run `popd` to return.

`pushd` is a stack (`dirs`)

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

The `with` statement is achieved with CMs.

A CM in Python must have
*  `__enter__` and
* `__exit__` functions.

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

Context managers use decorators with

```python
@contextlib.contextmanager
```

make a function
1. _containing one `yield` statement_
2. and decorate it:
  * `contextlib.contextmanager`.

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


---

In Everest: temporary working dir

++


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
* manage functions with little overhead

+++

Context managers let you
* safely change context
* rids of action/reaction pattern
* use decorators to make them

---
fin
