### Blockchain

(cc-by-sa 4.0)

---

#### Outline

Part I
* Public key cryptography
* Byzantine problem
* Satoshi Nakamoto
* Hashes
* Transactions

...
+++

#### Outline

Part II
* Block
* Chain
* Consensus

...
+++

#### Outline

Part III
* Stockchain | Air Block'n'Block
* Permissions
* Non-PoW: PoS, PoC, PoA, PoSV
* Insurance and cost

---

### Public key cryptography

* Consider Alice & Bob
* Alice has two keys, pk~A~, sk~A~
* and Bob has two keys, pk~B~, sk~B~
* and everybody knows pk~A~, pk~B~
public keys, and secret keys

+++

Using sk~A~, Alice can _sign_ a message M (or hash(M))
* to obtain a signed message (M, sign^M^~A~)
* with property that people can verify, using pk~A~
* that M was signed by Alice

> verify( (M, sign^M^~A~), pk~A~ )

+++

If verify( (M, sign^M^~A~), pk~A~ ), then
* no tampering of M
* non-repudiation (no denying)
* guarantee that A approves of M

(unless sk~A~ is compromised)




---

### The Byzantine Problem

+++

Explain the Byzantine Problem

+++

Conclusion:
* Impossible to agree over an unreliable ling
* (e.g. TCP cannot guarantee state consistency)

---

### Satoshi Nakamoto

+++

Suppose you have a document `doc`.

How can you share `doc` with Alice or Bob?

Due to the invention of the Internet, it's easy!

+++

Suppose you have a document `doc`.

How can you _give ownership_ of this `doc` to Alice or Bob?

Promise it's hers?

+++

Suppose you have a document `doc`.

* ... and you _sell_ this document to Alice for $100.
* ... behind her back, you sell it to Bob for $100.

This is called _double-spend_.

+++

Solution: A _central authority_

* A central authority can verify the rightful owner
* can assist in a sale, stopping any attempt of double-spend

+++

Solution: A _central authority_

* After the financial collapse,
* the central authorities produced millions of docs,
* which made Alice doubt the value of her $100 acquired doc

+++

Trust/no trust: A _central authority_

* Slow
* Hackable
* Corruptible
* Excluding
* ...

+++

2 months later, _Satoshi Nakamoto_ published

> Bitcoin: A Peer-to-Peer Electronic Cash System
>
> (Oct 2008)

Solved _double-spend_ and _no CA_



---

#### Hashes

+++

##### Hash functions in programming

+++

In Java/Python/ACMELang, a `hash` function is a function
* takes an object
* outputs a number
* properties
  * fast
  * exact (reproducible)
  * `hash(obj) != != hash(obj')` (very different)

+++

##### Cryptographic hash functions

+++

A cryptographic hash function is a function (e.g. `md5`, `sha256`)
* deterministic
* fast
* unpredictable (one-way)
* changes in input gives
  * completely, and
  * unpredictable changes in output
  * (avalanche effect)
* infeasible to invert

+++

* `sha('hello') = 5891b5b`
* `sha('hallo') = 622cb33` (avalanche)
* `sha(' ??? ') = 5891b5b` (non-invertible)

(_hexadecimal is `0123456789abcdef`_)

+++

So suppose we ask Alice:

* find an integer _n_ s.t.
  * `sha('hellon') = 0???`.
  * probability: 1/16

+++

So suppose we ask Alice:

* find an integer _n_ s.t.
  * `sha('hellon') = 00???`.
  * probability: 1/256

+++

So suppose we ask Alice:

* find an integer _n_ s.t.
  * `sha('hellon') = 00000???`.
  * probability: 1M^-1^

+++
