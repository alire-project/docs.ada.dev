---
crate: lzmada
layout: gnatdoc
gnatdoc: {
name: "Lzma.Filter",
qualified_name: "Lzma.Filter",
signature: "lzma.filter",
enclosing: "lzma",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "lzma_filter",
       qualified_name: "Lzma.Filter.lzma_filter",
       signature: "lzma.filter.lzma_filter",
       enclosing: "",
       is_private: false,
       documentation: "\n@field id\n  /usr/include/lzma/filter.h:54\n@field options\n  /usr/include/lzma/filter.h:63\n  /usr/include/lzma/filter.h:65",
       documentation_snippet: "type lzma_filter is record\n   id : aliased Lzma.Vli.lzma_vli;\n   options : System.Address;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "LZMA_FILTERS_MAX",
       qualified_name: "Lzma.Filter.LZMA_FILTERS_MAX",
       signature: "lzma.filter.lzma_filters_max",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/filter.h:26",
       documentation_snippet: "LZMA_FILTERS_MAX : constant := 4;",
       }   ,
   ]
,}
---
