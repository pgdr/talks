# Talking about software development

We are software developers, but talk surprisingly little about software
development.

I want us to be more concerned with and actively talk about software
development.

Lets talk about API vs Code.



# Version numbers

Version numbering: 25.3, 8.0.0960, 4.13.7, 4.13.b1, 4.0.2, 2.60.3, 3.0, 1.13.3, 1.13.0rc2, 0.20.3, 1.8.3.1

Version numbering: 2017.10, 2017.10


## Software Release Cycle

> These are the facts of the case and they are undisputed.

Pre-alpha -> alpha -> beta -> release candidate -> gold

Every version should have

Version numbering:  Major.Minor.Micro/Patch

* The major number should be increased whenever the API changes in an incompatible way.
* The minor number should be increased whenever the API changes in a compatible way.
* The micro number should be increased whenever the implementation changes, while the API does not.

* If Micro contains a letter, a=alpha, b=beta, rc=release candidate
  * beta is intended stable, but may change
  * rc is feature frozen


## Why the obsession with version numbers?

Because better men than we paved the road.  They wrote unix, GNU coreutils, Linux, all the software that we use and adore.  They found a way.  (Quote Eric S Raymond)

A version is defined by its API, its functionality

Once a function goes in, it must stay in until next major version!

## Consequence of software development

Mantra: Bad code can be deleted, bad API is legacy

API = functionality
code = machinery

Code is something that coincidentally makes the API work.




# Popular scientific approach

## Site 1

* test first
* rigorous, regular refactoring
* continuous integration
* simple design
* single coding standard to which all programmers adhere

3 / 5

## Site 2

* PEP-8
* YAGNI (You ain't gonna need it)
* Test _your_ code, not others'
* API: Simple things should be simple, complex things should be possible
* Code is the enemy --- write less, delete, don't write
* External facing APIs are where design up-front matters!
  * Changing API is painful
  * creating backwards incompatibility is horrible
  * design carefully! (But keep simple things simple ...)
* If a function or method is more than 30LOC, break it up!
* Refactor --- keep in mind that programming is about abstractions (and we discover new abstractions as we go along)
* Always see your test fail once!  (Here's a question: Can we have a robot making random changes in code and see if tests fail?)
* Continuously address technical debt.

0/10.




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


Design by Contract
* Formal API (contracts)
* data invariants (who has seen the following?)
```
private void datainvariant() {
    assert this.age >= 0;
    assert !this.name.isEmpty();
    assert this.parent != null;
}
```

It's not necessarily a good idea, but it's good to have an idea about it.


## The end

Perfection of a library is achieved, not when there isn't more to add, but when
there isn't more to remove.

Let's talk about software development.
