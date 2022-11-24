---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Symbols.Precomputed",
qualified_name: "Langkit_Support.Symbols.Precomputed",
signature: "langkit_support.symbols.precomputed",
enclosing: "langkit_support.symbols",
is_private: false,
documentation: "\nCopyright (C) 2020-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0\n\n@formal Precomputed_Symbol_Index\n  Indexes for symbols to pre-compute in each symbol table\n@formal Precomputed_Symbol\n  Return the symbol corresponding to the precomputed symbol Index",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Precomputed_Symbol_Table_Record",
       qualified_name: "Langkit_Support.Symbols.Precomputed.Precomputed_Symbol_Table_Record",
       signature: "langkit_support.symbols.precomputed.precomputed_symbol_table_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Precomputed_Symbol_Table_Record\nis new Symbol_Table_Record with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Precomputed_Symbol_Table",
       qualified_name: "Langkit_Support.Symbols.Precomputed.Precomputed_Symbol_Table",
       signature: "langkit_support.symbols.precomputed.precomputed_symbol_table",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Precomputed_Symbol_Table\nis access all Precomputed_Symbol_Table_Record'Class;",
       }   ,
   ]
,}
---
