## GIT


![equinor](https://raw.githubusercontent.com/pgdr/talks/master/gitws/eq-git-small.png)

Pål Grønås Drange

_(cc-by-nc-sa 3.0), `git-scm.com`_

---

## Git Workshop

+++

Snapshots

---

### Linear local

`init` `log` `status` `diff` `add` `commit` `reset` `clean` `stash` `tag` `blame` `show` `filter-banch` `bisect`

+++
### Local

`branch` `checkout` `merge` `rebase` `cherry-pick` `reflog`

+++
### Remote

`clone` `remote` `push` `fetch` `pull`


+++
### Git workflow

Repeat:

```
edit myfile
git add myfile
git commit
```


+++
### Git collaboration workflow

Repeat:

```
git pull
edit myfile
git add myfile
git commit
git push
```


+++
### Git branch workflow

Repeat:

```
git checkout -b newbranch
edit myfile
git add myfile
git commit
git checkout master
git merge newbranch
```


+++

showtime

---
### Exercises
+++
Exercise 1, linear local
+++

```
git init
edit README.md
git add
git commit
```

+++

Repeat

```
edit README.md
git diff
git status
git add
git commit
git log  # --oneline --graph
```

+++

Exercise 2, local

+++

branch

```
git checkout -b newbranch
edit README.md
git diff
git status
git add
git commit
git log
git checkout master
git merge newbranch
```

+++

branch, non-trivial merge

```
git checkout -b newbranch
edit README.md
git add
git commit
git checkout master
edit README.md  # different place in file
git add
git commit
git merge newbranch
```

+++

## Exercise 3, conflict

+++

branch, conflict

```
git checkout -b newbranch
edit README.md
git add
git commit
git checkout master
edit README.md  # same line
git add
git commit
git merge newbranch
# CONFLICT
edit file
git commit
```

+++

### Exercise 4, rebase

+++

```
git checkout -b newbranch
edit README.md
git add
git commit
git checkout master
edit README.md  # different place in file
git add
git commit
git checkout newbranch
git rebase master
git checkout master
git merge newbranch
```

### Exercise 5, rebase interactive

+++

```
git rebase --interactive HEADˆˆˆˆ
```

---
### Exercise 6, remotes

+++

```
git remote
git remote add origin git@github.com:username/repo
git remote show origin
git push --set-upstream origin master
```
