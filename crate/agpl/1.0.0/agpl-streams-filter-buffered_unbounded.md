---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams.Filter.Buffered_Unbounded",
qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded",
signature: "agpl.streams.filter.buffered_unbounded",
enclosing: "agpl.streams.filter",
is_private: false,
documentation: "These parameters affect new instances (a-la Float_Io).",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_type",
       qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded.Stream_type",
       signature: "agpl.streams.filter.buffered_unbounded.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_type is new Filter.Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded.Stream_access",
       signature: "agpl.streams.filter.buffered_unbounded.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Stream_type'Class;",
       }   ,
   ]
,variables:    [
       {
       name: "Grow_Percent",
       qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded.Grow_Percent",
       signature: "agpl.streams.filter.buffered_unbounded.grow_percent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Grow_Percent    : Positive             := 50;",
       }   ,
       {
       name: "Initial_Buffer",
       qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded.Initial_Buffer",
       signature: "agpl.streams.filter.buffered_unbounded.initial_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Initial_Buffer  : Stream_Element_Count := 4096;",
       }   ,
       {
       name: "Max_Buffer_Size",
       qualified_name: "Agpl.Streams.Filter.Buffered_Unbounded.Max_Buffer_Size",
       signature: "agpl.streams.filter.buffered_unbounded.max_buffer_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Buffer_Size : Stream_Element_Count := Stream_Element_Count'Last;",
       }   ,
   ]
,}
---
