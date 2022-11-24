---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Streams.Circular_Unbounded",
qualified_name: "Agpl.Streams.Circular_Unbounded",
signature: "agpl.streams.circular_unbounded",
enclosing: "agpl.streams",
is_private: false,
documentation: "Circular stream. This is a buffering stream where the written data\n  can be read afterwards in typical producer/consumer fashion.\nThe internal buffer will grow as needed to acommodate unread data.\nThe internal buffer isn't allocated until the first writting to save memory\nusage.\nAdditionally, it is controlled.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_type",
       qualified_name: "Agpl.Streams.Circular_Unbounded.Stream_type",
       signature: "agpl.streams.circular_unbounded.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_type\nis new Agpl.Streams.Observable.Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_access",
       qualified_name: "Agpl.Streams.Circular_Unbounded.Stream_access",
       signature: "agpl.streams.circular_unbounded.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_access is access all Stream_type'Class;",
       }   ,
   ]
,}
---
