---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Symbol_Info",
qualified_name: "Symbol_Info",
signature: "symbol_info",
enclosing: "",
is_private: false,
documentation: "\nThe following array declarations are used to compute the\nthe rules that have a particular symbol on the left hand\nside. NONTERMINAL_YIELD contains the rules and\nNONTERMINAL_YIELD_OFFSET contains the offset into the first array\nindexed by a particular nonterminal.  The user of this package\nshould not attempt to alter the contents of these arrays. They\nare visible in the spec only for efficiency reasons.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Yield_Index",
       qualified_name: "Symbol_Info.Yield_Index",
       signature: "symbol_info.yield_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Yield_Index      is  new Integer;",
       }   ,
   ]
,array_types:    [
       {
       name: "Offset_Array",
       qualified_name: "Symbol_Info.Offset_Array",
       signature: "symbol_info.offset_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Offset_Array     is  array (Grammar_Symbol range <>) of Yield_Index;",
       }   ,
       {
       name: "Rule_Array",
       qualified_name: "Symbol_Info.Rule_Array",
       signature: "symbol_info.rule_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rule_Array       is  array (Yield_Index range <>)    of Rule;",
       }   ,
   ]
,access_types:    [
       {
       name: "Offset_Array_Pointer",
       qualified_name: "Symbol_Info.Offset_Array_Pointer",
       signature: "symbol_info.offset_array_pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Offset_Array_Pointer is access Offset_Array;",
       }   ,
       {
       name: "Rule_Array_Pointer",
       qualified_name: "Symbol_Info.Rule_Array_Pointer",
       signature: "symbol_info.rule_array_pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rule_Array_Pointer   is access Rule_Array;",
       }   ,
   ]
,variables:    [
       {
       name: "Nonterminal_Yield",
       qualified_name: "Symbol_Info.Nonterminal_Yield",
       signature: "symbol_info.nonterminal_yield",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Nonterminal_Yield           : Rule_Array_Pointer;",
       }   ,
       {
       name: "Nonterminal_Yield_Index",
       qualified_name: "Symbol_Info.Nonterminal_Yield_Index",
       signature: "symbol_info.nonterminal_yield_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Nonterminal_Yield_Index     : Offset_Array_Pointer;",
       }   ,
   ]
,}
---
