---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Strings.superbounded",
qualified_name: "lace.Strings.superbounded",
signature: "lace.strings.superbounded",
enclosing: "lace.strings",
is_private: false,
documentation: "Type Bounded_String in Ada.Strings.Bounded.Generic_Bounded_Length is\nderived from Super_String, with the constraint of the maximum length.",
documentation_snippet: "",
record_types:    [
       {
       name: "Super_String",
       qualified_name: "lace.Strings.superbounded.Super_String",
       signature: "lace.strings.superbounded.super_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Super_String (Max_Length : Positive) is\n   record\n      Current_Length : Natural := 0;\n      Data           : String (1 .. Max_Length);\n   end record;",
       }   ,
   ]
,}
---
