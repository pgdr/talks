# KOMODO

## Deploy Is Not Copy

+++

Why Install is so important that we have added it as a separate point in the
architecture contracts.

+++

How we ended up where we are with

> `/project/res`

today.

+++

Why per-project Jenkins jobs is an _anti-pattern_ (?)

+++

Why Komodo was necessary.

+++

* `ert-deploy`
* `FUSD-deploy`
* `libecl-deploy`
* `segyio-deploy`
* `pyDAKOTA-deploy`
* `webportal-deploy`
* `well2seis-deploy`
* `ert-statoil-deploy`
* `fmu-storage-deploy`
* `segyviewlib-deploy`
* `Seba-WPRO-deploy-joaho`
* `libecl-shared-opm-deploy`
* `libecl-static-opm-deploy`
* `fmu-storage-deploy-client`
* `ert-statoil-deploy-setuptools`

+++

* `PM-deploy`
* `sunbeam-deploy`
* `pyDAKOTA-deploy`
* `Sentry-deploy-V2-PROD`
* `ERT-deploy-pgdr-branch`
* `Sentry-deploy-V1-STAGE`
* `Sentry-deploy-V2-STAGE`
* `ERT-deploy-ariel-branch`
* `opm-parser-deploy-joaho`
* `ERT-upstream-v1.7-deploy`
* `ERT-upstream-v1.8-deploy`
* `ERT-deploy-jpb-branch-RH6`
* `FUSD-deploy_TO_BE_DELETED`
* `ERT-deploy-alin-branch-RH6`
* `ERT-deploy-upstream-branch`
* `ERT-deploy-joaho-branch-RH6`
* `segyviewlib-deploy_TO_BE_DELETED`
* `ERT-upstream-master-nightly-deploy-RH6_TO_BE_DELETED`


+++

It might work when #devs + #projs <= 10.

It does not scale.

---

## CP vs install

+++

There is an `install`

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


+++

```make
Makefile:
install:
    # Documentation
    $(MAKE) -C docs install
    # Configuration files
    install -d $(DESTDIR)/etc/netctl/{examples,hooks,interfaces}
    install -m644 docs/examples/* $(DESTDIR)/etc/netctl/examples/
    # Libs
    install -d $(DESTDIR)/usr/lib/netctl/{connections,dhcp}
    install -m644 src/lib/{globals,interface,ip,rfkill,wpa} $(DESTDIR)/usr/lib/netctl/
    install -m644 src/lib/connections/* $(DESTDIR)/usr/lib/netctl/connections/
    install -m644 src/lib/dhcp/* $(DESTDIR)/usr/lib/netctl/dhcp/
    install -m755 src/lib/{auto.action,network} $(DESTDIR)/usr/lib/netctl/
    # Scripts
    ...
```

---

## Installation

`install` more suited to `cp`

a different kind of install

+++

### Jenkins deploy

So let's install, e.g. Clippy.

+++

I make a Jenkins job that
```
cp Clippy/bin/clippy    /project/res/bin  # or?
cp Clippy/python/clippy /project/res/lib  # or?
# don't forget
cp Clippy/data/the_important_file.yml /project/res/share  # or?
```

+++

Run Jenkins Clippy-deploy nightly (or so).

+++


Some issues:

* separate the installation from the source code

+++

Some issues:

* separate the installation from the source code
 * no tests (need nightly integration tests, but where?)

+++

Some issues:

* separate the installation from the source code
 * no tests (need nightly integration tests, but where?)
* this means that when you add a new file, it may and may not be copied

+++

Some issues:

* separate the installation from the source code
 * no tests (need nightly integration tests, but where?)
* this means that when you add a new file, it may and may not be copied
* it's _additive_, meaning that when you rename a file, the old remains

+++

How the software is installed is a part of the development!

+++

Use proper tools (cmake/setuptools/make) to install → testable

Called _installation testing_

How do you test that Jenkins deploy scripts are up-to-date?

+++

And this is how many people do it in Equinor.

> why can't you just put this script up there?

Well, it doesn't scale.


+++

## Debian with 30k packages.

+++

* don't accept anything but "perfect"
* it's not so hard
* should we accept anything less?
 * Because it's difficult?  It's not.
 * Because it takes time?  It doesn't.

---

## Deploy to `/project/res`

+++

Used to be de-facto deploy

(And still is.)

`cp this` and `cp that`
* by different users, with different permissions.

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

+++

* After discussing with Joakim and Jean-Paul
* brain-storming with Jørgen
* try doing it properly; Komodo demands installable.

**Step 1** getting into Komodo: install script in the source tree.

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

Komodo wasn't meant as a replacement for `/prog/sdpsoft` or RHEL distribution.


---

# Q/A
