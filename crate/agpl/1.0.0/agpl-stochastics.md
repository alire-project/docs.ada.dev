---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Stochastics",
qualified_name: "Agpl.Stochastics",
signature: "agpl.stochastics",
enclosing: "agpl",
is_private: false,
documentation: "The following types could be made generic if necessary at this level?",
documentation_snippet: "",
simple_types:    [
       {
       name: "Probabilities",
       qualified_name: "Agpl.Stochastics.Probabilities",
       signature: "agpl.stochastics.probabilities",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Probabilities is new Float range 0.0 .. 1.0 + Delta_Error;",
       }   ,
   ]
,constants:    [
       {
       name: "Delta_Error",
       qualified_name: "Agpl.Stochastics.Delta_Error",
       signature: "agpl.stochastics.delta_error",
       enclosing: "",
       is_private: false,
       documentation: "Distance to 1.0 in total probabilities greater than this would be\nconsidered an error:",
       documentation_snippet: "Delta_Error : constant := 0.000001;",
       }   ,
   ]
,}
---
