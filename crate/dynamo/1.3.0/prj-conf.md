---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Prj.Conf",
qualified_name: "Prj.Conf",
signature: "prj.conf",
enclosing: "prj",
is_private: false,
documentation: "The following package manipulates the configuration files",
documentation_snippet: "",
access_types:    [
       {
       name: "Config_File_Hook",
       qualified_name: "Prj.Conf.Config_File_Hook",
       signature: "prj.conf.config_file_hook",
       enclosing: "",
       is_private: false,
       documentation: "Hook called after the config file has been parsed. This lets the\napplication do last minute changes to it (GPS uses this to add the\ndefault naming schemes for instance). At that point, the config file\nhas not been applied to the project yet. When no config file was found,\nand automatic generation is disabled, it is possible that Config_File\nis set to Empty_Node when this procedure is called. You can then decide\nto create a new config file if you need.\n\n@param Config_File\n@param Project_Node_Tree",
       documentation_snippet: "type Config_File_Hook is access procedure\n  (Config_File       : in out Prj.Tree.Project_Node_Id;\n   Project_Node_Tree : Prj.Tree.Project_Node_Tree_Ref);",
       }   ,
   ]
,constants:    [
       {
       name: "No_Configuration_File",
       qualified_name: "Prj.Conf.No_Configuration_File",
       signature: "prj.conf.no_configuration_file",
       enclosing: "",
       is_private: false,
       documentation: "When specified as a parameter Config_File_Name in the procedures below,\nno existing configuration project file is parsed. This is used by\ngnatmake, gnatclean and the GNAT driver to avoid parsing an existing\ndefault configuration project file.",
       documentation_snippet: "No_Configuration_File : constant String := \"/\";",
       }   ,
   ]
,}
---
