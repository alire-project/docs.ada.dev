---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Utils.GNAT",
qualified_name: "Gen.Utils.GNAT",
signature: "gen.utils.gnat",
enclosing: "gen.utils",
is_private: false,
documentation: "Directory which contains the GNAT project files installed on the system.\nThis is overridden by the configuration property 'generator.gnat.projects.dir'.",
documentation_snippet: "",
record_types:    [
       {
       name: "Project_Info",
       qualified_name: "Gen.Utils.GNAT.Project_Info",
       signature: "gen.utils.gnat.project_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Project_Info is record\n   Path        : UString;\n   Name        : UString;\n   Is_Abstract : Boolean := False;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "ADA_PROJECT_PATH_NAME",
       qualified_name: "Gen.Utils.GNAT.ADA_PROJECT_PATH_NAME",
       signature: "gen.utils.gnat.ada_project_path_name",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADA_PROJECT_PATH_NAME    : constant String := \"ADA_PROJECT_PATH\";",
       }   ,
       {
       name: "DEFAULT_GNAT_PROJECT_DIR",
       qualified_name: "Gen.Utils.GNAT.DEFAULT_GNAT_PROJECT_DIR",
       signature: "gen.utils.gnat.default_gnat_project_dir",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DEFAULT_GNAT_PROJECT_DIR : constant String := \"/usr/lib/gnat\";",
       }   ,
   ]
,}
---
