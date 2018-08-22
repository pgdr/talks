# About reviews

+++

Mostly musings, but also heavily based on
* The Pragmatic Programmer
* Code Complete
* Making software


---


What is _quality_?

> _"the degree of excellence of something"_

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
- maintainable
  - readable and understandable

+++

- no bugs
- features
- efficient
- maintainable
  - readable and understandable
- really good
  - extendible and reusable

---

What is an editor's job?

+++

an editor

- reviews and edits drafts
- reviews manuscript for publishing
- oversees publication process
- works closely with author to perfect manuscript

why?

+++

an editor

- reviews and edits drafts
- reviews manuscript for publishing
- oversees publication process
- works closely with author to perfect manuscript

why?

- because the author isn't good enough

+++

no ...

- too close to the concepts
  * could it be told differently
  * simpler?
- semantic satiation
  * good names
  * correctly chosen words
- especially true for code


---


how we work

(there is no right way)

(except agile)

+++

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

+++


a workflow that works for _our_ team

+++

![Kanban](https://raw.githubusercontent.com/pgdr/talks/master/review/kanban.png)

+++

![Reviewing](https://raw.githubusercontent.com/pgdr/talks/master/review/everreview.png)

+++

![PR](https://raw.githubusercontent.com/pgdr/talks/master/review/everpr.png)

+++

![Everest approved](https://raw.githubusercontent.com/pgdr/talks/master/review/evergreen.png)



---

So what is _collaborative construction_?


+++

1. Self-check
2. Pair programming
3. Peer review / informal walk through
4. Formal inspection

+++


Self-check:

* read your own code
* quickest and simplest form of review

> Not as efficient, but better than nothing

+++


Pair programming

* four eyes over two
* the programmers should be "compatible"
  * personality clashes can disrupt productivity
* quality improves on complex tasks (not simple)

> _insights are often found by simply describing the problem aloud_



+++

Peer reviews and walk-throughs

* Either read and commented by reviewer
* ... or walk-through hosted and moderated by author

_(Used unintelligently, walk-throughs are more trouble than they are worth)_

+++

Formal inspection

* for large non-trivial proposals
* focus on defects (not fixes)
* Use checklist and a moderator
* all participants must prepare

_(while code inspection is effective, conducting reviews in meetings is not)_

> IBM reports 80-90% defects found, saving 25% resources

---





Pros of code review

+++

* finding bugs
* uncovering weaknesses
* improve variable names, local/global
* formatting and comments
* new team members need guidance
* reviewer gets to read more code

+++

* better code quality
* someone leaving the project has less impact
* bug tickets can be assigned to more people (fixed faster)
  * essential when sick leave
  * cost 10-100 times more expensive after deploy
* you don't _get away_ with dirty hacks

+++

* reading other people's source code and documentation,
* either informally or during code reviews
* It's not snooping; it's learning
* when introducing bugs, you're not the only one to blame


+++

hard data

+++

* Finding 1 bug/10min (wow!)
* max 60 min of review (fatigue)
* up to 400---500 LOC per hour

Conclusion
* PR should be at most 500 lines
* review should take at most 1h

(Best to have code in IDE)


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

creates tension between distributed teams ...


+++

> Online, there is no tone of voice, facial expressions, or extra context to
> really help distinguish intent.

+++

> Never attribute to malice that which is adequately explained by lack of
> context in online conversations.

+++

> When writing a message, we're responsible for ensuring that the intent is
> clearly portrayed.

+++

guidelines on how to communicate online:

1. Assume that you are asking *me* for a *favour*.
2. Assume your *boss* will read what you say.
3. Assume *your family* will read what you say.

---

happy reviewing
