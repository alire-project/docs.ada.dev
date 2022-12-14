---
crate: ayacc
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Actions_File",
    qualified_name: "Actions_File",
    signature: "actions_file",
    enclosing: "",
    is_private: false,
    documentation: "								--\n  Standard file access routines for the file containing   -- \n  the procedure user_action which associates rules to the --\n  user executable code. 					--\n 								--  ",
    documentation_snippet: "",
    },
    {
    name: "Ayacc_File_Names",
    qualified_name: "Ayacc_File_Names",
    signature: "ayacc_file_names",
    enclosing: "",
    is_private: false,
    documentation: "The collection of all file names used by Ayacc --",
    documentation_snippet: "",
    },
    {
    name: "Error_Report_File",
    qualified_name: "Error_Report_File",
    signature: "error_report_file",
    enclosing: "",
    is_private: false,
    documentation: "\nTITLE:	package Error_Report_File\n   Output the code which allows users to see what the error token was.\n\nLANGUAGE:\n   Ada\n\nPERSONNEL:\n   AUTHOR: Benjamin Hurwitz\n   DATE: Jul 27 1990\n\nOVERVIEW:\n   Export the procedure Write_File which outputs all the code to the\n   file {base_name}_error_report.a\n\nUPDATES:",
    documentation_snippet: "",
    },
    {
    name: "Goto_File",
    qualified_name: "Goto_File",
    signature: "goto_file",
    enclosing: "",
    is_private: false,
    documentation: " $Header: /dc/uc/self/arcadia/ayacc/src/RCS/goto_file.a,v 1.2 1993/05/31 22:36:35 self Exp self $ \n $Log: goto_file.a,v $\n Revision 1.2  1993/05/31  22:36:35  self\n added exception handler when opening files\n\n Revision 1.1  1993/05/31  22:14:38  self\n Initial revision\n\nRevision 1.1  88/08/08  13:43:29  arcadia\nInitial revision\n\n Revision 0.1  86/04/01  15:04:27  ada\n  This version fixes some minor bugs with empty grammars \n  and $$ expansion. It also uses vads5.1b enhancements \n  such as pragma inline. \n \n \n Revision 0.0  86/02/19  18:36:31  ada\n \n These files comprise the initial version of Ayacc\n designed and implemented by David Taback and Deepak Tolani.\n Ayacc has been compiled and tested under the Verdix Ada compiler\n version 4.06 on a vax 11/750 running Unix 4.2BSD.\n  ",
    documentation_snippet: "",
    },
    {
    name: "LALR_Symbol_Info",
    qualified_name: "LALR_Symbol_Info",
    signature: "lalr_symbol_info",
    enclosing: "",
    is_private: false,
    documentation: "                                                                    --\nAuthors   : David Taback , Deepak Tolani                            --\nCopyright : 1987, University of California Irvine                   --\n                                                                    -- \nIf you    -- \nmodify the source code or if you have any suggestions or questions  -- \nregarding ayacc, we would like to hear from you. Our mailing        -- \naddresses are :                                                     -- \n    taback@icsc.uci.edu                                             -- \n    tolani@icsc.uci.edu                                             --   \n                                                                    --  ",
    documentation_snippet: "",
    },
    {
    name: "Lexical_Analyzer",
    qualified_name: "Lexical_Analyzer",
    signature: "lexical_analyzer",
    enclosing: "",
    is_private: false,
    documentation: "$Header: lexical_analyzer.a,v 0.1 86/04/01 15:05:14 ada Exp $\n$Log:	lexical_analyzer.a,v $\nRevision 0.1  86/04/01  15:05:14  ada\n This version fixes some minor bugs with empty grammars\n and $$ expansion. It also uses vads5.1b enhancements\n such as pragma inline.\n\n\nRevision 0.0  86/02/19  18:36:57  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.",
    documentation_snippet: "",
    },
    {
    name: "Lists",
    qualified_name: "Lists",
    signature: "lists",
    enclosing: "",
    is_private: false,
    documentation: "| This package provides singly linked lists with elements of type\n| ItemType, where ItemType is specified by a generic parameter.\n\n@formal Itemtype\n  | This is the data being manipulated.\n@formal Equal\n  | This allows the user to define\n  | equality on ItemType.  For instance\n  | if ItemType is an abstract type\n  | then equality is defined in terms of\n  | the abstract type.  If this function\n  | is not provided equality defaults to\n  | =.",
    documentation_snippet: "",
    },
    {
    name: "LR0_Machine",
    qualified_name: "LR0_Machine",
    signature: "lr0_machine",
    enclosing: "",
    is_private: false,
    documentation: "$Header: /dc/uc/self/tmp/gnat_ayacc_new/lr0bad/RCS/lr0_machine.ads,v 1.1 1995/02/16 17:28:09 self Exp self $ \n$Log: lr0_machine.ads,v $\nRevision 0.1  86/04/01  15:06:19  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:37:14  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
    documentation_snippet: "",
    },
    {
    name: "Options",
    qualified_name: "Options",
    signature: "options",
    enclosing: "",
    is_private: false,
    documentation: "$Header: options.a,v 0.1 86/04/01 15:08:15 ada Exp $\n$Log:	options.a,v $\nRevision 0.1  86/04/01  15:08:15  ada\n This version fixes some minor bugs with empty grammars\n and $$ expansion. It also uses vads5.1b enhancements\n such as pragma inline.\n\n\nRevision 0.0  86/02/19  18:37:34  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.",
    documentation_snippet: "",
    },
    {
    name: "Output_File",
    qualified_name: "Output_File",
    signature: "output_file",
    enclosing: "",
    is_private: false,
    documentation: "Module       : output_file.ada\nComponent of : ayacc\nVersion      : 1.2\nDate         : 11/21/86  12:31:54\nSCCS File    : disk21~/rschm/hasee/sccs/ayacc/sccs/sxoutput_file.ada",
    documentation_snippet: "",
    },
    {
    name: "Parse_Table",
    qualified_name: "Parse_Table",
    signature: "parse_table",
    enclosing: "",
    is_private: false,
    documentation: "This package build the shift reduce table and the goto table and\nwrites it to the shift_reduce_file, and goto_file. If the verbose option\nis set, the states generated and their coresponding actions are written\nto the verobose_file.\nThe parse table produced is an LALR(1) parse table.\nThe number of conflicts resulting from the grammar\ncan be determinied by calling the funciton REDUCE_REDUCE_CONFLICTS and\nSHIFT_REDUCE_CONFLICTS, after calling MAKE_PARSE_TABLE.",
    documentation_snippet: "",
    },
    {
    name: "Parse_Template_File",
    qualified_name: "Parse_Template_File",
    signature: "parse_template_file",
    enclosing: "",
    is_private: false,
    documentation: "$Header: parse_template_file.a,v 0.1 86/04/01 15:09:47 ada Exp $\n$Log:	parse_template_file.a,v $\nRevision 0.1  86/04/01  15:09:47  ada\n This version fixes some minor bugs with empty grammars\n and $$ expansion. It also uses vads5.1b enhancements\n such as pragma inline.\n\n\nRevision 0.0  86/02/19  18:40:09  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.",
    documentation_snippet: "",
    },
    {
    name: "Parser",
    qualified_name: "Parser",
    signature: "parser",
    enclosing: "",
    is_private: false,
    documentation: "Parse the declarations section  ",
    documentation_snippet: "",
    },
    {
    name: "Ragged",
    qualified_name: "Ragged",
    signature: "ragged",
    enclosing: "",
    is_private: false,
    documentation: "Cell and index should be private but for efficency and for subtle \nproblems that arise when type item is implemeted as a limited private \nin an external package, cell and index are kept visible.\n\n@formal Row_Index\n@formal Col_Index\n@formal Item\n@formal Null_Value",
    documentation_snippet: "",
    },
    {
    name: "Rule_Table",
    qualified_name: "Rule_Table",
    signature: "rule_table",
    enclosing: "",
    is_private: false,
    documentation: "This package is used to store and access the rules\nof the input grammar.",
    documentation_snippet: "",
    },
    {
    name: "Set_Pack",
    qualified_name: "Set_Pack",
    signature: "set_pack",
    enclosing: "",
    is_private: false,
    documentation: "$Header: set_pack.a,v 0.1 86/04/01 15:11:51 ada Exp $ \n$Log:	set_pack.a,v $\nRevision 0.1  86/04/01  15:11:51  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:41:22  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n \n\n@formal Universe\n@formal \"<\"",
    documentation_snippet: "",
    },
    {
    name: "Shift_Reduce_File",
    qualified_name: "Shift_Reduce_File",
    signature: "shift_reduce_file",
    enclosing: "",
    is_private: false,
    documentation: " $Header: /dc/uc/self/arcadia/ayacc/src/RCS/shift_reduce_file.a,v 1.2 1993/05/31 22:36:35 self Exp self $ \n $Log: shift_reduce_file.a,v $\n Revision 1.2  1993/05/31  22:36:35  self\n added exception handler when opening files\n\n Revision 1.1  1993/05/31  22:14:38  self\n Initial revision\n\nRevision 1.1  88/08/08  14:27:14  arcadia\nInitial revision\n\n Revision 0.1  86/04/01  15:12:13  ada\n  This version fixes some minor bugs with empty grammars \n  and $$ expansion. It also uses vads5.1b enhancements \n  such as pragma inline. \n \n \n Revision 0.0  86/02/19  18:41:42  ada\n \n These files comprise the initial version of Ayacc\n designed and implemented by David Taback and Deepak Tolani.\n Ayacc has been compiled and tested under the Verdix Ada compiler\n version 4.06 on a vax 11/750 running Unix 4.2BSD.\n  ",
    documentation_snippet: "",
    },
    {
    name: "Source_File",
    qualified_name: "Source_File",
    signature: "source_file",
    enclosing: "",
    is_private: false,
    documentation: ".  This package provides input from the source file to the lexical\n.  analyzer.\n.  UNGET will work to unget up to one character. You can unget more\n.  characters until you try to unget an EOLN where the exception\n.  PUSHBACK_ERROR is raised.\n.  The next character in the input stream\n.  can be looked at using PEEK_NEXT_CHAR without affecting the input\n.  stream.",
    documentation_snippet: "",
    },
    {
    name: "Stack_Pack",
    qualified_name: "Stack_Pack",
    signature: "stack_pack",
    enclosing: "",
    is_private: false,
    documentation: "                                                                    --\nAuthors   : David Taback , Deepak Tolani                            --\nCopyright : 1987, University of California Irvine                   --\n                                                                    -- \nIf you    -- \nmodify the source code or if you have any suggestions or questions  -- \nregarding ayacc, we would like to hear from you. Our mailing        -- \naddresses are :                                                     -- \n    taback@icsc.uci.edu                                             -- \n    tolani@icsc.uci.edu                                             --   \n                                                                    --  \n\n@formal Element",
    documentation_snippet: "",
    },
    {
    name: "stack_pkg",
    qualified_name: "stack_pkg",
    signature: "stack_pkg",
    enclosing: "",
    is_private: false,
    documentation: "| Overview:\n| This package provides the stack abstract data type.  Element type is\n| a generic formal parameter to the package.  There are no explicit\n| bounds on the number of objects that can be pushed onto a given stack.\n| All standard stack operations are provided.\n|\n| The following is a complete list of operations, written in the order\n| in which they appear in the spec.  Overloaded subprograms are followed\n| by (n), where n is the number of subprograms of that name.\n|\n| Constructors:\n|        create \n|        push\n|        pop (2)\n|        copy\n| Query Operations:\n|        top\n|        size\n|        is_empty\n| Heap Management: \n|        destroy\n\n@formal elem_type\n  | Component element type.",
    documentation_snippet: "",
    },
    {
    name: "STR_Pack",
    qualified_name: "STR_Pack",
    signature: "str_pack",
    enclosing: "",
    is_private: false,
    documentation: "This package contains the type declarations and procedures\nfor the minimal string minipulation needed by ayacc.",
    documentation_snippet: "",
    },
    {
    name: "string_pkg",
    qualified_name: "string_pkg",
    signature: "string_pkg",
    enclosing: "",
    is_private: false,
    documentation: "| Overview:\n| Package string_pkg exports an abstract data type, string_type.  A\n| string_type value is a sequence of characters.  The values have arbitrary\n| length.  For a value, s, with length, l, the individual characters are\n| numbered from 1 to l.  These values are immutable; characters cannot be\n| replaced or appended in a destructive fashion.\n|\n| In the documentation for this package, we are careful to distinguish\n| between string_type objects, which are Ada objects in the usual sense,\n| and string_type values, the members of this data abstraction as described\n| above.  A string_type value is said to be associated with, or bound to,\n| a string_type object after an assignment (:=) operation.\n|\n| The operations provided in this package fall into three categories:\n|\n| 1. Constructors:  These functions typically take one or more string_type\n|      objects as arguments.  They work with the values associated with\n|      these objects, and return new string_type values according to\n|      specification.  By a slight abuse of language, we will sometimes\n|      coerce from string_type objects to values for ease in description.\n|\n| 2. Heap Management:\n|      These operations (make_persistent, flush, mark, release) control the\n|      management of heap space.  Because string_type values are\n|      allocated on the heap, and the type is not limited, it is necessary\n|      for a user to assume some responsibility for garbage collection.\n|      String_type is not limited because of the convenience of\n|      the assignment operation, and the usefulness of being able to\n|      instantiate generic units that contain private type formals.\n|      ** Important: To use this package properly, it is necessary to read\n|      the descriptions of the operations in this section.\n|\n| 3. Queries:  These functions return information about the values\n|      that are associated with the argument objects.  The same conventions\n|      for description of operations used in (1) is adopted.\n|\n| A note about design decisions...  The decision to not make the type\n| limited causes two operations to be carried over from the representation.\n| These are the assignment operation, :=, and the \"equality\" operator, \"=\".\n| See the discussion at the beginning of the Heap Management section for a\n| discussion of :=.\n| See the spec for the first of the equal functions for a discussion of \"=\".\n|\n| The following is a complete list of operations, written in the order\n| in which they appear in the spec.  Overloaded subprograms are followed\n| by (n), where n is the number of subprograms of that name.\n|\n| 1. Constructors:\n|        Empty_String\n|        create\n|        \"&\" (3)\n|        substr\n|        splice\n|        insert (3)\n|        lower (2)\n|        upper (2)\n|        mixed (2)\n| 2. Heap Management:\n|        make_persistent (2)\n|        flush\n|        mark, release\n| 3. Queries:\n|        is_empty\n|        length\n|        value\n|        fetch\n|        equal (3)\n|        equivalent (3)\n|        \"<\" (3),\n|    \"<=\" (3)\n|        match_c\n|        match_not_c\n|        match_s (2)\n|        match_any (2)\n|        match_none (2)",
    documentation_snippet: "",
    },
    {
    name: "String_Scanner",
    qualified_name: "String_Scanner",
    signature: "string_scanner",
    enclosing: "",
    is_private: false,
    documentation: "| Functions for scanning tokens from strings.",
    documentation_snippet: "",
    },
    {
    name: "Symbol_Info",
    qualified_name: "Symbol_Info",
    signature: "symbol_info",
    enclosing: "",
    is_private: false,
    documentation: "\nThe following array declarations are used to compute the\nthe rules that have a particular symbol on the left hand\nside. NONTERMINAL_YIELD contains the rules and\nNONTERMINAL_YIELD_OFFSET contains the offset into the first array\nindexed by a particular nonterminal.  The user of this package\nshould not attempt to alter the contents of these arrays. They\nare visible in the spec only for efficiency reasons.",
    documentation_snippet: "",
    },
    {
    name: "Symbol_Table",
    qualified_name: "Symbol_Table",
    signature: "symbol_table",
    enclosing: "",
    is_private: false,
    documentation: "$Header: symbol_table.a,v 0.1 86/04/01 15:13:41 ada Exp $ \n$Log:	symbol_table.a,v $\nRevision 0.1  86/04/01  15:13:41  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:47:05  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
    documentation_snippet: "",
    },
    {
    name: "Tokens_File",
    qualified_name: "Tokens_File",
    signature: "tokens_file",
    enclosing: "",
    is_private: false,
    documentation: "$Header: tokens_file.a,v 0.1 86/04/01 15:14:22 ada Exp $ \n$Log:	tokens_file.a,v $\nRevision 0.1  86/04/01  15:14:22  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:54:11  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
    documentation_snippet: "",
    },
    {
    name: "Verbose_File",
    qualified_name: "Verbose_File",
    signature: "verbose_file",
    enclosing: "",
    is_private: false,
    documentation: "$Header: verbose_file.a,v 0.1 86/04/01 15:14:39 ada Exp $ \n$Log:	verbose_file.a,v $\nRevision 0.1  86/04/01  15:14:39  ada\n This version fixes some minor bugs with empty grammars \n and $$ expansion. It also uses vads5.1b enhancements \n such as pragma inline. \n\n\nRevision 0.0  86/02/19  18:54:29  ada\n\nThese files comprise the initial version of Ayacc\ndesigned and implemented by David Taback and Deepak Tolani.\nAyacc has been compiled and tested under the Verdix Ada compiler\nversion 4.06 on a vax 11/750 running Unix 4.2BSD.\n ",
    documentation_snippet: "",
    },
]
, subprograms: [
    {
    name: "Ayacc",
    qualified_name: "Ayacc",
    signature: "ayacc()$",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "procedure Ayacc",
    },
]
}
---
