---
crate: linenoise_ada
layout: gnatdoc
gnatdoc: {
name: "Linenoise",
qualified_name: "Linenoise",
signature: "linenoise",
enclosing: "",
is_private: false,
documentation: "A vector of strings package, used by Completion_Callbacks and Split.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Color_Codes",
       qualified_name: "Linenoise.Color_Codes",
       signature: "linenoise.color_codes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "        type Color_Codes is\n		(Default, Red, Green, Yellow, Blue, Magenta, Cyan, White);",
       }   ,
       {
       name: "History_Length",
       qualified_name: "Linenoise.History_Length",
       signature: "linenoise.history_length",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type History_Length is range 0 .. Interfaces.C.int'Last;",
       }   ,
   ]
,access_types:    [
       {
       name: "Completion_Callback",
       qualified_name: "Linenoise.Completion_Callback",
       signature: "linenoise.completion_callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "        type Completion_Callback is access\n		function (Line : String) return String_Vectors.Vector;",
       }   ,
       {
       name: "Hint_Callback",
       qualified_name: "Linenoise.Hint_Callback",
       signature: "linenoise.hint_callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "        type Hint_Callback is access\n		function (\n			Line : String;\n			Color : out Color_Codes; Bold : out Boolean\n		) return String;",
       }   ,
   ]
,}
---
