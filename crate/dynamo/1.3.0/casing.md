---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Casing",
qualified_name: "Casing",
signature: "casing",
enclosing: "",
is_private: false,
documentation: "This package contains data and subprograms to support the feature that\nrecognizes the letter case styles used in the source program being\ncompiled, and uses this information for error message formatting, and\nfor recognizing reserved words that are misused as identifiers.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Casing_Type",
       qualified_name: "Casing.Casing_Type",
       signature: "casing.casing_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum All_Upper_Case\n  All letters are upper case\n@enum All_Lower_Case\n  All letters are lower case\n@enum Mixed_Case\n  The initial letter, and any letters after underlines are upper case.\n  All other letters are lower case\n@enum Unknown",
       documentation_snippet: "type Casing_Type is (\n   All_Upper_Case,\n   All_Lower_Case,\n   Mixed_Case,\n   Unknown\n);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Known_Casing",
       qualified_name: "Casing.Known_Casing",
       signature: "casing.known_casing",
       enclosing: "",
       is_private: false,
       documentation: "Exclude Unknown casing",
       documentation_snippet: "subtype Known_Casing is Casing_Type range All_Upper_Case .. Mixed_Case;",
       }   ,
   ]
,}
---
