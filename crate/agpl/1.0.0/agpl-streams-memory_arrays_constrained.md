---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams.Memory_arrays_constrained",
qualified_name: "Agpl.Streams.Memory_arrays_constrained",
signature: "agpl.streams.memory_arrays_constrained",
enclosing: "agpl.streams",
is_private: false,
documentation: "Allows reading from an array viewed as an stream:\nor writing to it.\nMixing the two operations is erroneous.\n\n@formal Size",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_type",
       qualified_name: "Agpl.Streams.Memory_arrays_constrained.Stream_type",
       signature: "agpl.streams.memory_arrays_constrained.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_type (Data  : access Sized_Array) is new\n   Ada.Streams.Root_Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Memory_arrays_constrained.Stream_access",
       signature: "agpl.streams.memory_arrays_constrained.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Stream_type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Sized_Array",
       qualified_name: "Agpl.Streams.Memory_arrays_constrained.Sized_Array",
       signature: "agpl.streams.memory_arrays_constrained.sized_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Sized_Array is Stream_Element_Array (1 .. Size);",
       }   ,
   ]
,}
---
