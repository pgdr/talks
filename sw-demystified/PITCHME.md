## Software development demystified


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

* is extremely complex
* is the formalization of ideas
* needs to be 100% correct or else it crashes
 * or even worse, it doesn't


+++
### Software development

* is extremely complex

 ... but billions of CPUs run millions of instructions per second


+++
### Software development

there is not a single thing today not involving an instruction written by a
developer

#### digitalization = it


+++
### Software development

 ... but we have methods, best practices and experience

_(backed by empirical evidence)_


+++
### Software development

* Why does it work?
 * it's a profession


+++
### Software development

* we have
 * education
 * experience
 * methods, best practices
* we also have
 * responsibility
 * trust


+++
### Software development

> Access to developers is a bigger threat to business success than access to
> capital.

In fact,

> People are not your most important asset. The right people are.


+++
### Software development

The waterfall model

* Requirements
* Design
* Implementation
* Validation
* Maintenance

+++
### Software development

The waterfall model is broken

* don't know exactly what their requirements are
* not aware of future difficulties
* makes changes difficult
* excludes the client and/or end user
* delays testing until after completion
* US DoD have a stated preference
 * encourages evolutionary acquisition
 * iterative and Incremental Development

+++
### Software development

There is no silver bullet to software development

* agile
* scrum
* lean

+++
### Software development

Agile manifesto

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
* Cloud ready/enabled (with no trust)


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

---
#### Technology

* Question: Why cloud?

* scalability
* pay-per-use

---
#### Technology

* Question: What is the cloud for Equinor

OMNIA is our MS Azure configuration

* OMNIA data
* OMNIA apps
* OMNIA aurora
* OMNIA radix

+++
#### Technology

* IaaS
 * pure cloud (just someone else's computer)
* PaaS
 * a method of delivering a capability (application deployment, hosting..)

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
  * aka machine learning

+++
##### Machine Learning

Example: Recall

+++
##### Machine Learning

Machine learning is:

* software engineering +
* statistics

* Accuracy
* 99% accurate is good (or ... ?)
* data leakage


+++
#### Summary

* Cloud is someone else's computer
* Cloud is treated as a "meta-computer"
* GUIs are not the future, APIs are
* Machine learning (AI) is software engineering with statistics using APIs

+++
#### Summary

* Software engineering is a complex field
 * need an education, need experience
* Software projects **are different**, not c&c
* Agile is not for fun
 * nor is it lean or anything else you hear
