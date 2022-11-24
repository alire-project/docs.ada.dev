---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams",
qualified_name: "Agpl.Streams",
signature: "agpl.streams",
enclosing: "agpl",
is_private: false,
documentation: "----------------------------------------------------------------------\n Types                                                              --\n----------------------------------------------------------------------",
documentation_snippet: "",
access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Stream_access",
       signature: "agpl.streams.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Ada.Streams.Root_stream_type'Class;",
       }   ,
       {
       name: "Stream_element_array_access",
       qualified_name: "Agpl.Streams.Stream_element_array_access",
       signature: "agpl.streams.stream_element_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_element_array_access is access all\n   Ada.Streams.Stream_element_array;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Root_Stream_Type",
       qualified_name: "Agpl.Streams.Root_Stream_Type",
       signature: "agpl.streams.root_stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Root_Stream_Type      is Ada.Streams.Root_Stream_Type;",
       }   ,
       {
       name: "Stream_Element_Array",
       qualified_name: "Agpl.Streams.Stream_Element_Array",
       signature: "agpl.streams.stream_element_array",
       enclosing: "",
       is_private: false,
       documentation: "use type Stream_Element_Offset;",
       documentation_snippet: "subtype Stream_Element_Array  is Ada.Streams.Stream_Element_Array;",
       }   ,
       {
       name: "Stream_Element_Count",
       qualified_name: "Agpl.Streams.Stream_Element_Count",
       signature: "agpl.streams.stream_element_count",
       enclosing: "",
       is_private: false,
       documentation: "use type Stream_Element_Offset;",
       documentation_snippet: "subtype Stream_Element_Count  is Ada.Streams.Stream_Element_Count;",
       }   ,
       {
       name: "Stream_Element_Offset",
       qualified_name: "Agpl.Streams.Stream_Element_Offset",
       signature: "agpl.streams.stream_element_offset",
       enclosing: "",
       is_private: false,
       documentation: "use type Stream_Element_Offset;",
       documentation_snippet: "subtype Stream_Element_Offset is Ada.Streams.Stream_Element_Offset;",
       }   ,
   ]
,}
---
