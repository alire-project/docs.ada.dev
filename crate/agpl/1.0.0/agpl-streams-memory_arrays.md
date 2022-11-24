---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams.Memory_arrays",
qualified_name: "Agpl.Streams.Memory_arrays",
signature: "agpl.streams.memory_arrays",
enclosing: "agpl.streams",
is_private: false,
documentation: "New stream type:\nTakes an access to an element array. It should remain allocated\nduring the life of this stream.\nIt will not be deallocated",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_type",
       qualified_name: "Agpl.Streams.Memory_arrays.Stream_type",
       signature: "agpl.streams.memory_arrays.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_type (\n   Data  : access Stream_element_array) is new\n   Ada.Streams.Root_Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Memory_arrays.Stream_access",
       signature: "agpl.streams.memory_arrays.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Stream_type;",
       }   ,
   ]
,}
---
