---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Names",
qualified_name: "Langkit_Support.Names",
signature: "langkit_support.names",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Casing_Convention",
       qualified_name: "Langkit_Support.Names.Casing_Convention",
       signature: "langkit_support.names.casing_convention",
       enclosing: "",
       is_private: false,
       documentation: "Designate a specific casing convention for names formatting. For\ninstance, to format the ``HTML_Document_Root`` name::\n\n   Camel_With_Underscores: HTML_Document_Root\n   Camel:                  HTMLDocumentRoot\n   Lower:                  html_document_root\n   Upper:                  HTML_DOCUMENT_ROOT\n\nNote that ``Camel_With_Underscores`` is the convention which preserves\nthe most information about a name: for instance it is not possible to\nknow from ``HTML_DOCUMENT_ROOT`` (an ``Upper`` formatted name) whether\nits ``Camel_With_Underscores`` format is ``HTML_Document_ROOT``,\n``Html_Document_Root`` or any other casing variation, while the\nreciprocical is true.\n\nBecause of this, different names can have different formattings in some\nconventions and same formattings in other conventions.\n\n@enum Camel_With_Underscores\n@enum Camel\n@enum Lower\n@enum Upper",
       documentation_snippet: "type Casing_Convention is (Camel_With_Underscores, Camel, Lower, Upper);",
       }   ,
       {
       name: "Name_Type",
       qualified_name: "Langkit_Support.Names.Name_Type",
       signature: "langkit_support.names.name_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Name_Type is private;",
       }   ,
   ]
,}
---
