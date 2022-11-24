---
crate: apdf
layout: gnatdoc
gnatdoc: {
name: "Fancy_page",
qualified_name: "Fancy_page",
signature: "fancy_page",
enclosing: "",
is_private: false,
documentation: "Demo for custom, overriden methods (e.g. header, footer) in PDF_Out",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Fancy_PDF",
       qualified_name: "Fancy_page.Fancy_PDF",
       signature: "fancy_page.fancy_pdf",
       enclosing: "",
       is_private: false,
       documentation: "\n@field page_nb\n  Total page number, obtained by running twice (à la TeX).",
       documentation_snippet: "type Fancy_PDF is new PDF_Out.PDF_Out_File with record\n  page_nb: Natural:= 0;\nend record;",
       }   ,
   ]
,}
---
