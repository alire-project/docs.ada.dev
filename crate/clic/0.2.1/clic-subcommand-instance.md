---
crate: clic
layout: gnatdoc
gnatdoc: {
name: "CLIC.Subcommand.Instance",
qualified_name: "CLIC.Subcommand.Instance",
signature: "clic.subcommand.instance",
enclosing: "clic.subcommand",
is_private: false,
documentation: "Instantiate this package to create a sub-command parser/executor\n\n@formal Main_Command_Name\n  Name of the main command or program\n@formal Version\n  Version of the program\n@formal Set_Global_Switches\n  This procedure should define the global switches using the\n  Register_Switch procedures of the CLIC.Subcommand package.\n@formal Put\n  Used to print help and usage\n@formal Put_Line\n  Used to print help and usage\n@formal Put_Error\n  Used to print errors\n@formal Error_Exit\n  Used to signal that the program should terminate with the give error\n  code. Typicaly use GNAT.OS_Lib.OS_Exit.\n  The procedures below are used to format the output such as usage and\n  help. Use CLIC.Subcommand.No_TTY if you don't want or need formating.\n@formal TTY_Chapter\n@formal TTY_Description\n@formal TTY_Version\n@formal TTY_Underline\n@formal TTY_Emph",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Builtin_Help",
       qualified_name: "CLIC.Subcommand.Instance.Builtin_Help",
       signature: "clic.subcommand.instance.builtin_help",
       enclosing: "",
       is_private: false,
       documentation: "Use Register (new Builtin_Help); to provide a build-in help command",
       documentation_snippet: "type Builtin_Help is new Command with private;",
       }   ,
   ]
,}
---
