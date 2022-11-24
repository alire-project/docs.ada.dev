---
layout: crate
crate: "serverfaces_unit"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-asf"]
tags: ["web",
"servlet",
"http",
"framework",
"facelet",
"jsf",
"testing"]
version: "1.5.0"
short_description: "Web Server Faces JSR 252, JSR 314 and JSR 344 (Testing framework)"
dependencies: [{crate: "security", version: "^1.4.1"},
{crate: "serverfaces", version: "^1.5.0"},
{crate: "servletada", version: "^1.6.0"},
{crate: "servletada_unit", version: "^1.5.3"},
{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_unit", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Ada-Server-Faces.svg)](https://jenkins.vacs.fr/job/Ada-Server-Faces/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Ada-Server-Faces.svg)](https://jenkins.vacs.fr/job/Ada-Server-Faces/)
[![codecov](https://codecov.io/gh/stcarrez/ada-asf/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-asf)

Ada Server Faces allows to create web applications using the same pattern
as the Java Server Faces (See JSR 252, JSR 314 and JSR 344). 

This library provides a unit test framework that helps in building unit tests
on top of Ada Server Faces.



