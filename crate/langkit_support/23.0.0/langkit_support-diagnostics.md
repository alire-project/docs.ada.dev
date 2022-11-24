---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Diagnostics",
qualified_name: "Langkit_Support.Diagnostics",
signature: "langkit_support.diagnostics",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
array_types:    [
       {
       name: "Diagnostics_Array",
       qualified_name: "Langkit_Support.Diagnostics.Diagnostics_Array",
       signature: "langkit_support.diagnostics.diagnostics_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Diagnostics_Array is array (Positive range <>) of Diagnostic;",
       }   ,
   ]
,record_types:    [
       {
       name: "Diagnostic",
       qualified_name: "Langkit_Support.Diagnostics.Diagnostic",
       signature: "langkit_support.diagnostics.diagnostic",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Sloc_Range\n  The source location range that the diagnostic message refers to\n@field Message",
       documentation_snippet: "type Diagnostic is record\n   Sloc_Range : Source_Location_Range;\n   Message    : Unbounded_Text_Type;\nend record;",
       }   ,
   ]
,}
---
