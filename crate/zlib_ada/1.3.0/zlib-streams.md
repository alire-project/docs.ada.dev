---
crate: zlib_ada
layout: gnatdoc
gnatdoc: {
name: "ZLib.Streams",
qualified_name: "ZLib.Streams",
signature: "zlib.streams",
enclosing: "zlib",
is_private: false,
documentation: "$Id: zlib-streams.ads,v 1.12 2004/05/31 10:53:40 vagul Exp $",
documentation_snippet: "",
simple_types:    [
       {
       name: "Stream_Mode",
       qualified_name: "ZLib.Streams.Stream_Mode",
       signature: "zlib.streams.stream_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Mode is (In_Stream, Out_Stream, Duplex);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Stream_Type",
       qualified_name: "ZLib.Streams.Stream_Type",
       signature: "zlib.streams.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Type is\n   new Ada.Streams.Root_Stream_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Stream_Access",
       qualified_name: "ZLib.Streams.Stream_Access",
       signature: "zlib.streams.stream_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Access is access all Ada.Streams.Root_Stream_Type'Class;",
       }   ,
   ]
,}
---
