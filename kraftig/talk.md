# Talking about software development (bærekraftig utvikling)

We are software developers, but talk surprisingly little about software
development.

I want us to be more concerned with and actively talk about software
development.



# The Art of Unix Programming


> Those who do not understand Unix are condemned to reivent it, poorly.

-- Henry Spencer


> This is the Unix philosophy: Write programs that do one thing and do it well.
> Write programs to work together.  Write programs to handle text streams,
> because that is a universal interface.

-- Eric S. Raymond

1. Rule of Modularity: Write simple parts connected by clean interfaces.
2. Rule of Clarity: Clarity is better than cleverness.
3. Rule of Composition: Design programs to be connected to other programs.
4. Rule of Separation: Separate policy from mechanism; separate interfaces from
   engines.
5. Rule of Simplicity: Design for simplicity; add complexity only where you
   must.
6. Rule of Parsimony: Write a big program only when it is clear by demonstration
   that nothing else will do.
7. Rule of Transparency: Design for visibility to make inspection and debugging
   easier.
8. Rule of Robustness: Robustness is the child of transparency and simplicity.
9. Rule of Representation: Fold knowledge into data so program logic can be
   stupid and robust.
10. Rule of Least Surprise: In interface design, always do the least surprising
    thing.
11. Rule of Silence: When a program has nothing surprising to say, it should say
    nothing.
12. Rule of Repair: When you must fail, fail noisily and as soon as possible.
13. Rule of Economy: Programmer time is expensive; conserve it in preference to
    machine time.
14. Rule of Generation: Avoid hand-hacking; write programs to write programs
    when you can.
15. Rule of Optimization: Prototype before polishing. Get it working before you
    optimize it.
16. Rule of Diversity: Distrust all claims for “one true way”.
17. Rule of Extensibility: Design for the future, because it will be here sooner
    than you think.


Lets talk about API vs Code.

> APIs should come with programs, and vice versa.  An API that you must write C
> code to use, which cannot be invoked easily from the command line, is harder
> to learn and use.
>
> And contrariwise, it's a royal pain to have interfaces whose only open,
> documented form is a program, so you cannot invoke them easily from a C
> program.

-- Henry Spencer




# Version numbers

Version numbering:
* 25.3
* 8.0.0960
* 4.13.7
* 4.13.b1
* 4.0.2
* 2.60.3
* 3.0
* 1.13.3
* 1.13.0rc2
* 0.20.3
* 1.8.3.1

Version numbering:
* 2017.10
* 2017.10


## Software Release Cycle

> These are the facts of the case and they are undisputed.

(Though, if you have no intention of making reusable code, don't bother with
this difficult stuff.)

### The anatomy of the version number

Version numbering:  Major.Minor.Micro/Patch

* The major number should be increased whenever the API changes in an incompatible way.
* The minor number should be increased whenever the API changes in a compatible way.
* The micro number should be increased whenever the implementation changes, while the API does not.

Pre-alpha -> alpha -> beta -> release candidate -> gold

* If Micro contains a letter, a=alpha, b=beta, rc=release candidate
  * beta is intended stable, but may change
  * rc is feature frozen

Examples:
* 2.3.pre-alpha1
* 2.3.pre-alpha2
* 2.3.a1
* 2.3.a2
* 2.3.b1
* 2.3.rc1
* 2.3.rc2


## Why the obsession with version numbers?

Because better men than we paved the road.  They wrote unix, GNU coreutils,
Linux, all the software that we use and adore.  They found a way.

> The first and most important quality of modular code is encapsulation.
> Well-encapsulated modules don't expose their internals to each other.  They
> don't call into the middle of each others' implementations, and they don't
> promiscuously share global data.  They communicate using application
> programming interfaces (APIs) — narrow, well-defined sets of procedure calls
> and data structures.

-- Eric S. Raymond


A version is defined by its API, its functionality

Once a function goes in, it must stay in until next major version!


## Consequence of software development

Mantra: Bad code can be deleted, bad API is legacy

* API = functionality
* code = machinery

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
* Refactor --- keep in mind that programming is about abstractions (and we
  discover new abstractions as we go along)
* Always see your test fail once!  (Here's a question: Can we have a robot
  making random changes in code and see if tests fail?)
* Continuously address technical debt.

0/10.




# Code is mass

Good PR: +14, -521 --- Bad PR: +3123, -1

> One of my most productive days was throwing away 1000 lines of code.

-- Ken Thompson


Code is mass and has a weight.  And somebody is going to carry it.

If we have the choice between implementing a feature, and using an existing
library, the pros and cons are:

* implement it yourself, you (or rather your team) carries the weight
* use somebody else's implementation, they carry the weight, you only carry the
  load of using that library (which may or may not be expensive)

If all else is equal, _less code_ is better than _more code_.  Fewer lines
equals lower weight.

We should think in terms of code as being something that's just there for the
API to work.

> Thou shalt study thy libraries and strive not to re-invent them without cause,
> that thy code may be short and readable and thy days pleasant and productive.

-- Henry Spencer's _"The Ten Commandments for C Programmers"_


## How to design a good API

> There are two ways of constructing a software design: One way is to make it so
> simple that there are obviously no deficiencies, and the other way is to make
> it so complicated that there are no obvious deficiencies. The first method is
> far more difficult.

-- C.A.R. Hoare


Use TDD: Sit down, and act like a user of your API!!

Command-query separation


Design by Contract
* Formal API (contracts)
* data invariants (who has seen the following?)

```java
private void datainvariant() {
    assert this.age >= 0;
    assert !this.name.isEmpty();
    assert this.parent != null;
}
```

It's not necessarily a good idea, but it's good to have an idea about it.

## Code smells

> A code smell is a surface indication that usually corresponds to a deeper
> problem in the system

-- Martin Fowler / Ken Beck

* Long method
* Conditional Complexity
* Large Class
* Type Embedded in Name
* Dead Code
* Speculative Generality (YAGNI)
* Data Class
* Indecent Exposure (You should have a compelling reason for every item you make public.)
* Lazy Class


## The end

> It seems that perfection is attained, not when there is nothing more to add,
> but when there is nothing more to take away.

-- Antoine de Saint-Exupéry

Let's talk about software development.
