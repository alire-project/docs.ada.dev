---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Input_Sources",
qualified_name: "Input_Sources",
signature: "input_sources",
enclosing: "",
is_private: false,
documentation: "<description>\nThis package provides a hierarchy of objects that return characters\nthat can then be used for different tasks.\nIt is not possible to go backward, nor to previous characters. This\ninterface is intentionally kept minimal, so that it can easily be used\nwith files, sockets, ...\n\nInput sources should try to automatically detect the appropriate encoding\nto use, for instance by using the byte order mark, if present, of the\nunicode stream (16#FFFE# or 16#FEFF#).\n</description>",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Input_Source",
       qualified_name: "Input_Sources.Input_Source",
       signature: "input_sources.input_source",
       enclosing: "",
       is_private: false,
       documentation: "General object for reading characters, one at a time.",
       documentation_snippet: "type Input_Source is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Input_Source_Access",
       qualified_name: "Input_Sources.Input_Source_Access",
       signature: "input_sources.input_source_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Input_Source_Access is access all Input_Source'Class;",
       }   ,
   ]
,}
---
