---
crate: simple_logging
layout: gnatdoc
gnatdoc: {
name: "Simple_Logging.Filtering",
qualified_name: "Simple_Logging.Filtering",
signature: "simple_logging.filtering",
enclosing: "simple_logging",
is_private: false,
documentation: "Filtering enables to accept/filter out messages that will get displayed.\nBy default, no filtering occurs.\nSee below how to configure the default filter.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Filtering_Modes",
       qualified_name: "Simple_Logging.Filtering.Filtering_Modes",
       signature: "simple_logging.filtering.filtering_modes",
       enclosing: "",
       is_private: false,
       documentation: "In blacklist mode, by default all passes but explicitly blacklisted.\nIn whitelist mode, nothing passes but whitelisted.\nEn each mode, you can further add exceptions to the list that operate\nin the contrary mode.\n\n@enum Blacklist\n@enum Whitelist",
       documentation_snippet: "type Filtering_Modes is (Blacklist, Whitelist);",
       }   ,
   ]
,variables:    [
       {
       name: "Accept_Message",
       qualified_name: "Simple_Logging.Filtering.Accept_Message",
       signature: "simple_logging.filtering.accept_message",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Accept_Message : access function (Message  : String;\n                                  Level    : Levels;\n                                  Entity   : String;\n                                  Location : String) return Boolean :=\n  Default_Filter'Access;",
       }   ,
       {
       name: "Mode",
       qualified_name: "Simple_Logging.Filtering.Mode",
       signature: "simple_logging.filtering.mode",
       enclosing: "",
       is_private: false,
       documentation: "MOde for the Default_Filter",
       documentation_snippet: "Mode : Filtering_Modes := Blacklist;",
       }   ,
   ]
,}
---
