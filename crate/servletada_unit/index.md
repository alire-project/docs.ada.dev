---
layout: crate
crate: "servletada_unit"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-servlet"]
tags: ["web",
"servlet",
"http",
"json",
"rest",
"testing"]
version: "1.6.0"
short_description: "Web Servlet Library following JSR 154, JSR 315 (Testing framework)"
dependencies: [{crate: "servletada", version: "^1.6.0"},
{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_unit", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![codecov](https://codecov.io/gh/stcarrez/ada-servlet/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-servlet)

This library provides helper operations for unit testing a servlet implemented on top of
Ada Servlet.



