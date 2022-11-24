---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Sax.Exceptions",
qualified_name: "Sax.Exceptions",
signature: "sax.exceptions",
enclosing: "sax",
is_private: false,
documentation: "-----------------\n Sax_Exception --\n-----------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Sax_Exception",
       qualified_name: "Sax.Exceptions.Sax_Exception",
       signature: "sax.exceptions.sax_exception",
       enclosing: "",
       is_private: false,
       documentation: "General type that encapsulates a general SAX error or warning.\nIt does not contain source location information (see Sax_Parse_Exception\ninstead)",
       documentation_snippet: "type Sax_Exception (<>) is tagged private;",
       }   ,
       {
       name: "Sax_Parse_Exception",
       qualified_name: "Sax.Exceptions.Sax_Parse_Exception",
       signature: "sax.exceptions.sax_parse_exception",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Sax_Parse_Exception (<>) is new Sax_Exception with private;",
       }   ,
   ]
,}
---
