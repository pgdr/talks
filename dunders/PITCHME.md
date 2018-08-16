# Why I like Python

better than js

+++

Because Peter Norvig does.

+++

Python doesn't suck.

+++

my opinions, so no need to object

---

Was developed for readability

(it should read like pseudocode)

+++

Great for communicating intent!

+++

Leaves out the unnecessary

* `{` and `}`
* `;`

and type declarations

+++

Code is typically quite dense

despite being easy to read.

+++

Extremely quick to develop in.

Development time is in general more expensive than the additional waiting time.

* creating prototypes (from scratch)
* adopt to new requirements

---

In Javascript you can't do OOP.

In Java you can't not do OOP.

+++

To OOP or not to OOP?  Why not both?

+++

Portable.  Java?  Hah.

---

wiiiidely used

+++

Is in thorough use

(and therefore has libraries,

documentation and forum support for)

* Web-programming (replacing php, cgi, .net, ...)
* System Programming (replacing bash, perl, ruby, ...)
* desktop applications (replacing Java, C++, C#, ...)

+++

A wider audience means

more eyes, means

more robust architecture

+++

Great selection of libraries

(both batteries-included and 3rd party)!

+++

It's very easy to extend with C libraries if something is too slow for you

+++

A proper and fully functional REPL (actually several)

being interpreted makes debugging trivial.

Trivial.

---


Finally: No coercion is done.

+++

You are never surprised

+++

Now ... Javascript, on the other hand ...


+++

Was developed to never let the programmer down

+++

The big JS quiz

+++




```js
> Number.MAX_VALUE > 0
true
> Number.MIN_VALUE < 0
false
```

+++

```js
> 1 < 2 < 3
true
> 3 > 2 > 1
false
```

+++

```js
> 42.toFixed(2)
SyntaxError
> 42.0.toFixed(2)
"42.00"
> 42 .toFixed(2)
"42.00"
```



+++

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

+++

```js
> []+(-~{}-~{}-~{}-~{})+(-~{}-~{})
"42"
```

+++

```js
> ['5'] * 5
25
> ['5'] + 5
"55"
```


+++

```js
> {} + [] + {} + [1]
"0[object Object]1"
```

+++

```js
> {} + []
"0"
```

+++

```js
> ({} + []) + {}
"[object Object][object Object]"
```

+++

```js
> 0 + {}
"0[object Object]"
```

+++

```js
> !+[]+[]+![]
"truefalse"

> ! + []
true

> ! + [] + []
"true"
```

+++

```js
> "1" + "2"
"12"

> "1" / "2"
0.5
```

+++

```js
> [] + -0
"0"
```

+++

```js
> [] == []
false
> [] == ![]
true
```

+++

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

+++

```js
> String(null)
"null"
> String([null])
""
```

---

How is stuff in Python?

+++

```python
> sys.maxsize > 0
True
> -sys.maxsize < 0
True
```

+++

```python
> 1 < 2 < 3
True
> 3 > 2 > 1
True
```

+++

```python
### ??? > 42.toFixed(2)
### ??? SyntaxError
### ??? > 42.0.toFixed(2)
### ??? "42.00"
### ??? > 42 .toFixed(2)
### ??? "42.00"

%0.2f' % 42
42
```

+++

```python
> [] + []
[]

> [] + {}
TypeError

> {} + []
TypeError

> {} + {}
TypeError

> []+(-~{}-~{}-~{}-~{})+(-~{}-~{})
TypeError
```

+++

```python
> ['5'] * 5
['5', '5', '5', '5', '5']
> ['5'] + 5
TypeError

> {} + [] + {} + [1]
TypeError

> {} + []
TypeError
```

+++

```python
> ({} + []) + {}
TypeError

> 0 + {}
TypeError

> !+[]+[]+![]
SyntaxError

> ! + []
SyntaxError

> ! + [] + []
SyntaxError
```

+++

```python
> "1" / "2"
TypeError

> "1" + "2"
'12'

> [] + -0
TypeError
```

+++

```python
> [] == []
True

> [] == ![]
SyntaxError
```

+++

```python
> [1,2,3] == [1,2,3]
True

> [1,2,3] == "1,2,3"
False

> ['x'] == 'x'
False

> [42] == 42
False
```

+++

```python
> str(None)
'None'
> str([None])
'[None]'
```

---

showtime
