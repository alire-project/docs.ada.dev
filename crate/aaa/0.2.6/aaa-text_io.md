---
crate: aaa
layout: gnatdoc
gnatdoc: {
name: "AAA.Text_IO",
qualified_name: "AAA.Text_IO",
signature: "aaa.text_io",
enclosing: "aaa",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Filling_Modes",
       qualified_name: "AAA.Text_IO.Filling_Modes",
       signature: "aaa.text_io.filling_modes",
       enclosing: "",
       is_private: false,
       documentation: "Fancier modes exist, not implemented for now.\n\n@enum Greedy",
       documentation_snippet: "type Filling_Modes is (Greedy);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "File",
       qualified_name: "AAA.Text_IO.File",
       signature: "aaa.text_io.file",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type File (<>) is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Line_Widths",
       qualified_name: "AAA.Text_IO.Line_Widths",
       signature: "aaa.text_io.line_widths",
       enclosing: "",
       is_private: false,
       documentation: "We need to at least be able to\nw-\nr-\ni-\nt-\ne like this.",
       documentation_snippet: "subtype Line_Widths is Positive range 2 .. Positive'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Line_Width",
       qualified_name: "AAA.Text_IO.Default_Line_Width",
       signature: "aaa.text_io.default_line_width",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Line_Width : constant := 79;",
       }   ,
   ]
,}
---
