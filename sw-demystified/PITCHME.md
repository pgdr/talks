## SW dev demystified

+++
## SW dev demystified

> Mysticism is the practice of religious ecstasies together with whatever
> ideologies, ethics, rites, myths, legends, and magic may be related to them.

+++
## SW dev demystified

> It may also refer to the attainment of insight in ultimate or hidden truths,
> and to human transformation supported by various practices and experiences.


+++
## Game of Life

* Each living cell with
 * one or no neighbors dies, as if by solitude
 * four or more neighbors dies, as if by overpopulation
 * two or three neighbors survives
* Each dead cell with
 * three neighbors becomes populated


+++
![Glider](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/gol-glider.gif)


+++
![Cannon](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/cannon.gif)


+++
![Spaceships](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/spaceships.gif)


+++
![GOL machine](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/gol.gif)


+++
![Turing machine](https://raw.githubusercontent.com/pgdr/talks/master/sw-demystified/assets/turing.png)


+++
### Power

Turing completeness

* `Y=λf.(λx.f(xx))(λx.f(xx))`
* programming languages
 * C++
 * Python
 * ...

Can run _any_ program


+++
### software dev is complex


+++
### software dev is complex

 ... but billions of CPUs run millions of instructions per second


+++
### software dev is complex

there is not a single thing today not involving an instruction written by a
developer


+++
### software dev is complex

> Access to developers is a bigger threat to business success than access to
> capital.


+++
### software dev is complex

 ... but we have methods, best practices and experience



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



+++
### Software projects

* process mistakes (45%)
* people mistakes (42%)
* product mistakes (8%)
* technology mistakes (4%)


+++
### Software projects in Equinor

* Use **free and open source software** to make Equinor a more competitive, agile and cost-effective organization
 * procurement and software deliveries shall evaluate
 * all developed by/for Equinor shall be open source
 * all development utlize open source technologies


+++
### Software projects in Equinor

* 4-layer IT architecture
 * Data
 * Business logic
 * API first (all data/(f) exposed by APIs
 * User interface (UI/UX)
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
insert pic of kanban push board


+++
### Methodology

* Push vs **pull**
 * testing is natural part
 * immediate feedback
 * immediate response to change
 * minimal scope creep (*)


+++
insert pic of kanban pull board



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
* Answer: Someone elses machine


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
