---
layout: crate
crate: "security"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/ada-security"]
tags: ["security",
"oauth2",
"authentication",
"permissions",
"jwt"]
version: "1.4.1"
short_description: "Security Library for HTTP client and server with OAuth2 support"
dependencies: [{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_xml", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Ada-Security.svg)](https://jenkins.vacs.fr/job/Ada-Security/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Ada-Security.svg)](https://jenkins.vacs.fr/job/Ada-Security/)
[![codecov](https://codecov.io/gh/stcarrez/ada-security/branch/master/graph/badge.svg)](https://codecov.io/gh/stcarrez/ada-security)
[![Documentation Status](https://readthedocs.org/projects/ada-security/badge/?version=latest)](https://ada-security.readthedocs.io/en/latest/?badge=latest)

Ada Security provides a security framework which allows applications to define
and enforce security policies. This framework allows users to authenticate by using
[OpenID Authentication 2.0](https://openid.net/specs/openid-authentication-2_0.html)
as well as [OAuth 2.0](https://oauth.net/2/) protocol.
It allows a web application to integrate easily with Yahoo!, Gitlab, Github, Facebook and
Google+ authentication systems.
The Ada05 library includes:

* An OpenID client authentication,
* An OAuth 2.0 client authentication,
* An OpenID Connect authentication framework,
* An OAuth 2.0 server authentication framework,
* A policy based security framework to protect the resources


![Ada Security Overview](https://gitlab.com/stcarrez/ada-security/wiki/images/AdaSecurity.jpg)

The Ada Security library is used by the
[Ada Web Application](https://gitlab.com/stcarrez/ada-awa)
to provide authentication and access control to users within the web applications.



