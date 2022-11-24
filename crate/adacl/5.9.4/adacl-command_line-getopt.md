---
crate: adacl
layout: gnatdoc
gnatdoc: {
name: "AdaCL.Command_Line.GetOpt",
qualified_name: "AdaCL.Command_Line.GetOpt",
signature: "adacl.command_line.getopt",
enclosing: "adacl.command_line",
is_private: false,
documentation: "\nAn opject oriented version of getopt made for Ada - thats without the C\nstyle uglines. If you are looking for a 100% compatible Version of\ngetopt see:\n\nAlso, unlike for exapmle GNAT.Command_Line this package is reentrant.\nAll internal states are kept inside the class instanz so two tasks can\nparse the commandline in parallel.\n\nlast not least we support GNU style commandline options.",
documentation_snippet: "",
simple_types:    [
       {
       name: "FoundFlag",
       qualified_name: "AdaCL.Command_Line.GetOpt.FoundFlag",
       signature: "adacl.command_line.getopt.foundflag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FoundFlag is (\n   EndOfOptions,\n   NoOption,\n   GNU_Style,\n   WithArgument,\n   WithoutArgument,\n   Error);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "AdaCL.Command_Line.GetOpt.Object",
       signature: "adacl.command_line.getopt.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Help_GNU",
       qualified_name: "AdaCL.Command_Line.GetOpt.Help_GNU",
       signature: "adacl.command_line.getopt.help_gnu",
       enclosing: "",
       is_private: false,
       documentation: "\nShort Option to request Help",
       documentation_snippet: "Help_GNU : constant String;",
       }   ,
       {
       name: "Help_Short",
       qualified_name: "AdaCL.Command_Line.GetOpt.Help_Short",
       signature: "adacl.command_line.getopt.help_short",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Help_Short : constant Character;",
       }   ,
   ]
,variables:    [
       {
       name: "Option_Argument",
       qualified_name: "AdaCL.Command_Line.GetOpt.Option_Argument",
       signature: "adacl.command_line.getopt.option_argument",
       enclosing: "",
       is_private: false,
       documentation: "\nCharacter with which all options start",
       documentation_snippet: "Option_Argument : Character renames Ada.Characters.Latin_1.Colon;",
       }   ,
       {
       name: "Option_Error",
       qualified_name: "AdaCL.Command_Line.GetOpt.Option_Error",
       signature: "adacl.command_line.getopt.option_error",
       enclosing: "",
       is_private: false,
       documentation: "\nOptions with Arguments.",
       documentation_snippet: "Option_Error : Character renames Ada.Characters.Latin_1.Question;",
       }   ,
       {
       name: "Option_Marker",
       qualified_name: "AdaCL.Command_Line.GetOpt.Option_Marker",
       signature: "adacl.command_line.getopt.option_marker",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Option_Marker : Character renames Ada.Characters.Latin_1.Hyphen;",
       }   ,
   ]
,}
---
