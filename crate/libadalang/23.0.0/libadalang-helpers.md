---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Helpers",
qualified_name: "Libadalang.Helpers",
signature: "libadalang.helpers",
enclosing: "libadalang",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
packages:    [
       {
       name: "App",
       qualified_name: "Libadalang.Helpers.App",
       signature: "libadalang.helpers.app",
       enclosing: "libadalang.helpers",
       is_private: false,
       documentation: "\n@formal Name\n  Name for the application. Used to create the GNATCOLL trace.\n@formal Description\n  Description for the application. Will be used in the help string.\n@formal Enable_Parallelism\n  If True, add a -j/--jobs command line option to allow multiple jobs\n  to run in parallel. In this mode, we create one analysis context per\n  job, and the files to process are distributed on each job. All the\n  callbacks below are called concurrently in all jobs:\n  \n  First, the main task calls App_Setup. Then all jobs start:\n  \n    * Job 1 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 2 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 3 calls ...\n  \n  Finally, once all jobs are done, the main task calls\n  App_Post_Process.\n@formal App_Setup\n  This procedure is called right after command line options are parsed,\n  the project is loaded (if present) and the list of files to process\n  is computed.\n@formal Job_Setup\n  This procedure will be called right before going through units.  If a\n  project was loaded, Project refers to it, otherwise it is null.\n@formal Process_Unit\n  This procedure will be called once right after a unit is parsed\n@formal Job_Post_Process\n  This procedure will be called once after all units have been parsed.\n  Note it will be called once per job.\n@formal App_Post_Process\n  This procedure is called once all jobs are done",
       documentation_snippet: "",
packages:           [
              {
              name: "Args",
              qualified_name: "Libadalang.Helpers.App.Args",
              signature: "libadalang.helpers.app.args",
              enclosing: "libadalang.helpers.app",
              is_private: false,
              documentation: "",
              documentation_snippet: "",
variables:                  [
                     {
                     name: "Parser",
                     qualified_name: "Libadalang.Helpers.App.Args.Parser",
                     signature: "libadalang.helpers.app.args.parser",
                     enclosing: "",
                     is_private: false,
                     documentation: "Argument parser for your application. Supports a set of default\noptions. You can add your own on this parser.",
                     documentation_snippet: "Parser : Argument_Parser := Create_Argument_Parser\n  (Help => Description);",
                     }                 ,
                 ]
,              }          ,
          ]
,constants:           [
              {
              name: "Trace",
              qualified_name: "Libadalang.Helpers.App.Trace",
              signature: "libadalang.helpers.app.trace",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "Trace : constant GNATCOLL.Traces.Trace_Handle :=\n   GNATCOLL.Traces.Create\n     (\"LIBADALANG.APP.\" & Name, GNATCOLL.Traces.From_Config);",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Job_ID",
       qualified_name: "Libadalang.Helpers.Job_ID",
       signature: "libadalang.helpers.job_id",
       enclosing: "",
       is_private: false,
       documentation: "Identifier for a job in App. Unless Enable_Parallelism is False, there\nis only one job, whose ID is 1. If there are multiple jobs, their IDs go\nfrom 1 up to the number of jobs.",
       documentation_snippet: "type Job_ID is new Positive;",
       }   ,
       {
       name: "Source_Provider_Kind",
       qualified_name: "Libadalang.Helpers.Source_Provider_Kind",
       signature: "libadalang.helpers.source_provider_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Provider_Kind is (Default, Project_File, Auto_Dir);",
       }   ,
   ]
,array_types:    [
       {
       name: "App_Job_Context_Array",
       qualified_name: "Libadalang.Helpers.App_Job_Context_Array",
       signature: "libadalang.helpers.app_job_context_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type App_Job_Context_Array is array (Job_ID range <>) of App_Job_Context;",
       }   ,
   ]
,record_types:    [
       {
       name: "App_Context",
       qualified_name: "Libadalang.Helpers.App_Context",
       signature: "libadalang.helpers.app_context",
       enclosing: "",
       is_private: false,
       documentation: "Context information for the whole application\n\n@field Provider",
       documentation_snippet: "type App_Context is record\n   Provider : Source_Provider;\nend record;",
       }   ,
       {
       name: "App_Job_Context",
       qualified_name: "Libadalang.Helpers.App_Job_Context",
       signature: "libadalang.helpers.app_job_context",
       enclosing: "",
       is_private: false,
       documentation: "Context information for a single job\n\n@field ID\n  Identifier for this job\n@field App_Ctx\n  Reference to the app-wide context\n@field Analysis_Ctx\n  Context to analyze source file (each job gets its own context)\n@field Units_Processed\n  List of analysis units that this job processed so far\n@field Aborted",
       documentation_snippet: "type App_Job_Context is record\n   ID : Job_ID;\n   App_Ctx : not null access constant App_Context;\n   Analysis_Ctx : Analysis_Context;\n   Units_Processed : Unit_Vectors.Vector;\n   Aborted : Boolean;\nend record;",
       }   ,
       {
       name: "Source_Provider",
       qualified_name: "Libadalang.Helpers.Source_Provider",
       signature: "libadalang.helpers.source_provider",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Source_Provider\n  (Kind : Source_Provider_Kind := Source_Provider_Kind'First) is\nrecord\n   case Kind is\n      when Default =>\n         null;\n      when Project_File =>\n         Project : GNATCOLL.Projects.Project_Tree_Access;\n      when Auto_Dir =>\n         Dirs, Found_Files : String_Vectors.Vector;\n   end case;\nend record;",
       }   ,
   ]
,}
---
