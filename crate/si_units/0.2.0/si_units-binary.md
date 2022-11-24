---
crate: si_units
layout: gnatdoc
gnatdoc: {
name: "SI_Units.Binary",
qualified_name: "SI_Units.Binary",
signature: "si_units.binary",
enclosing: "si_units",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Prefixes",
       qualified_name: "SI_Units.Binary.Prefixes",
       signature: "si_units.binary.prefixes",
       enclosing: "",
       is_private: false,
       documentation: "Prefixes supported in instantiated Image subprograms.\n\n@enum None\n@enum kibi\n@enum mebi\n@enum gibi\n@enum tebi\n@enum pebi\n@enum exbi\n@enum zebi\n@enum yobi",
       documentation_snippet: "type Prefixes is (None, kibi, mebi, gibi, tebi, pebi, exbi, zebi, yobi);",
       }   ,
   ]
,constants:    [
       {
       name: "Magnitude",
       qualified_name: "SI_Units.Binary.Magnitude",
       signature: "si_units.binary.magnitude",
       enclosing: "",
       is_private: false,
       documentation: "Magnitude change when trying to find the best representation for a given\nvalue.",
       documentation_snippet: "Magnitude : constant := 1024.0;",
       }   ,
   ]
,}
---
