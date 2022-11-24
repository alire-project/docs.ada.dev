---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Project_Provider",
qualified_name: "Libadalang.Project_Provider",
signature: "libadalang.project_provider",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Source_Files_Mode",
       qualified_name: "Libadalang.Project_Provider.Source_Files_Mode",
       signature: "libadalang.project_provider.source_files_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Files_Mode is\n  (Default, Root_Project, Whole_Project, Whole_Project_With_Runtime);",
       }   ,
   ]
,array_types:    [
       {
       name: "Provider_And_Projects_Array",
       qualified_name: "Libadalang.Project_Provider.Provider_And_Projects_Array",
       signature: "libadalang.project_provider.provider_and_projects_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Provider_And_Projects_Array is\n   array (Positive range <>) of Provider_And_Projects;",
       }   ,
   ]
,record_types:    [
       {
       name: "Provider_And_Projects",
       qualified_name: "Libadalang.Project_Provider.Provider_And_Projects",
       signature: "libadalang.project_provider.provider_and_projects",
       enclosing: "",
       is_private: false,
       documentation: "Associates one project unit provider with all the projects on which it\nhas visibility.\n\n@field Provider\n@field Projects",
       documentation_snippet: "type Provider_And_Projects is record\n   Provider : LAL.Unit_Provider_Reference;\n   Projects : Prj.Project_Array_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Provider_And_Projects_Array_Access",
       qualified_name: "Libadalang.Project_Provider.Provider_And_Projects_Array_Access",
       signature: "libadalang.project_provider.provider_and_projects_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Provider_And_Projects_Array_Access is\n   access all Provider_And_Projects_Array;",
       }   ,
   ]
,constants:    [
       {
       name: "Trace",
       qualified_name: "Libadalang.Project_Provider.Trace",
       signature: "libadalang.project_provider.trace",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Trace : constant GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LIBADALANG.PROJECT_PROVIDER\", GNATCOLL.Traces.From_Config);",
       }   ,
   ]
,}
---
