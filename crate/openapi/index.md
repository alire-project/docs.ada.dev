---
layout: crate
crate: "openapi"
authors: ["Stephane.Carrez@gmail.com"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Apache-2.0"]
websites: ["https://gitlab.com/stcarrez/openapi-ada"]
tags: ["rest",
"web",
"api",
"openapi"]
version: "0.6.0"
short_description: "OpenAPI library to build REST client applications"
dependencies: [{crate: "security", version: "^1.4.1"},
{crate: "utilada", version: "^2.5.0"},
{crate: "utilada_xml", version: "^2.5.0"}]
configuration_variables: []
configuration_values: []

---
[![Build Status](https://img.shields.io/jenkins/s/http/jenkins.vacs.fr/Bionic-Ada-Swagger.svg)](https://jenkins.vacs.fr/job/Bionic-Ada-Swagger/)
[![Test Status](https://img.shields.io/jenkins/t/http/jenkins.vacs.fr/Bionic-Ada-Swagger.svg)](https://jenkins.vacs.fr/job/Bionic-Ada-Swagger/)

[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) is a code generator that supports generation of
API client libraries, server stubs and documentation automatically
given an [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification).

The Ada client support has been integrated in [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator).

The OpenAPI Ada library is a small support library for the Ada code generator
provided by OpenAPI Generator.  The library provides support to serialize the data,
make HTTP requests and support the [OpenAPI Spec](https://github.com/OAI/OpenAPI-Specification).
specific operations or types.



