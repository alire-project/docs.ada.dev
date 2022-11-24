---
crate: xml_ez_out
layout: gnatdoc
gnatdoc: {
name: "Mckae.XML.EZ_Out.String_Stream",
qualified_name: "Mckae.XML.EZ_Out.String_Stream",
signature: "mckae.xml.ez_out.string_stream",
enclosing: "mckae.xml.ez_out",
is_private: false,
documentation: "A basic in-memory string-based XML document construction\n utility.  This is not intended to be a robust, full-function\n memory buffering package.",
documentation_snippet: "",
packages:    [
       {
       name: "String_Buffering",
       qualified_name: "Mckae.XML.EZ_Out.String_Stream.String_Buffering",
       signature: "mckae.xml.ez_out.string_stream.string_buffering",
       enclosing: "mckae.xml.ez_out.string_stream",
       is_private: false,
       documentation: "There's little point in having a small buffer for building XML\n documents, so the minimum size and expansion is 500 characters.",
       documentation_snippet: "",
simple_types:           [
              {
              name: "String_Buffer",
              qualified_name: "Mckae.XML.EZ_Out.String_Stream.String_Buffering.String_Buffer",
              signature: "mckae.xml.ez_out.string_stream.string_buffering.string_buffer",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type String_Buffer (Initial_Size : Buffer_Size_Range := 5000;\n                    Expansion    : Buffer_Size_Range := 5000) is limited private;",
              }          ,
          ]
,subtypes:           [
              {
              name: "Buffer_Size_Range",
              qualified_name: "Mckae.XML.EZ_Out.String_Stream.String_Buffering.Buffer_Size_Range",
              signature: "mckae.xml.ez_out.string_stream.string_buffering.buffer_size_range",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Buffer_Size_Range is Positive range 500 .. Positive'Last;",
              }          ,
          ]
,       }   ,
   ]
,subtypes:    [
       {
       name: "Buffer_Size_Range",
       qualified_name: "Mckae.XML.EZ_Out.String_Stream.Buffer_Size_Range",
       signature: "mckae.xml.ez_out.string_stream.buffer_size_range",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Buffer_Size_Range is String_Buffering.Buffer_Size_Range;",
       }   ,
       {
       name: "String_Buffer",
       qualified_name: "Mckae.XML.EZ_Out.String_Stream.String_Buffer",
       signature: "mckae.xml.ez_out.string_stream.string_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype String_Buffer is String_Buffering.String_Buffer;",
       }   ,
   ]
,}
---
