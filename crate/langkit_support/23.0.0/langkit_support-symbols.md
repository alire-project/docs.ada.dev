---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Symbols",
qualified_name: "Langkit_Support.Symbols",
signature: "langkit_support.symbols",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Symbol_Type",
       qualified_name: "Langkit_Support.Symbols.Symbol_Type",
       signature: "langkit_support.symbols.symbol_type",
       enclosing: "",
       is_private: false,
       documentation: "Main symbol type.\n\n.. warning:: For usability reasons, we use the access to the string as a\n   symbol type. This is very convenient because you can access the text\n   of a symbol without a reference to the symbol table, but is also\n   unsafe, because if the symbol table has been freed, the symbol will\n   be a dangling pointer.",
       documentation_snippet: "type Symbol_Type is new Text_Cst_Access;",
       }   ,
       {
       name: "Thin_Symbol",
       qualified_name: "Langkit_Support.Symbols.Thin_Symbol",
       signature: "langkit_support.symbols.thin_symbol",
       enclosing: "",
       is_private: false,
       documentation: "Thin symbol type. This type is a bit heavier to use than the main symbol\ntype, because you need a reference to the symbol table to get the text\nof the symbol, but:\n\n1. It consumes less memory (which is the primary reason it is used in\n   Langkit).\n\n2. It is safer, as long as you never store :ada:ref:`Symbol_Type`\n   instances returned by :ada:ref:`Get_Symbol` you should be safe.\n\n.. TODO: See if we can get rid of the intermediate operation that\n   returns a ``Symbol_Type``.",
       documentation_snippet: "type Thin_Symbol is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Symbolization_Result",
       qualified_name: "Langkit_Support.Symbols.Symbolization_Result",
       signature: "langkit_support.symbols.symbolization_result",
       enclosing: "",
       is_private: false,
       documentation: "Holder for results of the symbolization process, conditionned by whether\nthis process was successful.\n\n@field Success\n@field Size\n@field Symbol\n  Text for successfully symbolized identifiers\n@field Error_Message",
       documentation_snippet: "type Symbolization_Result (Success : Boolean; Size : Natural) is record\n   case Success is\n      when True  =>\n         Symbol : Text_Type (1 .. Size);\n      when False =>\n         Error_Message : Text_Type (1 .. Size);\n   end case;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Symbol_Table_Record",
       qualified_name: "Langkit_Support.Symbols.Symbol_Table_Record",
       signature: "langkit_support.symbols.symbol_table_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Symbol_Table_Record is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Symbol_Table",
       qualified_name: "Langkit_Support.Symbols.Symbol_Table",
       signature: "langkit_support.symbols.symbol_table",
       enclosing: "",
       is_private: false,
       documentation: "Represents a symbol table. The symbol table is the holder of the memory\nallocated for each symbol, and serves as a single access point if you\nwant to find back an existing symbol.",
       documentation_snippet: "type Symbol_Table is access all Symbol_Table_Record'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Symbol_Table",
       qualified_name: "Langkit_Support.Symbols.No_Symbol_Table",
       signature: "langkit_support.symbols.no_symbol_table",
       enclosing: "",
       is_private: false,
       documentation: "Value to use as a default for unallocated symbol tables",
       documentation_snippet: "No_Symbol_Table : constant Symbol_Table;",
       }   ,
       {
       name: "No_Thin_Symbol",
       qualified_name: "Langkit_Support.Symbols.No_Thin_Symbol",
       signature: "langkit_support.symbols.no_thin_symbol",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Thin_Symbol : constant Thin_Symbol;",
       }   ,
   ]
,}
---
