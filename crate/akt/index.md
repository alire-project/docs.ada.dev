---
layout: crate
crate: "akt"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-keystore"]
tags: ["security",
"storage",
"nosql"]
version: "1.3.3"
short_description: "Ada Keystore Tool"
dependencies: [{crate: "keystoreada", version: "^1.3.3"},
{crate: "utilada", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/https/jenkins.vacs.fr/Bionic-Ada-Keystore.svg)](http://jenkins.vacs.fr/job/Bionic-Ada-Keystore/)
[![Test Status](https://img.shields.io/jenkins/t/https/jenkins.vacs.fr/Bionic-Ada-Keystore.svg)](http://jenkins.vacs.fr/job/Bionic-Ada-Keystore/)
[![codecov](https://codecov.io/gh/stcarrez/ada-keystore/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-keystore)

# Overview

AKT is a tool to store and protect your sensitive information and documents by
encrypting them in secure keystore (AES-256, HMAC-256).

Create the keystore and protect it with a gpg public key:
```
   akt create secure.akt --gpg <keyid> ...
```

Store a small content:
```
   akt set secure.akt bank.password 012345
```

Store files, directory or a tar file:
```
   akt store secure.akt notes.txt
   akt store secure.akt contract.doc
   akt store secure.akt directory
   tar czf - . | akt store secure.akt -- backup
```

Edit a content with your $EDITOR:
```
   akt edit secure.akt bank.password
   akt edit secure.akt notes.txt
```

Get a content:
```
   akt get secure.akt bank.password
   akt extract secure.akt contract.doc
   akt extract secure.akt -- backup | tar xzf -
```

## Documents

* [Ada Keystore Guide](https://ada-keystore.readthedocs.io/en/latest/) [PDF](https://github.com/stcarrez/ada-keystore/blob/master/docs/keystore-book.pdf)



