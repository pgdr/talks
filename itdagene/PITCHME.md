## Decorators

(cc-by-sa 4.0)

+++

# Open

show us the code

+++

# NCPC

Nordic Collegiate Programming Contest

Saturday October 6 2018

[https://ncpc.idi.ntnu.no/](ncpc.idi.ntnu.no)

+++

![NCPC 2017 final standings](https://raw.githubusercontent.com/pgdr/talks/master/itdagene/ncpc2017.png)


---

```python
@decorator
def fun(args):
    ...
```

+++


```python
fun = decorator(fun)
```

+++

```python
@dec
def fun(args):            def fun(args):
    ...                          ...
                          fun = dec(fun)
```

+++

```python
def noop(f):
    return f

def sq(x):
    return x**2
sq = noop(sq)
```

+++

```python
def noop(f):
    def other_function():
        # hmm?
    return other_function

def sq(x):
    return x**2
sq = noop(sq)
```

+++

```python
def noop(f):
    def other_function(arg):
        # hmm?
    return other_function

def sq(x):
    return x**2
sq = noop(sq)
```

+++

```python
def noop(f):
    def other_function(arg):
        result = f(arg)
        return result
    return other_function

def sq(x):
    return x**2
sq = noop(sq)
```

+++

```python
def noop(f):
    def other_function(arg):
        print('before call')
        result = f(arg)
        print('after call')
        return result
    return other_function

def sq(x):
    return x**2
sq = noop(sq)
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
        result = func(args)
        end = dt.now()
        print('f({}) took time {}'.format(args,
                                          (end - start)))
        return result
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


+++

Platonic functions:

```python
@memoize
def fib(x):
    if x <= 1:
        return 1
    return fix(x-1) + fib(x-2)
```

+++

Minimizing diff

```patch
+@memoize
def my_slow_function():
    # load stuff from database
    # or do other slow stuff
```



---


# Examples in the wild

+++

#### Keybindings

```python
def save_buffer():
    pass

# somewhere below

keybindings.add(save_buffer, keys)
```

+++

```python
@keybinding.add(Keys.CTRL * 'x' + Keys.CTRL * 's')
def save_buffer():
    # save to file here ...
```


+++


#### Filters

```python
def my_filter(gen):
    # do filter stuff

# somewhere below

app.filter(my_filter, 'filtername')
```

+++



```python
@app.filter('filtername')
def my_filter(gen):
    # do filter stuff
```


+++

#### Pipeline


```python
def fft(timeseries):
    # do Fourier transform


@after(fft)
def powerdensity(timeseries):
   pass

@after(powerdensity)
@output
def my_function(timeseries):
    # plot
```

+++

* `@login_required`
* `@app.route`
* `@validate_config`
* `@lru_cache`
* `@logging`
* `@debug`
* `@timit`


---

## Case study: contract-driven development

+++

```python
def function(args):
    datainvariant()
    # some code
    # lots more code
    # yet more code
    datainvariant()
    return answer
```

Problems?
