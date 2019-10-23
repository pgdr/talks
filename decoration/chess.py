#!/usr/bin/env python
from __future__ import print_function
import ast
import inspect


def coord(x):
    c, r = x
    return int(r) - 1, ord(c) - ord("a")  # col, row


class chess:
    def __init__(self):
        self.board = [
            list("rnbqkbnr"),
            list("pppppppp"),
            list("        "),
            list("        "),
            list("        "),
            list("        "),
            list("PPPPPPPP"),
            list("RNBQKBNR"),
        ]

    def move(self, move):
        from_, to_ = coord(move[:2]), coord(move[2:])
        self.board[to_[0]][to_[1]] = self.board[from_[0]][from_[1]]
        self.board[from_[0]][from_[1]] = " "

    def __repr__(self):
        return (
            "8 "
            + "\n%s ".join(map(lambda x: "".join(x), self.board))
            % (7, 6, 5, 4, 3, 2, 1)
            + "\n  abcdefgh"
        )


def _algparse(func):
    tree = ast.parse(inspect.getsource(func))
    fdef = tree.body[0]
    body = fdef.body

    return [map(lambda elt: elt.id, expr.value.elts) for expr in body]


def algebraic(func):
    alg = _algparse(func)
    c = chess()
    for r in alg:
        for mv in r:
            c.move(mv)

    def wrapper():
        return c

    return wrapper


@algebraic
def deepblue():
    e2e4, c7c5
    c2c3, d7d5
    a1a5, h8h6


print(deepblue())
