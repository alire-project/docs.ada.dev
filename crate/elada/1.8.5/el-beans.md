---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Beans",
qualified_name: "EL.Beans",
signature: "el.beans",
enclosing: "el",
is_private: false,
documentation: "------------------------------\nBean Initialization\n------------------------------\nThe <b>Param_Value</b> describes a bean property that must be initialized by evaluating the\nassociated EL expression.  A list of <b>Param_Value</b> can be used to initialize several\nbean properties of an object.  The bean object must implement the <b>Bean</b> interface\nwith the <b>Set_Value</b> operation.",
documentation_snippet: "",
record_types:    [
       {
       name: "Param_Value",
       qualified_name: "EL.Beans.Param_Value",
       signature: "el.beans.param_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Param_Value (Length : Natural) is record\n   Name  : String (1 .. Length);\n   Value : EL.Expressions.Expression;\nend record;",
       }   ,
   ]
,}
---
