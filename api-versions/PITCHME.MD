# API=Versions=Software

---
# Analogy time
## mathematical papers

+++

* Definitions
* Lemmata
* (Propositions)
* Theorems
* Corollaries
* (and proofs)
* (and text)

---

# The inherent complexity of versions

+++

Version Selection is NP-complete.

+++

Suppose C → B → A and also C → A

(e.g. Everest → fmu_postprocessing → Res)

+++

Suppose Res breaks the API (e.g. changing namespace from res→ert).

(E.g. from 2.3 and 2.4)

+++

* fmu_postprocessing must make a choice; use Res 2.3 or Res 2.4?
* Everest depends on Res 2.3.  (Possibly because of Seba.)



---

# Don't touch it!

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

# Legal issues

+++

_Oracle America, Inc. v. Google, Inc._

+++

Inconclusive.

---

# Q∕A

+++

* Why do we keep changing the API?
* What do we think when we introduce new symbols?
* How to stop introducing new everlasting symbols?
* Do we agree that the lifetime should dictate the time we use to develop?
