---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Lexical_Analyzer",
qualified_name: "Lexical_Analyzer",
signature: "lexical_analyzer",
enclosing: "",
is_private: false,
documentation: "$Header: lexical_analyzer.a,v 0.1 86/04/01 15:05:14 ada Exp $\n$Log:	lexical_analyzer.a,v $\nRevision 0.1  86/04/01  15:05:14  ada\n This version fixes some minor bugs with empty grammars\n and $$ expansion. It also uses vads5.1b enhancements\n such as pragma inline.\n\n\nRevision 0.0  86/02/19  18:36:57  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Ayacc_Token",
       qualified_name: "Lexical_Analyzer.Ayacc_Token",
       signature: "lexical_analyzer.ayacc_token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "    type Ayacc_Token is\n	(Token, Start,\n	 Left, Right, Nonassoc, Prec,\n         With_Clause, Use_Clause, Unit_Clause,\n	 Identifier, Character_Literal,\n         Comma, Colon, Semicolon, Vertical_Bar, Left_Brace,\n	 Mark, Eof_Token);",
       }   ,
   ]
,}
---
