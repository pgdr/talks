# API
## =
# Versions
## =
# Software

---
## Analogy time
### mathematical papers

+++

* Definitions
* Lemmata
* Theorems
* Corollaries

+++

* Definitions = Types
* Lemmata = Helper functions
* Theorems = Main functions
* Corollaries = Utilities using Theorem

Text = documentation

Proofs = implementation

---

## The inherent complexity of versions

+++

Version Selection is NP-complete.

+++

By reduction from 3-SAT.

* Clause → package with three versions
* Variable → package with two versions
* Formula → package depending on all clauses

"QED"!

---

## Version selection complexity for developers

+++


Suppose `C` → `B` → `A` and also `C` → `A`

(e.g. `Everest` → `fmu_postprocessing` → `Res`)

+++

Suppose `Res` breaks the API

(E.g. from `2.3` and `3.0`)

There is now a **demarcation**

+++

* `fmu_postprocessing` must make a choice
 * use `Res 2.3` or `Res 3.0`?
* `Everest` depends on `Res 2.3`

+++

Python 2 v 3 anyone?

+++

### Additional work

The more major.minor branches we have

The more branches we need to backport to



---

## Don't touch it!

+++

Do you consider introducing a new symbol. Stop. Don't.

Exercise 1.

Fix the issue without touching the API.  API changes ripple for years.

+++

Annoying to get around an API that

* you didn't design and
* that is full of legacy,

but that's what we have.

+++

Implementation = bug scale = 1 week

API = Design = years

+++

Such decisions take as long time to make, review and commit as the bug fixes.

+++

E.g. we renamed res to ert more than one year ago ~800 commits ago ... we still
have users.

---

## Legal issues

+++

_Oracle America, Inc. v. Google, Inc._

+++

Inconclusive.

---

## Q∕A

+++

* Why do we keep changing the API?
* What do we think when we introduce new symbols?
* How to stop introducing new everlasting symbols?
* Do we agree that the lifetime should dictate the time we use to develop?
