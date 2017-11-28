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

Suppose I have a document `doc`.
