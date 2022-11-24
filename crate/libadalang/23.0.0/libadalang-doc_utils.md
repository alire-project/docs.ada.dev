---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Doc_Utils",
qualified_name: "Libadalang.Doc_Utils",
signature: "libadalang.doc_utils",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
record_types:    [
       {
       name: "Doc_Type",
       qualified_name: "Libadalang.Doc_Utils.Doc_Type",
       signature: "libadalang.doc_utils.doc_type",
       enclosing: "",
       is_private: false,
       documentation: "Type representing the documentation of an entity\n\n@field Doc\n  Documentation, where every line is concatenated as one XString\n@field Annotations",
       documentation_snippet: "type Doc_Type is record\n   Doc : XStrings.XString;\n   Annotations : Annotations_Maps.Map;\nend record;",
       }   ,
   ]
,}
---
