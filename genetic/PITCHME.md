## Genetic algorithms

(cc-by-sa 4.0)

---


![Antenna](https://raw.githubusercontent.com/pgdr/talks/master/genetic/antenna.jpg)

---

**A genetic algorithm** is

* an optimization algorithm
* based on evolutionary principles

with a pool of individuals

---

You need three functions to use GAs.

* mutation
* crossover
* fitness

---

### mutation

make a random mutation of an individual

```python
def mutate(ind : Individual) -> Individual:
    pass
```

(GAs with mutation is a form of local random search)

---

### crossover

```python
def crossover(ind1 : Individual, ind2 : Individual) -> Individual:
    pass
```

---

### fitness

```python
def fitness(ind : Individual) -> float:
    pass
```

---

#### live

---

---
```python
def _iterate(pool, mut, cros, fit):
    nextpool = []
    for p in pool:
        nextpool.append(mut(p))
    for i in range(10):
        for j in range(10):
            nextpool.append(cros(pool[i], pool[j]))
    return sorted(list(set(nextpool)), key=fit)[:min(len(pool), len(nextpool))]

def genetic_algorithm(generator, mut, cros, fit):
    pool = [generator() for _ in range(SIZE)]
    for i in range(GENS):
        pool = _iterate(pool, mut, cros, fit)
        if fit(pool[0]) == 0:
            break
    return pool
```

---

---

