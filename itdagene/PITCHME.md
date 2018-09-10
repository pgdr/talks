## Decorators

(cc-by-sa 4.0)

---

```python

@decorator
def myfunc(args):
    ...

```

+++


```python
myfunc = otherfunc(myfunc)
```

+++

```python
def myfunc(x):
    import time
    time.sleep(1.5)
    return x**2
```

```
>>> myfunc(7)
49
```

+++

```python
def timeit(func):
    def wrapper(args):
        from datetime import datetime as dt
        start = dt.now()
        ret = func(args)
        end = dt.now()
        print('f({}) took time {}'.format(args,
                                          (end - start)))
        return ret
    return wrapper
```

+++

```python

def myfunc(x):
    import time
    time.sleep(1.5)
    return x**2


>>> myfunc(7)
f(7) took time 0:00:01.501650
49
```


---

## Breakdown

+++

```python
@decorator
def f():
    ...
```

```python
f = decorator(f)
```

`decorator` takes a function as argument, hence

```python
def decorator(func):
    ...
```

But `decorator(f)` also _returns_ a function, so

```python
def decorator(func):
    def inner_function(args):
        ...
    return inner_function

```

+++

```python
def decorator(func):
    def new_function(the, args, to, func_):
        return_value = func(the, args, to, func_)
    return new_function


@decorator
def myfunc(args):
    print('Hello, world!')

```

That's equivalent to ...

+++

```python
def decorator(func):
    def new_function(the, args, to, func_):
        return_value = func(the, args, to, func_)
    return new_function

def myfunc(args):
    print('Hello, world!')
myfunc = decorator(myfunc)
```

---

## What's cool about that?
