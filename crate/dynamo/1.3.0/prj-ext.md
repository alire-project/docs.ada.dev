---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Ext",
qualified_name: "Prj.Ext",
signature: "prj.ext",
enclosing: "prj",
is_private: false,
documentation: "-----------------------\n External References --\n-----------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "External_References",
       qualified_name: "Prj.Ext.External_References",
       signature: "prj.ext.external_references",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type External_References is private;",
       }   ,
       {
       name: "External_Source",
       qualified_name: "Prj.Ext.External_Source",
       signature: "prj.ext.external_source",
       enclosing: "",
       is_private: false,
       documentation: "Indicates where was the value of an external reference defined. They are\nprioritized in that order, so that a user can always use the command\nline to override a value coming from his environment, or an environment\nvariable to override a value defined in an aggregate project through the\n\"for External()...\" attribute.\n\n@enum From_Command_Line\n@enum From_Environment\n@enum From_External_Attribute",
       documentation_snippet: "type External_Source is\n  (From_Command_Line,\n   From_Environment,\n   From_External_Attribute);",
       }   ,
   ]
,constants:    [
       {
       name: "No_External_Refs",
       qualified_name: "Prj.Ext.No_External_Refs",
       signature: "prj.ext.no_external_refs",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_External_Refs : constant External_References;",
       }   ,
   ]
,}
---
