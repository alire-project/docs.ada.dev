---
crate: ada_fuse
layout: gnatdoc
gnatdoc: {
name: "Fuse",
qualified_name: "Fuse",
signature: "fuse",
enclosing: "",
is_private: false,
documentation: "In order to create a filesystem instantiate Fuse.Main.\nFuse.General and Fuse.System will be instatiated through Main.\nIf you want to build a passthrough filesystem, you can use Fuse.Aux.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Log_Level_Type",
       qualified_name: "Fuse.Log_Level_Type",
       signature: "fuse.log_level_type",
       enclosing: "",
       is_private: false,
       documentation: "see Fuse.Main",
       documentation_snippet: "type Log_Level_Type is new Integer range 0..9;",
       }   ,
   ]
,record_types:    [
       {
       name: "Null_Data",
       qualified_name: "Fuse.Null_Data",
       signature: "fuse.null_data",
       enclosing: "",
       is_private: false,
       documentation: "Use for User_Data if not needed",
       documentation_snippet: "type Null_Data is null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Arguments_Type",
       qualified_name: "Fuse.Arguments_Type",
       signature: "fuse.arguments_type",
       enclosing: "",
       is_private: false,
       documentation: "This is used to pass command line arguments to Fuse.\nFill the Vector and pass it to Fuse.Main.Main.",
       documentation_snippet: "subtype Arguments_Type is String_Vectors.Vector;",
       }   ,
   ]
,}
---
