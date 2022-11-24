---
crate: lzmada
layout: gnatdoc
gnatdoc: {
name: "Lzma.Vli",
qualified_name: "Lzma.Vli",
signature: "lzma.vli",
enclosing: "lzma",
is_private: false,
documentation: "unsupported macro: LZMA_VLI_MAX (UINT64_MAX / 2)\nunsupported macro: LZMA_VLI_UNKNOWN UINT64_MAX",
documentation_snippet: "",
subtypes:    [
       {
       name: "lzma_vli",
       qualified_name: "Lzma.Vli.lzma_vli",
       signature: "lzma.vli.lzma_vli",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/vli.h:63",
       documentation_snippet: "subtype lzma_vli is Long_Long_Integer;",
       }   ,
   ]
,constants:    [
       {
       name: "LZMA_VLI_BYTES_MAX",
       qualified_name: "Lzma.Vli.LZMA_VLI_BYTES_MAX",
       signature: "lzma.vli.lzma_vli_bytes_max",
       enclosing: "",
       is_private: false,
       documentation: "/usr/include/lzma/vli.h:44\narg-macro: procedure LZMA_VLI_C UINT64_C(n)\n  UINT64_C(n)\narg-macro: function lzma_vli_is_valid ((vli) <= LZMA_VLI_MAX  or else  (vli) = LZMA_VLI_UNKNOWN\n  return (vli) <= LZMA_VLI_MAX  or else  (vli) = LZMA_VLI_UNKNOWN;",
       documentation_snippet: "LZMA_VLI_BYTES_MAX : constant := 9;",
       }   ,
   ]
,}
---
