# About reviews

+++

based on
* The Pragmatic Programmer
* Code Complete
* ...

---


how we work


+++

there is no right way

+++

the only request is that we work in an agile way:

+++

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

+++


a workflow that works for _our_ team

+++

_pic of teamboard_

+++

_pic of pr_

+++

_pic of review approval and green buttons_





---


So what is _collaborative construction_?


+++

1. Rubber duck
2. Pair programming
3. Peer review / informal walk through
4. Formal inspection

+++

Rubber duck ...

> _insights are often found by simply describing the problem aloud_

+++

The rubber duck insight from pair programming

+++

Pair programming

* four eyes over two
* rotate pairs
* the programmers should be "compatible"

+++

Peer reviews and walk-throughs

* Either read and commented by reviewer
* ... or walk-through hosted and moderated by author
* 

+++

Formal inspection

* Use checklist
* focus on defects (not fixes)
* moderator
* all participants must prepare
* leaders do not attend

_(while code inspection is effective, conducting reviews in meetings is not)_

---


What is _quality_?

+++

- no bugs
- features

+++

- no bugs
- features
- efficient

+++

- no bugs
- features
- efficient
- maintainable(?)

+++

- no bugs
- features
- efficient
- readable and understandable
- extendible

---

What is an editor's job?

+++

an editor

- reviews manuscript for publishing
- review and edit drafts
- oversee publication process
- working closely with author to perfect manuscript

why?

+++

an editor

- reviews manuscript for publishing
- review and edit drafts
- oversee publication process
- working closely with author to perfect manuscript

why?

- because the author isn't good enough

+++

authors get blind



---


Pros of code review

+++

* finding bugs
* uncovering weaknesses
* improve variable names, local/global
* formatting and comments
* new team members need guidance

+++

* better code quality
* someone leaving the project has less impact
* bug tickets can be assigned to more people (fixed faster)
* you don't _get away_ with dirty hacks
* 

+++

* reading other people's source code and documentation,
* either informally or during code reviews
* It's not snooping; it's learning

---

We do review because four eyes are better than two

---

We do review because it distributes knowledge

---

Cons

+++

takes time that could be spent coding

(according to research, benefit in the long run)

+++

bike-shedding

(fix: coding standards)

(fix: don't review "easy" stuff)

+++

cargo cult?

(don't believe that review _fixes_ anything)

(more experienced should review new members)

+++

creates tension between distributed teams

(more on this now!)

+++

https://mail.python.org/pipermail/python-ideas/2018-August/052722.html

> Never attribute to malice that which is adequately explained by lack of
> context in online conversations.

+++

> Online, there is no tone of voice, facial expressions, or extra context to
> really help distinguish intent.

> When writing a message, we're responsible for ensuring that the intent is
> clearly portrayed.

> When reading a message, we're responsible for correctly interpreting such
> intent, and everyone is usually better off if, when in doubt, the
> interpretation leans towards ambiguity over malice.

