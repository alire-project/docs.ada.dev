---
crate: clic
layout: gnatdoc
gnatdoc: {
name: "CLIC.Config",
qualified_name: "CLIC.Config",
signature: "clic.config",
enclosing: "clic",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Instance",
       qualified_name: "CLIC.Config.Instance",
       signature: "clic.config.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance is tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Check_Import",
       qualified_name: "CLIC.Config.Check_Import",
       signature: "clic.config.check_import",
       enclosing: "",
       is_private: false,
       documentation: "Return False when a Key/Value combination is not valid. Can be used to\ncheck formating of string value like email address for instance.\n\n@param Key\n@param Value\n\n@return",
       documentation_snippet: "type Check_Import is\n  access function (Key : Config_Key; Value : TOML.TOML_Value)\n                   return Boolean;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Config_Key",
       qualified_name: "CLIC.Config.Config_Key",
       signature: "clic.config.config_key",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Config_Key is String\n  with Dynamic_Predicate => Is_Valid_Config_Key (Config_Key);",
       }   ,
   ]
,}
---
