---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Env",
qualified_name: "GPR.Env",
signature: "gpr.env",
enclosing: "gpr",
is_private: false,
documentation: "This package implements services for Project-aware tools, mostly related\nto the environment (configuration pragma files, path files, mapping files).",
documentation_snippet: "",
simple_types:    [
       {
       name: "Project_Search_Path",
       qualified_name: "GPR.Env.Project_Search_Path",
       signature: "gpr.env.project_search_path",
       enclosing: "",
       is_private: false,
       documentation: "An abstraction of the project path. This object provides subprograms\nto search for projects on the path (and caches the results to improve\nefficiency).",
       documentation_snippet: "type Project_Search_Path is private;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Project_Search_Path",
       qualified_name: "GPR.Env.No_Project_Search_Path",
       signature: "gpr.env.no_project_search_path",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Project_Search_Path : constant Project_Search_Path;",
       }   ,
   ]
,}
---
