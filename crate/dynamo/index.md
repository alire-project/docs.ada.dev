---
layout: crate
crate: "dynamo"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/dynamo"]
tags: ["uml",
"generator",
"database"]
version: "1.3.0"
short_description: "Dynamo Ada Generator"
dependencies: [{crate: "ado_all", version: "2.3.0"},
{crate: "ado_mysql", version: "2.3.0"},
{crate: "ado_postgresql", version: "2.3.0"},
{crate: "ado_sqlite", version: "2.3.0"},
{crate: "elada", version: "^1.8.5"},
{crate: "libgpr", version: "*"},
{crate: "security", version: "^1.4.1"},
{crate: "serverfaces", version: "1.5.0"},
{crate: "servletada", version: "^1.6.0"},
{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_xml", version: "^2.5.0"},
{crate: "xmlada", version: "*"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/https/jenkins.vacs.fr/Bionic-Dynamo.svg)](https://jenkins.vacs.fr/job/Bionic-Dynamo/)
[![Test Status](https://img.shields.io/jenkins/t/https/jenkins.vacs.fr/Bionic-Dynamo.svg)](https://jenkins.vacs.fr/job/Bionic-Dynamo/)
[![codecov](https://codecov.io/gh/stcarrez/dynamo/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/dynamo)
[![Download](https://img.shields.io/badge/download-1.3.0-brightgreen.svg)](https://download.vacs.fr/dynamo/dynamo-1.3.0.tar.gz)
[![License](https://img.shields.io/badge/license-APACHE2-blue.svg)](LICENSE)
![Commits](https://img.shields.io/github/commits-since/stcarrez/dynamo/1.3.0.svg)

This Ada05 application is a code generator used to generate
an Ada Web Application or database mappings from hibernate-like
XML description, YAML doctrine model or UML models.  It provides various commands for the
generation of a web application which uses the Ada Web Application framework
(https://github.com/stcarrez/ada-awa/).
