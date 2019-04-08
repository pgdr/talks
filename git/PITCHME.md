## GIT


![equinor](https://raw.githubusercontent.com/pgdr/talks/master/itdagene/equinor.png)

Pål Grønås Drange

_(cc-by-nc-sa 3.0), `git-scm.com`_

---

### Getting started



+++
##### About Version Control

* edit and keep track
* collaborate
* centralized vs distributed


+++
##### A Short History of Git

* Speed
* Simple design
* Strong support for non-linear development
* Fully distributed
* Able to handle large projects


+++
##### What is Git?

* Snapshots, not deltas
* Stream of snapshots of filesystem
* (Nearly) everything is local
* Integrity (never corrupt, never loss)
* Three stages
  * modified
  * staged
  * committed

---

## Git intro

+++
### Git intro

```
mkdir project
cd project
git init
```

+++


+++
### Git workflow

Repeat:

```
vim myfile
git add myfile
git commit
```


+++
### Git collaboration workflow

Repeat:

```
git pull
vim myfile
git add myfile
git commit
git push
```


+++
### Git branch workflow

Repeat:

```
git checkout -b newbranch
vim myfile
git add myfile
git commit
git checkout master
git merge newbranch
```


+++

showtime
