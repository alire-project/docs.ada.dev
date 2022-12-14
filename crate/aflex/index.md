---
layout: crate
crate: "aflex"
authors: ["John Self"]
maintainers: ["Stephane.Carrez@gmail.com"]
licenses: ["Unlicense"]
websites: ["https://github.com/Ada-France/aflex"]
tags: ["parser",
"generator",
"grammar"]
version: "1.5.2021"
short_description: "An Ada Lexical Analyzer Generator"
dependencies: []
configuration_variables: []
configuration_values: []

---
Aflex is a lexical analyzer generating tool similar to the Unix tool lex.

The first implementation was written by John Self of the Arcadia project
at the University of California, Irvine.  The last version that was released
appeared to be the aflex 1.4a released in 1994.

Aflex was used and improved by P2Ada, the Pascal to Ada translator.
This version of Aflex is derived from the P2Ada aflex implementation
released in August 2010.

This version brings a number of improvements:

- Aflex generates the spec and body files as separate files so that
  there is no need to use gnatchop to split the DFA and IO files.
- Aflex uses the lex file name to generate the package name and
  it supports child package with the `%unit` directive.



