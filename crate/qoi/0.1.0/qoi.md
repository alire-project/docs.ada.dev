---
crate: qoi
layout: gnatdoc
gnatdoc: {
name: "QOI",
qualified_name: "QOI",
signature: "qoi",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Colorspace_Kind",
       qualified_name: "QOI.Colorspace_Kind",
       signature: "qoi.colorspace_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Colorspace_Kind is (SRGB, SRGB_Linear_Alpha);",
       }   ,
   ]
,record_types:    [
       {
       name: "QOI_Desc",
       qualified_name: "QOI.QOI_Desc",
       signature: "qoi.qoi_desc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type QOI_Desc is record\n   Width, Height : Storage_Count;\n   Channels      : Storage_Count;\n   Colorspace    : Colorspace_Kind;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "QOI_HEADER_SIZE",
       qualified_name: "QOI.QOI_HEADER_SIZE",
       signature: "qoi.qoi_header_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "QOI_HEADER_SIZE : constant := 14;",
       }   ,
       {
       name: "QOI_PADDING",
       qualified_name: "QOI.QOI_PADDING",
       signature: "qoi.qoi_padding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "QOI_PADDING : constant Storage_Array (1 .. 8) := (0, 0, 0, 0, 0, 0, 0, 1);",
       }   ,
   ]
,}
---
