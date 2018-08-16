Why I like Python


Because Peter Norvig does.

Python doesn't suck.


Was developed for readability (it should read like pseudocode)

Great for communicating intent!

Leaves out the unnecessary `{` and `}` and `;` and type declarations

Code is typically quite dense, despite being easy to read.

To OOP or not to OOP?  Why not both?

Portable.  Java?  Hah.

Extremely quick to develop in.  Development time is in general more
expensive than the additional waiting time.

    creating prototypes; it’s easy to use and create code from the scratch;
    adopt to new project requirements and quickly change ongoing development milestone according to updated specifications.


Is in thorough use (and therefore has libraries, documentation and forum support for)

* Web-programming (replacing php/cgi/.net/...)
* System Programming (replacing bash/perl/ruby,...)
* desktop applications (replacing Java, C++, C#, ...)

A wider audience means more eyes which means a more robust architecture


Great selection of libraries (both batteries-included and 3rd party)!


It's very easy to extend with C libraries if something is too slow for you


A proper and fully functional REPL (actually several) - being
interpreted makes debugging trivial.  Trivial.



Finally:

It is strongly typed, just not statically.  No coercion is done.  Only
casting is possible.

You are never surprised (except that something exists)

Type mumbo jumbo


```js
> Number.MAX_VALUE > 0
true
> Number.MIN_VALUE < 0
false
```

```js
> 1 < 2 < 3
true
> 3 > 2 > 1
false
```

```js
> 42.toFixed(2)
SyntaxError
> 42.0.toFixed(2)
"42.00"
> 42 .toFixed(2)
"42.00"
```



```js
> [] + []
""

> [] + {}
"[object Object]"

> {} + []
0

> {} + {}
NaN
```

```js
> []+(-~{}-~{}-~{}-~{})+(-~{}-~{})
"42"
```

```js
> ['5'] * 5
25
> ['5'] + 5
"55"
```


```js
> {} + [] + {} + [1]
"0[object Object]1"
```

```js
> {} + []
"0"
```

```js
> ({} + []) + {}
"[object Object][object Object]"
```

```js
> 0 + {}
"0[object Object]"
```

```js
> !+[]+[]+![]
"truefalse"

> ! + []
true

> ! + [] + []
"true"
```

```js
> "1" / "2"
0.5

> "1" + "2"
"12"
```

```js
> [] + -0
"0"
```


```js
> new Date(0) + 1
"Thu Jan 01 1970 01:00:00 GMT+0100 (CET)1"

> new Date(42) - 1
41
```

```js
> [] == []
false
> [] == ![]
true
```

```js
> [1,2,3] == [1,2,3]
false

> [1,2,3] == "1,2,3"
true

> ['x'] == 'x'
true

> [42] == 42
true
```

```js
> String(null)
"null"
> String([null])
""
```
