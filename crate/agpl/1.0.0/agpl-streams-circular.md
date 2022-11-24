---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams.Circular",
qualified_name: "Agpl.Streams.Circular",
signature: "agpl.streams.circular",
enclosing: "agpl.streams",
is_private: false,
documentation: "----------------------------------------------------------------------\n Stream_type                                                        --\n----------------------------------------------------------------------\n  The size of the intermediate buffer is the maximum non-read data we\n  can have:",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_type",
       qualified_name: "Agpl.Streams.Circular.Stream_type",
       signature: "agpl.streams.circular.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_type (Size : Stream_element_count) is new\n   Streams.Observable.Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Circular.Stream_access",
       signature: "agpl.streams.circular.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Stream_type;",
       }   ,
   ]
,}
---
