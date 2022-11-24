---
crate: lace
layout: gnatdoc
gnatdoc: {
name: "lace.Strings.Bounded",
qualified_name: "lace.Strings.Bounded",
signature: "lace.strings.bounded",
enclosing: "lace.strings",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Generic_Bounded_Length",
       qualified_name: "lace.Strings.Bounded.Generic_Bounded_Length",
       signature: "lace.strings.bounded.generic_bounded_length",
       enclosing: "lace.strings.bounded",
       is_private: false,
       documentation: "\n@formal Max\n  Maximum length of a Bounded_String",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Bounded_String",
              qualified_name: "lace.Strings.Bounded.Generic_Bounded_Length.Bounded_String",
              signature: "lace.strings.bounded.generic_bounded_length.bounded_string",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Bounded_String is private;",
              }          ,
          ]
,subtypes:           [
              {
              name: "Length_Range",
              qualified_name: "lace.Strings.Bounded.Generic_Bounded_Length.Length_Range",
              signature: "lace.strings.bounded.generic_bounded_length.length_range",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Length_Range is Natural range 0 .. Max_Length;",
              }          ,
          ]
,constants:           [
              {
              name: "Max_Length",
              qualified_name: "lace.Strings.Bounded.Generic_Bounded_Length.Max_Length",
              signature: "lace.strings.bounded.generic_bounded_length.max_length",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Max_Length : constant Positive := Max;",
              }          ,
              {
              name: "Null_Bounded_String",
              qualified_name: "lace.Strings.Bounded.Generic_Bounded_Length.Null_Bounded_String",
              signature: "lace.strings.bounded.generic_bounded_length.null_bounded_string",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Null_Bounded_String : constant Bounded_String;",
              }          ,
          ]
,       }   ,
   ]
,}
---
