# KOMODO
## Maintainer course

+++

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

## Komodo

+++

Komodos track record

* Since 2018-01
  * no outages
  * no breaks due to incompatible versions

+++

Several parts

* the Komodo _software_
* the Komodo _configuration_
* the Komodo _doctrine_

---

## The Komodo software

+++

* Builds an atomic deploy with all dependencies included
* The build recipe is given in a Komodo configuration with explicit versions
* Openly available at [https://github.com/equinor/komodo]

---

## The Komodo configuration

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

## The Komodo doctrine

+++

API → Semver.org

* API is important
* semver
  * major.minor.micro (break, backwards compatible, no change in API)
  * semver ensures communication of API
  * semver makes the developer think

+++

Maintainers' roles and responsibility
* Making sure that packages are fully functioning in every release
* Deal with bugs and incompatibility issues in good time before they get to stable
* Schedule and test new releases of a package
* Communicate with users of the package

+++

Incompatible packages
* Two packages are incompatible if they:
  * depend on different versions of same lib
  * if one package in komodo breaks its API
* Incompatibilities are dealt with on scenario by scenario basis
  * minimal impact on FMU,
  * a package can be frozen for a limited time if one presents a plan to
    mitigate
  * We cannot stop the komodo train
  * worst case scenario, a package will not make it to the next stable

+++

Requirements to enter Komodo
* GIT and CI
* Automatic testing
* Code review
* Semantic versioning
* Nightly testing against stable/testing/unstable

---

## Komodo examples

+++

Preparing for new stable

+++

Bugfix stable

+++

---

## The future

+++

* `/prog/res/komodo`
* Python 3

---

## Q&A
