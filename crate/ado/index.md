---
layout: crate
crate: "ado"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-ado"]
tags: ["database",
"uml",
"sql"]
version: "2.3.0"
short_description: "Ada Database Objects (Core library)"
dependencies: [{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_xml", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/https/jenkins.vacs.fr/Ada-ADO.svg)](https://jenkins.vacs.fr/job/Ada-ADO/)
[![Test Status](https://img.shields.io/jenkins/t/https/jenkins.vacs.fr/Ada-ADO.svg)](https://jenkins.vacs.fr/job/Ada-ADO/)
[![codecov](https://codecov.io/gh/stcarrez/ada-ado/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-ado)
[![Documentation Status](https://readthedocs.org/projects/ada-ado/badge/?version=latest)](https://ada-ado.readthedocs.io/en/latest/?badge=latest)

Ada Database Objects is an Ada05 library that provides
object relational mapping to access a database in Ada05.
The library supports Postgresql, MySQL, SQLite as databases.
Most of the concepts developped for ADO come from the Java Hibernate ORM.

The ORM uses an YAML, XML mapping file or an UML model, a code generator and a runtime library
for the implementation.  It provides a database driver for [Postgresql](https://www.postgresql.org/),
[MySQL](https://www.mysql.com/) and [SQLite](https://www.sqlite.org/).  The ORM helps your
application by providing a mapping of your database tables directly in the target programming
language: Ada05 in our case.  The development process is the following:

  * You design your database model either using a UML tool or by writing a YAML or XML description,
  * You generate the Ada05 mapping files by using the [Dynamo](https://github.com/stcarrez/dynamo) code generator,
  * You generate the SQL database tables by using the same tool,
  * You write your application on top of the generated code that gives you direct and simplified access to your database.

![ADO Development model](https://github.com/stcarrez/ada-ado/wiki/images/ado-orm.png)

You need at least one of these databases (or all of then).  The configure script will now
fail if no supported database was found.  Check the [Database Drivers](#database-drivers)
section to install them and run the configure again after the installation.

# Documentation

  * [Ada Database Objects Programmer's Guide](https://ada-ado.readthedocs.io/en/latest/)
  * [Persistence with Ada Database Objects](https://fr.slideshare.net/StephaneCarrez1/persistence-with-ada-database-objects-ado) FOSDEM 2019



