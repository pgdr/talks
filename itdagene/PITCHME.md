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

# the classic example: timeit

+++


```
def slow(x):
	s = 0
	for i in range(x * 10**6):
		s += i
	return s
```

+++

```python
def timeit(func):
    def new_func(args):
        from datetime import datetime as dt
        start = dt.now()
        result = func(args)
        end = dt.now()
        duration = end - start
        print('{}({}) took time {}'.format(func.__name__,
                                           args,
                                           duration))
        return result
    return new_func
```

+++

```python
def slow(x):
    ...
slow = timeit(slow)
```


+++


```python
@timeit
def slow(x):
    ...
```

+++

```python
>>> slow(50)
slow(50) took time 0:00:02.524620
1249999975000000
```


---


## Why?


+++

Platonic functions:

```python
@memoize
def fib(x):
    if x <= 1:
        return 1
    return fib(x - 1) + fib(x - 2)
```

+++

Minimizing diff

```patch
+@memoize
def my_slow_function():
    # load stuff from database
    # or do other slow stuff
```

+++

Safer
```python
def database_function():
    lock = get_lock()
    do_some_stuff()

    # lots of code

    do_more_stuff()

    lock.release()
    return stuff
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
@keybinding.add(keys)
def save_buffer():
    pass
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
* `@timeit`


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
