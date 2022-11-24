---
crate: ini_files
layout: gnatdoc
gnatdoc: {
name: "Config",
qualified_name: "Config",
signature: "config",
enclosing: "",
is_private: false,
documentation: "Created On      : Fri Apr 26 08:09:14 1996",
documentation_snippet: "",
simple_types:    [
       {
       name: "Type_Mismatch_Action",
       qualified_name: "Config.Type_Mismatch_Action",
       signature: "config.type_mismatch_action",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Type_Mismatch_Action is (Raise_Data_Error,\n                              Print_Warning,\n                              Be_Quiet);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Configuration",
       qualified_name: "Config.Configuration",
       signature: "config.configuration",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Configuration is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Section_List",
       qualified_name: "Config.Section_List",
       signature: "config.section_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Section_List is String_Vector.Vector;",
       }   ,
   ]
,constants:    [
       {
       name: "LF",
       qualified_name: "Config.LF",
       signature: "config.lf",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "LF : constant Character := Character'Val (10);",
       }   ,
       {
       name: "web",
       qualified_name: "Config.web",
       signature: "config.web",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at one of those locations.",
       documentation_snippet: "web     : constant String := \"https://sourceforge.net/projects/ini-files/\";",
       }   ,
       {
       name: "web_alt",
       qualified_name: "Config.web_alt",
       signature: "config.web_alt",
       enclosing: "",
       is_private: false,
       documentation: "Hopefully the latest version is at one of those locations.",
       documentation_snippet: "web_alt : constant String := \"https://github.com/zertovitch/ini-files\";",
       }   ,
   ]
,}
---
