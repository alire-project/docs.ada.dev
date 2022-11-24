---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Script",
qualified_name: "GPR.Script",
signature: "gpr.script",
enclosing: "gpr",
is_private: false,
documentation: "This package provide services to build a build script in gprbuild.",
documentation_snippet: "",
constants:    [
       {
       name: "Build_Script_Option",
       qualified_name: "GPR.Script.Build_Script_Option",
       signature: "gpr.script.build_script_option",
       enclosing: "",
       is_private: false,
       documentation: "gprbuild switch to create a build script",
       documentation_snippet: "Build_Script_Option : constant String := \"--build-script=\";",
       }   ,
   ]
,variables:    [
       {
       name: "Build_Script_File",
       qualified_name: "GPR.Script.Build_Script_File",
       signature: "gpr.script.build_script_file",
       enclosing: "",
       is_private: false,
       documentation: "Build script file",
       documentation_snippet: "Build_Script_File : File_Type;",
       }   ,
       {
       name: "Build_Script_Name",
       qualified_name: "GPR.Script.Build_Script_Name",
       signature: "gpr.script.build_script_name",
       enclosing: "",
       is_private: false,
       documentation: "Path name of the build script",
       documentation_snippet: "Build_Script_Name : String_Access := null;",
       }   ,
   ]
,}
---
