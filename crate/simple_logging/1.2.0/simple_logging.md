---
crate: simple_logging
layout: gnatdoc
gnatdoc: {
name: "Simple_Logging",
qualified_name: "Simple_Logging",
signature: "simple_logging",
enclosing: "",
is_private: false,
documentation: "NOTE: this library is thread-unsafe. Using it with multithreaded\napplications will likely result in mangled output.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Levels",
       qualified_name: "Simple_Logging.Levels",
       signature: "simple_logging.levels",
       enclosing: "",
       is_private: false,
       documentation: "From most important to less important\nOr, from less verbose to more verbose\n\n@enum Always\n@enum Error\n@enum Warning\n@enum Info\n@enum Detail\n@enum Debug",
       documentation_snippet: "type Levels is (Always,\n                Error,\n                Warning,\n                Info,\n                Detail,\n                Debug);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Ongoing",
       qualified_name: "Simple_Logging.Ongoing",
       signature: "simple_logging.ongoing",
       enclosing: "",
       is_private: false,
       documentation: "The status line is used to present an ongoing activity. This is done\nthrough a scoped type. Several nested statuses can be created, and the\ntrailing '...' is added by this prompt. The rest of logging subprograms\nwill emit normally over the status line.",
       documentation_snippet: "type Ongoing (<>) is tagged limited private;",
       }   ,
   ]
,variables:    [
       {
       name: "ASCII_Only",
       qualified_name: "Simple_Logging.ASCII_Only",
       signature: "simple_logging.ascii_only",
       enclosing: "",
       is_private: false,
       documentation: "Restrict the deliberate use of non-ASCII chars (currently only for the\nbusy status spinner).",
       documentation_snippet: "ASCII_Only : Boolean := True;",
       }   ,
       {
       name: "Is_TTY",
       qualified_name: "Simple_Logging.Is_TTY",
       signature: "simple_logging.is_tty",
       enclosing: "",
       is_private: false,
       documentation: "Set this to True when you know log is not being redirected. This flag\nsuppresses the use of busy statuses (see below) which, by relying\non ASCII.CR, will greatly pollute logfiles.",
       documentation_snippet: "Is_TTY : Boolean := False;",
       }   ,
       {
       name: "Level",
       qualified_name: "Simple_Logging.Level",
       signature: "simple_logging.level",
       enclosing: "",
       is_private: false,
       documentation: "Any message at the same level or below will be output to console",
       documentation_snippet: "Level : Levels := Info;",
       }   ,
   ]
,}
---
