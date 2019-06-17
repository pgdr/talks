# KOMODO

## Pre-komodo

+++

How we ended up where we are with

> `/project/res`

today.

+++

* Where?
* What ?
* Why  ?
* How  ?
* Who  ?

+++

Why per-project Jenkins jobs is an _anti-pattern_ (?)

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

## What is install?

+++

* creates directory structure
* sets permissions
* does not overwrite unless different
* preserves security context
* makes backups
* unlinks if necessary
* etc

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

Run Jenkins Clippy-deploy nightly (or so).

+++

Some issues:

* separate the installation from the source code
 * no tests (need nightly integration tests, but where?)
* this means that when you add a new file, it may and may not be copied
* it's _additive_, meaning that when you rename a file, the old remains


How the software is installed is a part of the development!

+++

Use proper tools (cmake/setuptools/make) to install → testable

Called _installation testing_

How do you test that Jenkins deploy scripts are up-to-date?

+++

And this is how many people do it in Equinor.

> why can't you just put this script up there?

Well, it doesn't scale.


---

## Technical solution

+++

Several parts

* the Komodo _software_
* the Komodo _configuration_
* the Komodo _distributions_ (and how they are made)

+++

Has a `repository.yml` of all software, versions, dependencies, maintainers:

```yml

everest:
  0.6.1:
    source: git
    make: setup.py
    depends:
      - python
      - seba
      - libres
    maintainer: mfane
```

+++

And a "release" is

`2019.06.yml`

```yml
everest: 0.6.1
libres: 2.4.2
python: 2.7.14
```

etc.

+++

So why Komodo?


* Where -- where the install script puts it
* What -- look at `release.yml`
* Why -- ask the maintainer, who is
* Who -- the maintainer as specified in `.yml`
* How -- re-run Komodo

---

## Komodo Release Lifecycle

+++

* Komodos track record
* API → Semver.org
* maintainers' roles and responsibility
* requirements
  * GIT and CI
  * Automatic testing
  * Code review
  * semver
  * Nightly testing against stable/testing/unstable
* bugfix stable
* preparing for new stable


---

## The future

+++

* `/prog/res/komodo`
* Python 3

+++

## Q&A
