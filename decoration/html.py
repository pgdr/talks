#!/usr/bin/env python
from __future__ import print_function


def html(fun):
    def wrapper(arg):
        print("<p>")
        x = fun(arg)
        print("</p>")
        return x

    return wrapper


@html
def write(text):
    print(text)
    return 7


x = write("hello worlds")
print(x)

# <h1>
# hello worlds
# </h1>
