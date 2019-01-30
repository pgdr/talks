## Software development demystified

+++
## Software development demystified

> Mysticism refers to the attainment of insight in ultimate or hidden truths,
> and to human transformation supported by various practices and experiences.

+++
## Software development demystified

> Mysticism refers to the attainment of insight in ultimate or hidden truths,
> and to human transformation supported by various practices and experiences.

... so, nothing to demystify


+++
## Game of Life

Imagine an infinite grid, with each cell alive or dead.

* Each living cell with
 * one or no neighbors dies, as if by solitude
 * four or more neighbors dies, as if by overpopulation
 * two or three neighbors survives
* Each dead cell with
 * three neighbors becomes populated


+++
## Game of Life

![Glider](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/gol-glider.gif)


+++
## Game of Life

![Cannon](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/cannon.gif)


+++
## Game of Life

![Spaceships](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/spaceships.gif)


+++
## Game of Life

![GOL machine](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/gol.gif)


+++
## Game of Life

![Turing machine](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/turing.png)


+++
### Power (Turing)

* Game of Life
* `Y=λf.(λx.f(xx))(λx.f(xx))`
* programming languages
 * C++
 * Python
 * ...

Can run _any_ program, simulation, computation.

They can simulate (as far as we know) a human brain!


+++
### Software development

is extremely complex


+++
### Software development

 ... but billions of CPUs run millions of instructions per second


+++
### Software development

there is not a single thing today not involving an instruction written by a
developer

#### digitalization = it


+++
### Software development

> Access to developers is a bigger threat to business success than access to
> capital.


+++
### Software development

 ... but we have methods, best practices and experience

_(backed by empirical evidence)_


---
### Software Craftsmanship


+++
### Software Craftsmanship

* responsibility
* trust


+++
### Software Craftsmanship

The waterfall model


+++
### Software Craftsmanship

The waterfall model is broken


+++
### Software Craftsmanship

Agile manifesto


+++
### Software Craftsmanship

**Individuals and interactions** over _processes and tools_
**Working software** over _comprehensive documentation_
**Customer collaboration** over _contract negotiation_
**Responding to change** over _following a plan_



---
### Software projects

We have a choice now,

1. do IT projects correctly to best of knowledge
2. do IT projects as C&C, waterfall or [insert preference]


+++
### Software projects

* process mistakes (45%)
* people mistakes (42%)
* product mistakes (8%)
* technology mistakes (4%)


+++
### Software projects in Equinor

* Use **free and open source software** to make Equinor a more competitive, agile and cost-effective organization
 * procurement & software delivery shall evaluate
 * all developed by/for Equinor shall be
 * all development utlize

open source


+++
### Software projects in Equinor

* 4-layer IT architecture
 * Data
 * Business logic
 * API first (— all data exposed by APIs)
 * User interface
* No point-to-point integration
* Cloud ready/enabled
* Self protecting solution – (Zero Trust)


---
### Methodology



+++
### Methodology

* An actual field
 * ... with actual literature
 * ... and experience


+++
### Methodology

* **Push** vs pull
 * leads to congestion
 * lack of testing
 * scope creep
 * no respons to change
 * You ain't gonna need it

+++

![Kanban Push](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/kanban-push.png)

+++

![Kanban Pull](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/kanban-pull.png)



+++
### Methodology

* Push vs **pull**
 * testing is natural part
 * immediate feedback
 * immediate response to change
 * minimal scope creep (*)


+++
### Methodology

Summarizing

* c&c
* push
* waterfall

does not work!


+++
### Methodology

Testing



+++
### Methodology

CI / CD



+++
### Methodology

Summarizing

* agile
 * individuals and interactions
 * working software
 * customer collaboration
 * response to change

We don't do it for fun



---
## PART II



---
#### Technology

* Question: What is the cloud?

+++

![There is no cloud](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/no-cloud.png)



+++
#### Technology

* Microservices


+++
#### Technology

* IaaS
* Containers
 * Docker
 * Kubernetes
 * scalability
 * pay-per-use
* cloud native?


+++
#### Technology

* access control
* Zero trust model


+++
#### Technology

* APIs
 * programming interface
 * how programs communicate with other programs
* GUIs
 * Graphical User Interfaces
 * (mouse and keyboards)
 * (users and screens)


+++
#### Technology

* APIs
 * _API first strategy_
 * _AI ready_


+++
#### Technology

(intermezzo)


+++
##### Machine Learning

* Accuracy
* 99% accurate is good </
* data leakage


+++
#### Technology
