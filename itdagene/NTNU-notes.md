# Equinor

We do open source (show github)

As you can see, when we have code open online, it's quite easy to prove
for your that we actually do some programming.

Indeed, most of you would be convinced that we actually know
programming!


One of the first things we ask on an interview is whether the candidate
has code online.

Do yourself a favor; take some code, an assignment or something else
that you made, make it a bit prettier, and put it online somewhere.

There is literally no better way of proving that you can code than to
show us.



# Programming competitions

Something else that is a very good trick is to participate in a
programming contest.



# Python --- why?


Python doesn't suck.

Was developed for readability

Great for communicating intent!

# Python decoration

Why do I want to talk about _decorators_ ?

Because it further improves readability and enables communication!

Furthermore,

* We use it a lot in Equinor, and it's widely used in general
* Few students learn it during their studies


If you have seen Python code, you have probably seen decorators in use.

They look quite innocent,

```
@decorator
def myfunc():
    ...
```

The next half hour or so, we will dive into what this actually means, how we
write one ourselves, and what it is useful for.

So, to what it actually means:

```python
myfunc = otherfunc(myfunc).
```

That wasn't so hard.  That is literally what it means...

Okay, so let's see one in action before we tear the definition apart.


# Example : Xmas

Okay, so what happened?


# Example: `timeit`

suppose a function

# Definition of decorator

Since `@d f()` is equal to `f=d(f)`, we see that `d` takes a function as
argument, hence

```
def timeit(func):
    ...
```

Furthermore, we see that `f` needs to be assigned a function, so `d` needs to
return a function as well!  And, often a different function (we'll see an
example later where we return back `f`.

```python
def decorator(func):
    def inner_function(args):
        ...
    return inner_function
```

now, `decorator` takes a function, and `decorator(func)` returns a function.

Okay, but then we can actually take a look at what we can do;

```python
def decorator(func):
    def new_function(the, args, to, func_):
        return_value = func(the, args, to, func_)
    return new_function
```

That's it.  That's all there is to it.
