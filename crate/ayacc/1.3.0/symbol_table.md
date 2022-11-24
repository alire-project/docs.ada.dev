---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Symbol_Table",
qualified_name: "Symbol_Table",
signature: "symbol_table",
enclosing: "",
is_private: false,
documentation: "$Header: symbol_table.a,v 0.1 86/04/01 15:13:41 ada Exp $ \n$Log:	symbol_table.a,v $\nRevision 0.1  86/04/01  15:13:41  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:47:05  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
documentation_snippet: "",
simple_types:    [
       {
       name: "Associativity",
       qualified_name: "Symbol_Table.Associativity",
       signature: "symbol_table.associativity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type  Associativity  is (Left_Associative, Right_Associative, \n                         Nonassociative, Undefined);",
       }   ,
       {
       name: "Grammar_Symbol",
       qualified_name: "Symbol_Table.Grammar_Symbol",
       signature: "symbol_table.grammar_symbol",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type  Grammar_Symbol is range -5_000..5_000;",
       }   ,
       {
       name: "Precedence",
       qualified_name: "Symbol_Table.Precedence",
       signature: "symbol_table.precedence",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type  Precedence     is range 0..5_000;",
       }   ,
       {
       name: "Symbol_Type",
       qualified_name: "Symbol_Table.Symbol_Type",
       signature: "symbol_table.symbol_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type  Symbol_Type    is  (Start, Nonterminal, Terminal);",
       }   ,
   ]
,}
---
