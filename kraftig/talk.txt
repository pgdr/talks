# Talking about software development

We are software developers, but talk surprisingly little about software
development.

I want us to be more concerned with and actively talk about software
development.

Lets talk about API vs Code.

# Version numbers

Version numbering: 25.3, 8.0.0960, 4.13.7, 4.13.b1, 4.0.2, 2.60.3, 3.0, 1.13.3, 1.13.0rc2, 0.20.3

Version numbering: 2017.10, 2017.10


## Software Release Cycle

Pre-alpha -> alpha -> beta -> release candidate -> gold

Every version should have

Version numbering:  Major.Minor.Micro/Patch

* The major number should be increased whenever the API changes in an incompatible way.
* The minor number should be increased whenever the API changes in a compatible way.
* The micro number should be increased whenever the implementation changes, while the API does not.

* If Micro contains a letter, a=alpha, b=beta, rc=release candidate
** beta is intended stable, but may change
** rc is feature frozen


## Why the obsession with version numbers?

A version is defined by its API, its functionality

Once a function goes in, it must stay in until next major version!

## Consequence of software development

Mantra: Bad code can be deleted, bad API is legacy

API = functionality
code = machinery

Code is something that coincidentally makes the API work.



# Code is mass

Code is mass and has a weight.  And somebody is going to carry it.

If we have the choice between implementing a feature, and using an existing
library, the pros and cons are:

* implement it yourself, you (or rather your team) carries the weight
* use somebody else's implementation, they carry the weight, you only carry the load of using that library (which may or may not be expensive)

If all else is equal, less code is better than more code.  Fewer lines is lower
weight.

We should think in terms of code as being something that's just there for the
API to work.

Good PR: +14, -521 --- Bad PR: +3123, -1


## How to design a good API

Use TDD: Sit down, and act like a user of your API!!

Command-query separation


Contract driven


Data invariant


## The end

Perfection of a library is achieved, not when there isn't more to add, but when
there isn't more to remove.

Let's talk about software development.
