---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.PP",
qualified_name: "Prj.PP",
signature: "prj.pp",
enclosing: "prj",
is_private: false,
documentation: "The following access to procedure types are used to redirect output when\ncalling Pretty_Print.",
documentation_snippet: "",
access_types:    [
       {
       name: "Write_Char_Ap",
       qualified_name: "Prj.PP.Write_Char_Ap",
       signature: "prj.pp.write_char_ap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Char_Ap is access procedure (C : Character);",
       }   ,
       {
       name: "Write_Eol_Ap",
       qualified_name: "Prj.PP.Write_Eol_Ap",
       signature: "prj.pp.write_eol_ap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Eol_Ap  is access procedure;",
       }   ,
       {
       name: "Write_Str_Ap",
       qualified_name: "Prj.PP.Write_Str_Ap",
       signature: "prj.pp.write_str_ap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Write_Str_Ap is access procedure (S : String);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Max_Length_Of_Line",
       qualified_name: "Prj.PP.Max_Length_Of_Line",
       signature: "prj.pp.max_length_of_line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Max_Length_Of_Line is Positive range 50 .. 255;",
       }   ,
   ]
,}
---
