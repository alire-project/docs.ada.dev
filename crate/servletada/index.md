---
layout: crate
crate: "servletada"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-servlet"]
tags: ["web",
"servlet",
"http",
"json",
"rest"]
version: "1.6.0"
short_description: "Web Servlet Library following JSR 154, JSR 315 (Core)"
dependencies: [{crate: "elada", version: "^1.8.5"},
{crate: "security", version: "^1.4.1"},
{crate: "utilada", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![codecov](https://codecov.io/gh/stcarrez/ada-servlet/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-servlet)

Ada Servlet allows to create web applications using the same pattern
as the Java Servlet (See JSR 154, JSR 315). 

The Ada Servlet library is used by the [Ada Server Faces](https://gitlab.com/stcarrez/ada-asf)
framework and [Ada Web Application](https://gitlab.com/stcarrez/ada-awa)
to provide server web requests.



