# Decorators and context managers in Python

We will talk about two advanced but simple features of Python that make coding
more fun (and more safe and more sane and everything).


## Decorators

What is a decorator?  How do we make one?

Perhaps you've seen one of the following:

```python
@skipIf(...)
def test_fun(self):
    pass

@metaclass
class MyClass(object):

    @property
    def msg(self):
        return self._msg

    @classmethod
    def create(cls):
        return MyClass(cls)

    @staticmethod
    def true():
        return MyClass(True)
```


### Decorators in Everest

In Everest we had a couple of validator functions:

```python
def is_valid_realization(r):
    return r > 0

def is_f77(s):
    return len(s) <= 8
```

We wanted a validator function to be able to output a _reason_ why it is False,
but at the same time, a validator should return True or False?

How to come around it so it is cute and nice to use, and hard to use wrong?

Enter decorators.

Suppose the following was possible:

```python

val = is_f77('SOMESTRING')
if not val:
    print('Validation error: %s' % val.msg)  # but False does not have a .msg?
```

We implemented a decorator that you could use like this:



```python

@validation('asserting that r > 0')
def is_valid_realization(r):
    return r > 0

@validation('asserting that s has length at most 8')
def is_f77(s):
    return len(s) <= 8
```

Now, if we run

```python

val = is_f77('SOMESTRING')
if not val:
    print('Validation error: %s' % val.msg)  # but False does not have a .msg?
```

this outputs `Validation error: asserting that s has length at most 8`.


### Decorator implementation

So how do we implement a decorator?

First we made a class that wraps a bool, and contains a msg:

```python
class Validation(object):
    def __init__(self, value, msg=''):
        self.value = value
        self.msg = msg

    def __nonzero__(self):
        return self.value

    def __bool__(self):
        return self.value

    @classmethod
    def true(cls):
        return Validation(True)

    @classmethod
    def false(cls, msg=''):
        return Validation(False, msg=msg)
```

The `__bool__` and `__nonzero__` are just so we can evalute them to
truthy/falsy.

So now, if `is_f77` returns `True`, we would rather output `Validation.true()`,
and if it returns `False`, we instead output `Validation.false(msg='some error
message')`.


### The decorator!

```python
def validator(msg):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            if res is True:
                return Validation.true()
            return Validation.false(msg='FAIL ' + msg + ' for x=' + str(*args))
        return wrapper
    return real_decorator
```


## Context managers

```python
with open('fname', 'r') as f:
    f.write('Hello, world\n')

    f   # f is open
f       # f is closed
```

How does this work?

We will use an example from jokva; `with pushd`.

`pushd` (and `popd`) is a Linux command that changes your directory (works like
`cd`), but remembers where you came from.

You can run `popd` to return to the previous directory.

When `pushd` is called, the directory is pushed onto a stack (`dirs`) and when
`popd` is called, it is popped off the stack.

We want to have this functionality:

```python
with pushd('~/some/path'):
    print(os.cwd())  # returns ~/some/path
    do_stuff()
    call_functions()
os.cwd()  # here we are back to the old cwd
```

### Classical context manager

The with statement is achieved through the use of a context manager.


### Context manager decorators

Simple context managers can use decorators!

```python
# taken from Komodo by jokva

@contextlib.contextmanager
def pushd(path):
    prev = os.getcwd()

    if path is not None:
        os.chdir(path)

    yield
    os.chdir(prev)
```

