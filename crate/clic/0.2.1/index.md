---
crate: clic
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "CLIC",
    qualified_name: "CLIC",
    signature: "clic",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Command_Line",
    qualified_name: "CLIC.Command_Line",
    signature: "clic.command_line",
    enclosing: "clic",
    is_private: false,
    documentation: "-----------\n Parsing --\n-----------",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Config",
    qualified_name: "CLIC.Config",
    signature: "clic.config",
    enclosing: "clic",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Config.Edit",
    qualified_name: "CLIC.Config.Edit",
    signature: "clic.config.edit",
    enclosing: "clic.config",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Config.Info",
    qualified_name: "CLIC.Config.Info",
    signature: "clic.config.info",
    enclosing: "clic.config",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Config.Load",
    qualified_name: "CLIC.Config.Load",
    signature: "clic.config.load",
    enclosing: "clic.config",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Subcommand",
    qualified_name: "CLIC.Subcommand",
    signature: "clic.subcommand",
    enclosing: "clic",
    is_private: false,
    documentation: "This root package defines the interface types to be used in the\nSubcommand. See CLIC.Subcommand.Instance to create the parser/executor.",
    documentation_snippet: "",
    },
    {
    name: "CLIC.Subcommand.Instance",
    qualified_name: "CLIC.Subcommand.Instance",
    signature: "clic.subcommand.instance",
    enclosing: "clic.subcommand",
    is_private: false,
    documentation: "Instantiate this package to create a sub-command parser/executor\n\n@formal Main_Command_Name\n  Name of the main command or program\n@formal Version\n  Version of the program\n@formal Set_Global_Switches\n  This procedure should define the global switches using the\n  Register_Switch procedures of the CLIC.Subcommand package.\n@formal Put\n  Used to print help and usage\n@formal Put_Line\n  Used to print help and usage\n@formal Put_Error\n  Used to print errors\n@formal Error_Exit\n  Used to signal that the program should terminate with the give error\n  code. Typicaly use GNAT.OS_Lib.OS_Exit.\n  The procedures below are used to format the output such as usage and\n  help. Use CLIC.Subcommand.No_TTY if you don't want or need formating.\n@formal TTY_Chapter\n@formal TTY_Description\n@formal TTY_Version\n@formal TTY_Underline\n@formal TTY_Emph",
    documentation_snippet: "",
    },
    {
    name: "CLIC.TTY",
    qualified_name: "CLIC.TTY",
    signature: "clic.tty",
    enclosing: "clic",
    is_private: false,
    documentation: "Color/Formatting related subprograms. These won't have any\neffect if a redirection of output is detected, or if global\nflag Simple_Logging.Is_TTY is false.",
    documentation_snippet: "",
    },
    {
    name: "CLIC.User_Input",
    qualified_name: "CLIC.User_Input",
    signature: "clic.user_input",
    enclosing: "clic",
    is_private: false,
    documentation: "-----------------\n Interactivity --\n-----------------",
    documentation_snippet: "",
    },
    {
    name: "Clic_Config",
    qualified_name: "Clic_Config",
    signature: "clic_config",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
]
}
---