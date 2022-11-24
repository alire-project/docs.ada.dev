---
crate: aaa
layout: gnatdoc
gnatdoc: {
name: "AAA.Table_IO",
qualified_name: "AAA.Table_IO",
signature: "aaa.table_io",
enclosing: "aaa",
is_private: false,
documentation: "A type to format tables according to the max length of fields. The table\nis ANSI-aware, so it will work properly for text with embedded ANSI\ncontrol sequences. However, non-left-aligned text may not align\nproperly.",
documentation_snippet: "",
array_types:    [
       {
       name: "Alignments",
       qualified_name: "AAA.Table_IO.Alignments",
       signature: "aaa.table_io.alignments",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Alignments is array (Positive range <>) of Ada.Strings.Alignment;",
       }   ,
   ]
,record_types:    [
       {
       name: "Reference",
       qualified_name: "AAA.Table_IO.Reference",
       signature: "aaa.table_io.reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reference (Table : access Table_IO.Table) is limited null record\n  with Implicit_Dereference => Table;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Table",
       qualified_name: "AAA.Table_IO.Table",
       signature: "aaa.table_io.table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Table is tagged private;",
       }   ,
   ]
,}
---
