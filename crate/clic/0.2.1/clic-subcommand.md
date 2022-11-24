---
crate: clic
layout: gnatdoc
gnatdoc: {
name: "CLIC.Subcommand",
qualified_name: "CLIC.Subcommand",
signature: "clic.subcommand",
enclosing: "clic",
is_private: false,
documentation: "This root package defines the interface types to be used in the\nSubcommand. See CLIC.Subcommand.Instance to create the parser/executor.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Switch_Parsing_Kind",
       qualified_name: "CLIC.Subcommand.Switch_Parsing_Kind",
       signature: "clic.subcommand.switch_parsing_kind",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Parse_All\n  All the sub-command arguments are parsed for switches\n@enum Before_Double_Dash\n  Only the arguments before a potential \"--\" are parsed for switches.\n  The remaining switches and arguments are passed to the Args parameter\n  of the Execute primitive.\n@enum All_As_Args",
       documentation_snippet: "type Switch_Parsing_Kind is\n  (Parse_All,\n   Before_Double_Dash,\n   All_As_Args\n  );",
       }   ,
       {
       name: "Switches_Configuration",
       qualified_name: "CLIC.Subcommand.Switches_Configuration",
       signature: "clic.subcommand.switches_configuration",
       enclosing: "",
       is_private: false,
       documentation: "This is a wrapper around GNAT.Command_Line.Command_Line_Configuration\nto provide extra features such as duplicate switch detection and custom\nusage format. The \"Define_Switch\" procedure below work exactly like the\nGNAT.Command_Line ones.",
       documentation_snippet: "type Switches_Configuration is limited private;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Command",
       qualified_name: "CLIC.Subcommand.Command",
       signature: "clic.subcommand.command",
       enclosing: "",
       is_private: false,
       documentation: "This type encapsulates configuration and execution of a specific\ncommand. It also has help-related subprograms.",
       documentation_snippet: "type Command is limited interface;",
       }   ,
       {
       name: "Help_Topic",
       qualified_name: "CLIC.Subcommand.Help_Topic",
       signature: "clic.subcommand.help_topic",
       enclosing: "",
       is_private: false,
       documentation: "This type encapsulate the content of an \"help topic\", i.e. a piece of\ndocumentation that can displayed from the command line.",
       documentation_snippet: "type Help_Topic is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Command_Access",
       qualified_name: "CLIC.Subcommand.Command_Access",
       signature: "clic.subcommand.command_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Access is access all Command'Class;",
       }   ,
       {
       name: "Help_Topic_Access",
       qualified_name: "CLIC.Subcommand.Help_Topic_Access",
       signature: "clic.subcommand.help_topic_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Help_Topic_Access is access all Help_Topic'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Identifier",
       qualified_name: "CLIC.Subcommand.Identifier",
       signature: "clic.subcommand.identifier",
       enclosing: "",
       is_private: false,
       documentation: "-----------\n Command --\n-----------",
       documentation_snippet: "subtype Identifier is String\n  with Predicate => (for all C of Identifier\n                     => C in 'a' .. 'z' | 'A' .. 'Z' |\n                             '0' .. '9' | '-' | '.' | '_');",
       }   ,
   ]
,}
---
