### Inhouse Software Development

+++

Agenda

* Why in-house development
  * domain knowledge
  * close with users
  * keep knowledge ...
  * speed of development
  * Main benefit from softw. dev. is the knowledge
* Software engineering is unlike everything
  * we never solve the same thing twice
  * completely different project management
    * leaders do not understand the complexity
    * leaders do not believe developers' estimates
    * software projects are more like research projects than trad projects
* Some drawbacks in large corporations
  * governing (controlling the creatively unpredictable)
  * bad management
  * bad project lead believing they can
  * bad strategies coming from above
    * ... a reverse correlation between technical competence and position in ladder
  * non-developers doing development without understanding
* Open development
  * Open source
    * what is it
    * why we do it
  * Open data
    * not so easy as people would like
    * increase understanding of facts
    * necessary for open standards
    * we are in a better position if
      * students
      * vendors
      * contractors know and understand the data and facts
* Programmer's oath

---

### Free software (open source?)

>_All software developed by or for Equinor shall be made open source unless …_




+++
### Free software

> Hvorfor gi noe bort gratis som vi har brukt millioner på å utvikle?!

_(cc-by-sa 4.0)_

+++
### Free software

1. What is open source software?
2. Why do we use it?
3. Why do we give away code for free?

---
### History (before 1984)

* Software was written and distributed
* Different architectures
* Code was considered _«public domain»_
* 1975—85: Code is copyrightable; proprietary code

+++
### History (1980s)

* Richard Stallman started GNU Project
* —— wrote GNU Manifesto, later
 * Free Software Foundation
 * GNU General Public License (GPL)


+++
### History (1990s)

> I'm doing a (free) operating system (just a hobby, won't be big and
> professional like gnu)

* Linux (1991)
* Linux lisensiert under GPL (1992)

+++
### History (1990s)

> OSS poses a direct, short-term revenue and platform threat to
> Microsoft, particularly in server space. Additionally, the intrinsic
> parallelism and free idea exchange in OSS has benefits that are not
> replicable with our current licensing model and therefore present a
> long term developer mindshare threat.

— Microsoft, Halloween documents (1998)

+++
### History (1990s)

Microsoft released two attacks on the OSS process

* _"fear, uncertainty and doubt"_ (FUD)
* _"embrace, extend, extinguish"_ (EEE)


+++
### Today

* 500 out of 500 supercomputers
* The majority of Microsoft Azure,
 * Google and Amazon
 * Facebook and Twitter and Instagram
 * LinkedIn and eBay and IBM
* Microsoft IoT
* 80% of the world's phone market runs Android
* Toyota, Audi, Ford, Mazda, Subaru, Mercedes..


---
### Q

What is free software?

+++
### Free software

The freedom to

* **run the program** as you wish, for any purpose
* **study how the program works**, and change it
* **redistribute copies** so you can _help others_
* **distribute copies** of your modified versions


+++
### Q

What is open source?


+++
### Open source

1. Free Redistribution
2. Source Code
3. Derived Works
4. Integrity of The Author's Source Code
5. No Discrimination Against Persons or Groups
6. No Discrimination Against Fields of Endeavor
7. Distribution of License
8. License Must Not Be Specific to a Product
9. License Must Not Restrict Other Software
10. License Must Be Technology-Neutral


+++
### Q

"Free software" vs "open source"?

* free: ideological
* open: practical



+++
### Q

But is it really free?

+++

is it free?

* Free as in "free speech"
* not necessarily free as in "free beer"


+++
### Q

Can Open Source software be used for commercial purposes?


+++

Money is "irrelevant"



+++
### Q

What is the legal basis of OSS licenses?


+++
### Opphavsrett Til Åndsverk

> den som skaper et åndsverk har opphavsrett
>
> unntak: datamaskinprogrammer.  opphavsrett går til arbeidsgiveren

_(«Lov om opphavsrett til åndsverk»)_




+++
### Copyright

* Free software is based on the copyright law
* Everything you create is your copyright _(opphavsrett til åndsverk)_
* Licenses are contracts giving more rights



+++
### Free software

Two main classes of licenses:

* share-alike, _"copyleft"_
* anything you like, _"permissive"_


(requirements are only for distributing!)


+++
### Examples

* GNU GPL 2 (Linux, MediaWiki, Wordpress, +++)
* GNU GPL 3 (GCC, GNU, +++)
* GNU AGPL (Launchpad)
* GNU LGPL (QT, Vorbis, Segyio)
* MIT (Jenkins, Atom, Compiz, Mono, Node.js)
* APACHE (Android, Apache, Kubernetes, PyCharm)
* BSD (Chromium, D3, Django, Flask, Nginx, Vorbis)
* Creative Commons (Wikipedia content)
* Open Database Licence (OpenStreetMaps, ...)



+++
### GNU General Public License


+++
#### GPL 2/3 states

* copy, modify, (re)distribute
* changes must be under GPL 2/3


+++
#### AGPL 3 (Affero GPL)

* copy, modify, (re)distribute
* changes must be under AGPL
* if the software is served as "web publication"
 * the source must be distributed




+++
#### LGPL 3 (Library/Lesser GPL)

* copy, modify, (re)distribute
* changes must be under LGPL
* software using LGPL do not need be



+++
#### BSD, MIT & Apache

* BSD, MIT & Apache
 * Do as you wish
 * Retain license
* Apache
 * Some patent stuff


+++
### Creative commons

(for content)

* by = attribution
* sa = share-alike
* nc = non-commercial (non-free)
* nd = no-derivates (non-free)


+++
### Open Database Licence

Like cc-by-sa, but for "data"

+++
### Q

Which Open Source license should I choose to release my software under?



+++
### Q

Which Open Source license is best?



+++
### Q
Do I need to be afraid of open source?



+++
### Q

Do I need to give away my software if I use open source?


---
### Why, Equinor!?


* Three categories
 * company / shareholders
 * project / product
 * team / developers



+++
##### (company) commoditize complementaries

* demand of a product
* inverse of price for complementary products


+++
##### (company) risks inherent in closed dev

* Greatly increased costs
* Inability to use improvements
* The release of a competing OSS project
* Questions about the openness of Equinor


+++
##### (company) Advertising and recruitment

* can show _«real development»_
* talks at conferences, workshops, universities
 * share knowledge
 * competence lift,
 * give something back


+++
##### (company) Openness yields trust

* increased confidence to the IT community
* One of Equinor's core values (**åpenhet**)
 * best way IT can be open
* open infrastructure (Kerckhoffs' principle)


+++
##### (project) Reduce product development time

* If you are based on proprietary software
 * ignore lots of knowledge and solved problems

> standing on the shoulders of giants



+++
##### (project) increased quality

* if you claim to be free/open
 * README
 * up-to-date description of product
 * instruction manual
 * installation manual
 * automatic tests

+++
##### (project) given enough eyeballs

* in open code (empirical and anecdotal)
 * fewer bugs
 * more tests
* we regularly receive feedback from externals
 * bugs
 * improvements
 * new functionality


+++
##### (team) complete focus on development

* open source software development has
 * GitHub
 * Travis
 * CircleCI
 * AppVeyor
 * Codacy
 * ...
* and easier access to the code(!)


+++
##### (developer) every patch and review is a ☆

* every
 * patch,
 * commit,
 * review a star in their resume
* we rarely get to show our work


+++
##### (developer) Contribute back

Create a
* pip package
* Debian package
* RedHat package
* npm package

Ubuntu? — you have completed the game!

> `apt install my_pkg`

---






+++
### Q

What are "contributor agreements"? Are they like open source licenses?


+++
### Q

Can I write proprietary code that links to a shared library that's open source?



+++
### Q
How do I make money if anybody can sell my code?



+++
### Q
How is OSS typically developed?


+++
### Q

Isn't OSS developed primarily by inexperienced students?





+++
### Q
Are OSS licenses legally enforceable?

+++
### Q
Is it more difficult to comply with OSS licenses than proprietary licenses?


+++
### Q

Doesn't hiding source code automatically make software more secure?


+++
### Q
Does ~~the DoD~~ Equinor already use open source software?



+++
### Q
Is there any quantitative evidence that open source software is better than proprietary software?






---

Happy coding

---
---
---
---
### due diligence

* _Bruk_ av fri programvare
 * ingen garantier
 * ingen support
 * ingen krav til noe


+++
### Testing

* Har pakken (automatiserte) tester?
* Klarer du å kjøre dem, og går alle testene gjennom?


+++
### Design

Er
* pakken veldokumentert og API-et veldesignet?
* forventninger til brukere dokumentert?


+++
### Kodekvalitet

* Er kodekvaliteten grei?
* Ser koden ut som noe du kunne tenke deg å debugge?


+++
### Bug-database

* Er det mange åpne bug-rapporter (over lang tid)?
* Er det mange lukkede bug-rapporter (nylig)?


+++
### Vedlikehold

* Er pakken "ferdig", hvis ikke, når var siste commit?
* Er det et aktivt (og sunt) utviklingsmiljø?



+++
### Bruk

* Er det mange som bruker denne pakken?
* Er det noen seriøse som avhenger av denne pakken?


+++
### Sikkerhet

* Kommer pakken til å håndtere rådata, og tåler den ondsinnet input?
* Har den noen innslag i _National Vulnerability Database_?


+++
### Lisensiering

* Har koden en kjent lisens?
* Passer lisensen med dine behov?


+++
### Avhengigheter

* Avhenger denne pakken på andre pakker?
* Husk at den kan introdusere nye avhengigheter senere!

---

EOF
