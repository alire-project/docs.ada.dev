---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Hash_Tables",
qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables",
signature: "sal.gen_unbounded_definite_hash_tables",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Key_Type\n@formal Key\n@formal Key_Compare\n@formal Hash\n  WORKAROUND: GNAT community 2019 doesn't allow 'with post' here\n  with Release compilation switches. Fixed in GNAT community 2021.\n  with Post => Hash'Result in 1 .. Rows;\n  \n  Takes Element, not Key, to allow storing Hash in Element so it is\n  only computed once.\n  \n  1 + (Some_hash (Key) mod Rows) works.\n@formal Default_Init_Rows",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Cursor",
       signature: "sal.gen_unbounded_definite_hash_tables.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Hash_Table",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Hash_Table",
       signature: "sal.gen_unbounded_definite_hash_tables.hash_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Hash_Table is tagged private\nwith\n  Constant_Indexing => Constant_Ref,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Element_Type;",
       }   ,
       {
       name: "Iterator",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Iterator",
       signature: "sal.gen_unbounded_definite_hash_tables.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator (<>) is new Iterators.Forward_Iterator with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_hash_tables.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "The name lies; this is not a \"reference type\" as defined by Ada.\nBut gnat pro 22.0w 20201222 does not support using a real\nreference type here. See AdaCore ticket U117-010 (on the\nEurocontrol contract).",
       documentation_snippet: "type Constant_Reference_Type is access constant Element_Type;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Variable_Reference_Type",
       signature: "sal.gen_unbounded_definite_hash_tables.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "Similarly, this is not a \"reference type\"; therefore we cannot\nimplement aspect Variable_Indexing.",
       documentation_snippet: "type Variable_Reference_Type is access all Element_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Rows",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.Default_Rows",
       signature: "sal.gen_unbounded_definite_hash_tables.default_rows",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Rows : constant Positive := Pkg.Default_Init_Rows;",
       }   ,
       {
       name: "No_Element",
       qualified_name: "SAL.Gen_Unbounded_Definite_Hash_Tables.No_Element",
       signature: "sal.gen_unbounded_definite_hash_tables.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---
