Number.MAX_VALUE > 0
// true
Number.MIN_VALUE < 0
// false

1 < 2 < 3
// true
3 > 2 > 1
// false


42.toFixed(2)
// SyntaxError
42.0.toFixed(2)
// "42.00"
42 .toFixed(2)
// "42.00"


[] + []
// ""

[] + {}
// "[object Object]"

{} + []
// 0

{} + {}
// NaN


[]+(-~{}-~{}-~{}-~{})+(-~{}-~{})
// "42"


['5'] * 5
// 25

['5'] + 5
// "55"


{} + [] + {} + [1]
// "0[object Object]1"


{} + []
// "0"

({} + []) + {}
// "[object Object][object Object]"

0 + {}
// "0[object Object]"


(!+[]+[]+![]).length
// 9

!+[]+[]+![]
// "truefalse"

! + []
// true

! + [] + []
// "true"


"1" + "2"
"12// "

"1" / "2"
// 0.5

[] + -0
// "0"

[] == []
// false
[] == ![]
// true

[1,2,3] == [1,2,3]
// false

[1,2,3] == "1,2,3"
// true

['x'] == 'x'
// true

[42] == 42
// true

String(null)
// "null"
String([null])
// ""
