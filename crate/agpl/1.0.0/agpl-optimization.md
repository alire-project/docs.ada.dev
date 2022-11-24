---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Optimization",
qualified_name: "Agpl.Optimization",
signature: "agpl.optimization",
enclosing: "agpl",
is_private: false,
documentation: "type Cost is delta 0.00001 digits 18;\ntype Cost is new Long_Float;",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cost",
       qualified_name: "Agpl.Optimization.Cost",
       signature: "agpl.optimization.cost",
       enclosing: "",
       is_private: false,
       documentation: "We are *minimizing* the solution cost.\nIf you want ot maximize an utility function, simply negate your function.",
       documentation_snippet: "type Cost is new Float;",
       }   ,
   ]
,constants:    [
       {
       name: "Infinite",
       qualified_name: "Agpl.Optimization.Infinite",
       signature: "agpl.optimization.infinite",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Infinite : constant Cost := Cost'Last;",
       }   ,
   ]
,}
---
