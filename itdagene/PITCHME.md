## Decorators

Pål Grønås Drange, _Leading Advisor_

![equinor](https://raw.githubusercontent.com/pgdr/talks/master/itdagene/equinor.png)

_(cc-by-sa 4.0)_

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

Explicit is better than implicit

```python
@app.register
def my_listener():
    # load stuff from database
    # or do other slow stuff

app.register(my_listener)
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


#### Do it in `tmp`

```python
@tmpdir
def my_test():
    assert file_writeing_works()
```

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
* `@app.route('/index.html')`
* `@validate_config`
* `@lru_cache`
* `@logging`
* `@debug`
* `@timeit`


---

## Advanced: `@decorator(something)`

```python
@html('h1')
def header(arg):
    print(arg)
```




+++


```python
def header(arg):
    print(arg)

header = html('h1')(header)
```

+++


```python
def html(tag):
    def the_real_decorator(func):
        def the_new_func(args):
            args = '<{tag}>{arg}</{tag}>'.format(tag=tag, arg=args)
            return func(args)
        return the_new_func
    return the_real_decorator

header = html('h1')(header)
```


---


## Case study: contract-driven development

+++

When you design a class, `Person`:

* `age >= 0`
* `name is not None`
* `len(ssn) == 11`

called _invariants_

+++

For every public function:

```python

def update_ssn(self, new_ssn):
    datainvariant()
    # actually do stuff
    datainvariant()
    return result
```

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

+++

Exceptions

* exceptions are legal
* leaving the object in an invalid state is not
* datainvariant not run on postcondition

+++

Multiple return statements

```python
def update_ssn(self, new_ssn):
    datainvariant()
    old_ssn = do_lots_of_stuff
    if new_ssn == old_ssn:
        return
    # actually do stuff
    datainvariant()
    return result
```

+++

```python
def contract(invariant):
    def the_real_decorator(func):
        def the_new_func(*args):
            invariant()
            try:
                return func(*args)
            finally:
                invariant()
        return the_new_func
    return the_real_decorator


@contract(Person.invariant)
def update_ssn(self, new_ssn):
    do_stuff()
    return result
```


---

# Summary


* Code is about communicating intent

> _'Programs are meant to be read by humans and only incidentally for computers to execute.'_

--- Donald Knuth
