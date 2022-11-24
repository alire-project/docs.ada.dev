---
crate: clic
layout: gnatdoc
gnatdoc: {
name: "CLIC.Command_Line",
qualified_name: "CLIC.Command_Line",
signature: "clic.command_line",
enclosing: "clic",
is_private: false,
documentation: "-----------\n Parsing --\n-----------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Command_Line",
       qualified_name: "CLIC.Command_Line.Command_Line",
       signature: "clic.command_line.command_line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Line is private;",
       }   ,
       {
       name: "Command_Line_Configuration",
       qualified_name: "CLIC.Command_Line.Command_Line_Configuration",
       signature: "clic.command_line.command_line_configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Line_Configuration is private;",
       }   ,
       {
       name: "Command_Line_Iterator",
       qualified_name: "CLIC.Command_Line.Command_Line_Iterator",
       signature: "clic.command_line.command_line_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Line_Iterator is private;",
       }   ,
       {
       name: "Expansion_Iterator",
       qualified_name: "CLIC.Command_Line.Expansion_Iterator",
       signature: "clic.command_line.expansion_iterator",
       enclosing: "",
       is_private: false,
       documentation: "Type used during expansion of file names",
       documentation_snippet: "type Expansion_Iterator is limited private;",
       }   ,
       {
       name: "Opt_Parser",
       qualified_name: "CLIC.Command_Line.Opt_Parser",
       signature: "clic.command_line.opt_parser",
       enclosing: "",
       is_private: false,
       documentation: "This object is responsible for parsing a list of arguments, which by\ndefault are the standard command line arguments from Ada.Command_Line.\nThis is really a pointer to actual data, which must therefore be\ninitialized through a call to Initialize_Option_Scan, and must be freed\nwith a call to Free.\n\nAs a special case, Command_Line_Parser does not need to be either\ninitialized or free-ed.",
       documentation_snippet: "type Opt_Parser is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Switch_Handler",
       qualified_name: "CLIC.Command_Line.Switch_Handler",
       signature: "clic.command_line.switch_handler",
       enclosing: "",
       is_private: false,
       documentation: "Called when a switch is found on the command line. Switch includes\nany leading '-' that was specified in Define_Switch. This is slightly\ndifferent from the functional version of Getopt above, for which\nFull_Switch omits the first leading '-'.\n\n@param Switch\n@param Parameter\n@param Section",
       documentation_snippet: "type Switch_Handler is access procedure\n  (Switch    : String;\n   Parameter : String;\n   Section   : String);",
       }   ,
       {
       name: "Value_Callback",
       qualified_name: "CLIC.Command_Line.Value_Callback",
       signature: "clic.command_line.value_callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Callback is access procedure (Switch, Value : String);",
       }   ,
   ]
,constants:    [
       {
       name: "Command_Line_Parser",
       qualified_name: "CLIC.Command_Line.Command_Line_Parser",
       signature: "clic.command_line.command_line_parser",
       enclosing: "",
       is_private: false,
       documentation: "This object is responsible for parsing a list of arguments, which by\ndefault are the standard command line arguments from Ada.Command_Line.\nThis is really a pointer to actual data, which must therefore be\ninitialized through a call to Initialize_Option_Scan, and must be freed\nwith a call to Free.\n\nAs a special case, Command_Line_Parser does not need to be either\ninitialized or free-ed.",
       documentation_snippet: "Command_Line_Parser : constant Opt_Parser;",
       }   ,
   ]
,}
---
