# KOMODO

## Deploy Is Not Copy

+++

Why Install is so important that we have added it as a separate point in the
architecture contracts.

+++

How we ended up where we are with `/project/res` today.

+++

Why per-project Jenkins jobs is an anti-pattern.

+++

Why Komodo is necessary.

---

## CP vs install

+++

First, since not all are experience Linux/UNIX

there is actually an `install`

command that might be interesting,

which is like `cp`, but

+++

* creates directory structure
* sets permissions
* does not overwrite unless different
* preserves security context
* makes backups
* unlinks if necessary
* etc

(perhaps something to add to Everest)


---

## Installation

So while `install` is an improvement over `cp` it's a different kind of install
I want to talk about.

The purpose of installation of a project is to convert the source tree into
executables and libraries, and making available extra files.

(Please read `man hier`, although old, still valid.)


---

### Jenkins deploy

So let's install my software, e.g., Clippy.  (A celebration for the GitHub
acquisition.)

+++

I make a Jenkins job that
* `cp Clippy/bin/clippy /project/res/bin` (or somewhere else?)
* `cp Clippy/python/clippy /project/res/lib` (or somewhere else?)

Oh, and don't forget
* `cp Clippy/data/the_important_file.yml /project/res/share` ?

+++

Run Jenkins deploy-clippy nightly (or so).

+++

Some issues:

* separate the installation from the source code
** no tests (need nightly integration tests, but where?)
* this means that when you add a new file, it may and may not be copied
* It's _additive_, meaning that when you rename a file, the old remains

+++

How the software is installed is a part of the development!

When we use proper install tools (cmake/setuptools/make) to install, we put the
install responsibility in the source tree, and make it possible to test.

This is called _installation testing_ and can be done on Travis by a simple
install before tests are run.

How do you test that Jenkins deploy scripts are up-to-date?

+++

However, if you are a maintainer of one or two, or maybe five applications, this
may work.  But if you are responsible for 10 or more, it will not.  It simply
does not scale.

+++

And this is how many people do it in Equinor.  They say, why can't you just put
this script up there?

Well, it doesn't scale.


+++


Take Debian with 30k packages.

They do not accept anything but "perfect".  And is perfect so hard?

No, it's not so hard.  Write a proper (short, viz jokva) `setup.py` script.

Should we accept anything less than perfect?  Why?

Because it's difficult?  It's not.

Because it takes time?  It doesn't.

We shouldn't accept being mediocre.  There's no reason.

---

## Deploy to `/project/res`

+++

That was the way deploy to `/project/res` used to be when jokva and I started.

(And still is.)

Lots of files where copied into place, by different users, with different
permissions.

+++

* Where

+++

* Where
* What

+++

* Where
* What
* Why

+++

* Where
* What
* Why
* How

+++

* Where
* What
* Why
* How
* Who

---

## Enter Komodo

After discussing with Joakim and Jean-Paul I brain-stormed with Jørgen to find
alternative ways.  We discussed several ideas, and together with Jean-Paul
agreed that we would be allowed to spend some time on trying.

As you might know, Komodo demands that your software is installable.

Hence, step 1 for getting something into Komodo is to make an install script in
the source tree.

+++

Decided to make releases (like Debian/Ubuntu)

+++

Has a `repository.yml` of all software, versions, dependencies, maintainers:

```yml

everest:
  0.3.5:
    source: git
    make: setup.py
    depends:
      - python
      - seba
      - libres
    maintainer: pgdr@equinor.com
```

+++

And a "release" is

`2018.03.yml`

```yml
everest: 0.3.5
libres: 2.3.0
python: 2.7.14
```

etc.

+++

This solves


* Where -- where the install script puts it
* What -- look at `release.yml`
* Why -- ask the maintainer, who is
* Who -- the maintainer as specified in `.yml`
* How -- re-run Komodo

---

# Discussions

+++

The two roles of Komodo

* installation improvement
* actually fixing some issues with the current

+++

Prior to Komodo, not every project _was installable_.

In that way, Komodo serves as a springboard

+++

Komodo was meant to replace `/project/res` deploy for

* Ert,
* Everest,
* segyio,
* ?

needed for running on cluster

+++

Do we want to support more than just the regular "run this on the cluster"
software?

Komodo wasn't meant as a 


---

# Q/A
