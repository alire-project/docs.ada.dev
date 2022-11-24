---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "MLib",
qualified_name: "MLib",
signature: "mlib",
enclosing: "",
is_private: false,
documentation: "This package provides the core high level routines used by GNATMLIB\nand GNATMAKE to build libraries",
documentation_snippet: "",
access_types:    [
       {
       name: "Fail_Proc",
       qualified_name: "MLib.Fail_Proc",
       signature: "mlib.fail_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fail_Proc is access procedure (S1 : String);",
       }   ,
   ]
,constants:    [
       {
       name: "Max_Characters_In_Library_Name",
       qualified_name: "MLib.Max_Characters_In_Library_Name",
       signature: "mlib.max_characters_in_library_name",
       enclosing: "",
       is_private: false,
       documentation: "Maximum number of characters in a library name.\nUsed by Check_Library_Name below.",
       documentation_snippet: "Max_Characters_In_Library_Name : constant := 20;",
       }   ,
       {
       name: "No_Argument",
       qualified_name: "MLib.No_Argument",
       signature: "mlib.no_argument",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Argument      : constant String_List_Access := No_Argument_List'Access;",
       }   ,
   ]
,variables:    [
       {
       name: "Fail",
       qualified_name: "MLib.Fail",
       signature: "mlib.fail",
       enclosing: "",
       is_private: false,
       documentation: "This procedure is used in the MLib hierarchy, instead of\ndirectly calling Osint.Fail.\nIt is redirected to Make.Make_Failed by gnatmake.",
       documentation_snippet: "Fail : Fail_Proc := Osint.Fail'Access;",
       }   ,
       {
       name: "No_Argument_List",
       qualified_name: "MLib.No_Argument_List",
       signature: "mlib.no_argument_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Argument_List : aliased String_List := (1 .. 0 => null);",
       }   ,
   ]
,}
---
