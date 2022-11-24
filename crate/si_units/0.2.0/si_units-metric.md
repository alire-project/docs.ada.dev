---
crate: si_units
layout: gnatdoc
gnatdoc: {
name: "SI_Units.Metric",
qualified_name: "SI_Units.Metric",
signature: "si_units.metric",
enclosing: "si_units",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Prefixes",
       qualified_name: "SI_Units.Metric.Prefixes",
       signature: "si_units.metric.prefixes",
       enclosing: "",
       is_private: false,
       documentation: "Prefixes supported in instantiated Image subprograms.\n\n@enum yocto\n@enum zepto\n@enum atto\n@enum femto\n@enum pico\n@enum nano\n@enum micro\n@enum milli\n@enum None\n@enum kilo\n@enum Mega\n@enum Giga\n@enum Tera\n@enum Peta\n@enum Exa\n@enum Zetta\n@enum Yotta",
       documentation_snippet: "type Prefixes is (yocto, zepto, atto, femto, pico, nano, micro, milli,\n                  None,\n                  kilo, Mega, Giga, Tera, Peta, Exa, Zetta, Yotta);",
       }   ,
   ]
,constants:    [
       {
       name: "Magnitude",
       qualified_name: "SI_Units.Metric.Magnitude",
       signature: "si_units.metric.magnitude",
       enclosing: "",
       is_private: false,
       documentation: "Magnitude change when trying to find the best representation for a given\nvalue.",
       documentation_snippet: "Magnitude : constant := 1000.0;",
       }   ,
   ]
,}
---
