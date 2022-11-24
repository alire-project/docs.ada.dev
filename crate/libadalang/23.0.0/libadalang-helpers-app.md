---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "App",
qualified_name: "Libadalang.Helpers.App",
signature: "libadalang.helpers.app",
enclosing: "libadalang.helpers",
is_private: false,
documentation: "\n@formal Name\n  Name for the application. Used to create the GNATCOLL trace.\n@formal Description\n  Description for the application. Will be used in the help string.\n@formal Enable_Parallelism\n  If True, add a -j/--jobs command line option to allow multiple jobs\n  to run in parallel. In this mode, we create one analysis context per\n  job, and the files to process are distributed on each job. All the\n  callbacks below are called concurrently in all jobs:\n  \n  First, the main task calls App_Setup. Then all jobs start:\n  \n    * Job 1 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 2 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 3 calls ...\n  \n  Finally, once all jobs are done, the main task calls\n  App_Post_Process.\n@formal App_Setup\n  This procedure is called right after command line options are parsed,\n  the project is loaded (if present) and the list of files to process\n  is computed.\n@formal Job_Setup\n  This procedure will be called right before going through units.  If a\n  project was loaded, Project refers to it, otherwise it is null.\n@formal Process_Unit\n  This procedure will be called once right after a unit is parsed\n@formal Job_Post_Process\n  This procedure will be called once after all units have been parsed.\n  Note it will be called once per job.\n@formal App_Post_Process\n  This procedure is called once all jobs are done",
documentation_snippet: "",
packages:    [
       {
       name: "Args",
       qualified_name: "Libadalang.Helpers.App.Args",
       signature: "libadalang.helpers.app.args",
       enclosing: "libadalang.helpers.app",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
variables:           [
              {
              name: "Parser",
              qualified_name: "Libadalang.Helpers.App.Args.Parser",
              signature: "libadalang.helpers.app.args.parser",
              enclosing: "",
              is_private: false,
              documentation: "Argument parser for your application. Supports a set of default\noptions. You can add your own on this parser.",
              documentation_snippet: "Parser : Argument_Parser := Create_Argument_Parser\n  (Help => Description);",
              }          ,
          ]
,       }   ,
   ]
,constants:    [
       {
       name: "Trace",
       qualified_name: "Libadalang.Helpers.App.Trace",
       signature: "libadalang.helpers.app.trace",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Trace : constant GNATCOLL.Traces.Trace_Handle :=\n   GNATCOLL.Traces.Create\n     (\"LIBADALANG.APP.\" & Name, GNATCOLL.Traces.From_Config);",
       }   ,
   ]
,}
---
