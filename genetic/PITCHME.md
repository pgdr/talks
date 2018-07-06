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
def mutate(ind: Individual) -> Individual:
    pass
```

(GAs with mutation is a form of local random search)

---

### crossover

```python
def crossover(ind1: Individual, ind2: Individual) -> Individual:
    pass
```

---

### fitness

```python
def fitness(ind: Individual) -> float:
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
    return sorted(list(set(nextpool)), key=fit)[:len(pool)]

def genetic_algorithm(generator, mut, cros, fit):
    pool = [generator() for _ in range(SIZE)]
    for i in range(GENS):
        pool = _iterate(pool, mut, cros, fit)
    return pool
```

---

---

The Surprising Creativity of Digital Evolution: A Collection of Anecdotes from
the Evolutionary Computation and Artificial Life Research Communities

---

![Inheritance](https://raw.githubusercontent.com/pgdr/talks/master/genetic/inheritance.png)

---

![Locomotion](https://raw.githubusercontent.com/pgdr/talks/master/genetic/locomotion.png)

---

![Locomotion2](https://raw.githubusercontent.com/pgdr/talks/master/genetic/locomotion2.png)

---

![Pole-vault](https://raw.githubusercontent.com/pgdr/talks/master/genetic/pole-vault.png)

---

![Collision detection](https://raw.githubusercontent.com/pgdr/talks/master/genetic/collision-detection.png)


---

[Walking gaits](https://youtu.be/H6OB1E8NsLw?list=PL5278ezwmoxQODgYB0hWnC0-Ob09GZGe2)

---

[No claws](https://youtu.be/_5Y1hSLhYdY?list=PL5278ezwmoxQODgYB0hWnC0-Ob09GZGe2)

---
