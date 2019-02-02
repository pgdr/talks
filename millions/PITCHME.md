## Why Free Software?

(cc-by-sa 4.0)

+++


### Make it easy to build

When putting your software out you need to also make clear and neutral
instructions

---

### Internal network means hidden assumptions
+++
When you build, test and deploy your code on your internal network you have
access to thousands of sweet libraries.

+++

However!  These sweet libraries come with a hidden cost, because they are hidden
assumptions.

+++

It makes your software tightly (and invisibly so) coupled to your internal
infrastructure.

+++

This makes it harder to change your infrastructure, and harder to change your
software.



---

### Why would we give away our precious software for free?

+++

A common misconseption is that free software is free to use.  Especially
software that is designed to solve one company's or customer's need.

+++

Anyone who wants to use the software themselves need to make changes and
bugfixes.

+++

These means that they (most likely) want to contribute back with new features,
new generalizations, new improvements, etc.



---

### Great advertising

+++

When you develop free software you can give a lots of talks!

+++

When recruting developers, you get to point them to code and review practices on
github or lauchpad or wherever you have your code.

+++

If you develop software that students might use, they can download it and test
it even before they start working in your company.







## Licenses

(cc-by-sa 4.0)

---

Go through

* GNU GPL 2 v 3
* GNU AGPL
* GNU LGPL
* MIT
* APACHE
* BSD
* CREATIVE COMMONS
* ODbL

+++

Examples

* GNU GPL 2 (Linux, MediaWiki, Wordpress, +++, ERT, OPM)
* GNU GPL 3 (GCC, GNU, +++, Sunbeam)
* GNU AGPL (Launchpad)
* GNU LGPL (QT, Vorbis*, Segyio)
* MIT (Jenkins, Atom, Compiz, Mono, Ncurses, Node.js)
* APACHE (Android, Apache, Kubernetes, PyCharm)
* BSD (Chromium, D3, Django, Flask, Nginx, Vorbis)
* CREATIVE COMMONS (Wikipedia content)
* Open Database Licence (Norne)

---

### COPYRIGHT

* No license can take away your copyright
* Everything you make is immediately your copyright (caveat employee)
* Licenses are contracts!

+++

### COPYRIGHT

* If you have copyright
  * you can relicense to whatever
* You cannot give away copyright (in Norway you can?)
  * hence, e.g. FSF and ERT ask you to
  * sign a contract allowing them to relicense your code
* FSF owns all GNU code and could therefore upgrade GPL2 to GPL3
* Linux copyrights scattered around, cannot upgrade (won't anyway)

+++

### OPPHAVSRETT TIL ÅNDSVERK

> den som skaper et åndsverk har opphavsrett

> finnes ingen lovbestemmelse vedr. arbeidsgiver

> unntak: datamaskinprogrammer.  opphavsretten går til arbeidsgiveren (§39g)

(Covered under _"Lov om opphavsrett til åndsverk"_)


+++

### COPYLEFT

* Copyleft
* share-alike

concerns _redistribution_ of copyrighted work


---

### GNU General Public License

---

#### GPL 2 states

* copy, modify, and distribute the software
* modifications to software GPL 2
  * must be available under GPL 2
* (with build instructions)

---

##### Tivoization

Suppose that I go ahead and
* make a car running Linux
* only signed software can run on car
* people can get and modify source code
* but not run the modified software on the car

Was it really possible to modify the source code as per GPL 2?

---

##### Tivoization

Richard M. Stallman was annoyed.

Made GNU GPL3

Linus Torvalds says he understands the car manufacturer.

---

#### GPL 3 states

* copy, modify, and distribute the software
* modifications to software GPL 3
  * must be available under GPL 3
* (with build instructions)

+++

GPL3 also contains more
* specific about license compatibility (e.g. apache)
* DRM (tivo)
* explicit patents stuff
  * (cannot deny rights via patents)
* make AGPL explicitly necessary
  * (if software not sent, no distribution necessary)
  * (recall Wordpress)

---

#### AGPL 3 (Affero GPL)

* For network software
* copy, modify, and distribute the software
* derivative work must be redistributed under AGPL
* if the software is used in "web publication"
  * the source code must be made available

---

#### LGPL 3 (Library/Lesser GPL)

* For libraries
* copy, modify, and distribute the software
* derivative work must be redistributed under LGPL
* applications using the library needn't


---

### Non-GPL

---

#### MIT

* Do whatever you like
* Must retain the original license

---

#### Apache 2

* Do whatever you like
* Must retain the original license
* Contains patent stuff

---

#### BSD 3

* Include BSD copyright and license notice
* Do whatever you like

---

### Creative commons

(for content)

+++

* by = attribution
* sa = share-alike
* nc = non-commercial
* nd = no-derivates

_(tivoization is built-in in cc)_

+++

* cc
* cc-by
* cc-sa
* cc-nc
* cc-by-sa-nc
* cc-nd

---

### Open Database Licence

Like cc-by-sa for database content


---


## due diligence

_Using_ open source software often means no warranties!



---

happy coding
