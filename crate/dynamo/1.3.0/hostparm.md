---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Hostparm",
qualified_name: "Hostparm",
signature: "hostparm",
enclosing: "",
is_private: false,
documentation: "-------------------\n HOST Parameters --\n-------------------",
documentation_snippet: "",
constants:    [
       {
       name: "Direct_Separator",
       qualified_name: "Hostparm.Direct_Separator",
       signature: "hostparm.direct_separator",
       enclosing: "",
       is_private: false,
       documentation: "Normalized string to access current directory",
       documentation_snippet: "Direct_Separator : constant Character;",
       }   ,
       {
       name: "Exclude_Missing_Objects",
       qualified_name: "Hostparm.Exclude_Missing_Objects",
       signature: "hostparm.exclude_missing_objects",
       enclosing: "",
       is_private: false,
       documentation: "If set to true, gnatbind will exclude from consideration all\nnon-existent .o files.",
       documentation_snippet: "Exclude_Missing_Objects : constant Boolean := True;",
       }   ,
       {
       name: "Max_Line_Length",
       qualified_name: "Hostparm.Max_Line_Length",
       signature: "hostparm.max_line_length",
       enclosing: "",
       is_private: false,
       documentation: "Maximum source line length. By default we set it to the maximum\nvalue that can be supported, which is given by the range of the\nColumn_Number type. We subtract 1 because need to be able to\nhave a valid Column_Number equal to Max_Line_Length to represent\nthe location of a \"line too long\" error.\n\n200 is the minimum value required (RM 2.2(15)). The value set here\ncan be reduced by the explicit use of the -gnatyM style switch.",
       documentation_snippet: "Max_Line_Length : constant :=\n  Types.Column_Number'Pred (Types.Column_Number'Last);",
       }   ,
       {
       name: "Max_Name_Length",
       qualified_name: "Hostparm.Max_Name_Length",
       signature: "hostparm.max_name_length",
       enclosing: "",
       is_private: false,
       documentation: "Maximum length of unit name (including all dots, and \" (spec)\") and\nof file names in the library, must be at least Max_Line_Length, but\ncan be larger.",
       documentation_snippet: "Max_Name_Length : constant := 1024;",
       }   ,
       {
       name: "Normalized_CWD",
       qualified_name: "Hostparm.Normalized_CWD",
       signature: "hostparm.normalized_cwd",
       enclosing: "",
       is_private: false,
       documentation: "Normalized string to access current directory",
       documentation_snippet: "Normalized_CWD : constant String := \".\" & Direct_Separator;",
       }   ,
       {
       name: "Tag_Errors",
       qualified_name: "Hostparm.Tag_Errors",
       signature: "hostparm.tag_errors",
       enclosing: "",
       is_private: false,
       documentation: "If set to true, then brief form error messages will be prefaced by\nthe string \"error:\". Used as default for Opt.Unique_Error_Tag.",
       documentation_snippet: "Tag_Errors : constant Boolean := False;",
       }   ,
   ]
,}
---
