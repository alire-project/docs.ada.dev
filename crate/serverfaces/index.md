---
layout: crate
crate: "serverfaces"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-asf"]
tags: ["web",
"servlet",
"http",
"json"]
version: "1.5.0"
short_description: "Web Server Faces JSR 252, JSR 314 and JSR 344"
dependencies: [{crate: "security", version: "^1.4.1"},
{crate: "servletada", version: "^1.6.0"},
{crate: "utilada", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Ada-Servlet.svg)](https://jenkins.vacs.fr/job/Ada-Servlet/)
[![codecov](https://codecov.io/gh/stcarrez/ada-servlet/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-servlet)

Ada Servlet allows to create web applications using the same pattern
as the Java Servlet (See JSR 154, JSR 315). 

The Ada Servlet library is used by the [Ada Server Faces](https://github.com/stcarrez/ada-asf)
framework and [Ada Web Application](https://github.com/stcarrez/ada-awa)
to provide server web requests.



