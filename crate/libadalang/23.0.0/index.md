---
crate: libadalang
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Libadalang",
    qualified_name: "Libadalang",
    signature: "libadalang",
    enclosing: "",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Analysis",
    qualified_name: "Libadalang.Analysis",
    signature: "libadalang.analysis",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Auto_Provider",
    qualified_name: "Libadalang.Auto_Provider",
    signature: "libadalang.auto_provider",
    enclosing: "libadalang",
    is_private: false,
    documentation: "This package provides the capability to automatically discover the layout\nof source files in an Ada project, given a list of files, or a file name\npattern and a list of directories.\n\nIt is useful in order to easily run Libadalang on a complex project that\ndoes not have its own GPR project file.",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.C",
    qualified_name: "Libadalang.C",
    signature: "libadalang.c",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Common",
    qualified_name: "Libadalang.Common",
    signature: "libadalang.common",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Config_Pragmas",
    qualified_name: "Libadalang.Config_Pragmas",
    signature: "libadalang.config_pragmas",
    enclosing: "libadalang",
    is_private: false,
    documentation: "This package provides helpers to deal with GNAT's configurations pragmas\nfiles.",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Doc_Utils",
    qualified_name: "Libadalang.Doc_Utils",
    signature: "libadalang.doc_utils",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Expr_Eval",
    qualified_name: "Libadalang.Expr_Eval",
    signature: "libadalang.expr_eval",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Generic_API",
    qualified_name: "Libadalang.Generic_API",
    signature: "libadalang.generic_api",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Generic_API.Introspection",
    qualified_name: "Libadalang.Generic_API.Introspection",
    signature: "libadalang.generic_api.introspection",
    enclosing: "libadalang.generic_api",
    is_private: false,
    documentation: "This package provides contants to refer to Libadalang types and struct\nmembers in the generic introspection API\n(``Langkit_Support.Generic_API.Introspection``).",
    documentation_snippet: "",
    },
    {
    name: "Member_Refs",
    qualified_name: "Libadalang.Generic_API.Introspection.Member_Refs",
    signature: "libadalang.generic_api.introspection.member_refs",
    enclosing: "libadalang.generic_api.introspection",
    is_private: false,
    documentation: "---------------------\n Member references --\n---------------------",
    documentation_snippet: "",
    },
    {
    name: "Type_Refs",
    qualified_name: "Libadalang.Generic_API.Introspection.Type_Refs",
    signature: "libadalang.generic_api.introspection.type_refs",
    enclosing: "libadalang.generic_api.introspection",
    is_private: false,
    documentation: "-------------------\n Type references --\n-------------------",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Helpers",
    qualified_name: "Libadalang.Helpers",
    signature: "libadalang.helpers",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "App",
    qualified_name: "Libadalang.Helpers.App",
    signature: "libadalang.helpers.app",
    enclosing: "libadalang.helpers",
    is_private: false,
    documentation: "\n@formal Name\n  Name for the application. Used to create the GNATCOLL trace.\n@formal Description\n  Description for the application. Will be used in the help string.\n@formal Enable_Parallelism\n  If True, add a -j/--jobs command line option to allow multiple jobs\n  to run in parallel. In this mode, we create one analysis context per\n  job, and the files to process are distributed on each job. All the\n  callbacks below are called concurrently in all jobs:\n  \n  First, the main task calls App_Setup. Then all jobs start:\n  \n    * Job 1 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 2 calls Job_Setup, then several Process_Units, then\n      Job_Post_Process.\n  \n    * Job 3 calls ...\n  \n  Finally, once all jobs are done, the main task calls\n  App_Post_Process.\n@formal App_Setup\n  This procedure is called right after command line options are parsed,\n  the project is loaded (if present) and the list of files to process\n  is computed.\n@formal Job_Setup\n  This procedure will be called right before going through units.  If a\n  project was loaded, Project refers to it, otherwise it is null.\n@formal Process_Unit\n  This procedure will be called once right after a unit is parsed\n@formal Job_Post_Process\n  This procedure will be called once after all units have been parsed.\n  Note it will be called once per job.\n@formal App_Post_Process\n  This procedure is called once all jobs are done",
    documentation_snippet: "",
    },
    {
    name: "Args",
    qualified_name: "Libadalang.Helpers.App.Args",
    signature: "libadalang.helpers.app.args",
    enclosing: "libadalang.helpers.app",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Introspection",
    qualified_name: "Libadalang.Introspection",
    signature: "libadalang.introspection",
    enclosing: "libadalang",
    is_private: false,
    documentation: "--------------\n Node types --\n--------------",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Iterators",
    qualified_name: "Libadalang.Iterators",
    signature: "libadalang.iterators",
    enclosing: "libadalang",
    is_private: false,
    documentation: "------------------\n Iterators core --\n------------------",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Iterators.Extensions",
    qualified_name: "Libadalang.Iterators.Extensions",
    signature: "libadalang.iterators.extensions",
    enclosing: "libadalang.iterators",
    is_private: false,
    documentation: "Extension to the generated Iterators API for Libadalang-specific entry\npoints.",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Lexer",
    qualified_name: "Libadalang.Lexer",
    signature: "libadalang.lexer",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Preprocessing",
    qualified_name: "Libadalang.Preprocessing",
    signature: "libadalang.preprocessing",
    enclosing: "libadalang",
    is_private: false,
    documentation: "This package implements a preprocessor for Ada sources that is compatible\nwith GNATprep. It also provides a file reader implementing such a\npreprocessor, to be used in an analysis context. Please refer to GNATprep's\ndocumentation for a description of the main concepts, of preprocessor data\nfiles and of preprocessing features. The API provided here closely follows\nthese concepts.\n\nThe action of preprocessing an Ada source file is done according to\nparameters (definition of preprocessor symbols, how to format directives\nand disabled lines in the output, ...). The ``File_Config`` type is used to\nrepresent such parameters, and the ``Preprocess`` procedure taking a\n``File_Config`` argument can be used to preprocess a given source buffer.\n\n.. code-block:: ada\n\n   --  Create a file configuration using symbol definitions from GNATprep's\n   --  \"foo.txt\" definition file, replacing directives and disabled lines\n   --  with blank lines.\n\n   Cfg : constant File_Config :=\n     (Enabled => True,\n      Definitions => Parse_Definition_File (\"foo.txt\"),\n      Line_Mode   => Blank_Lines,\n      others      => <>);\n\n    Input_Buffer  : String := \"...\";\n    Output_Buffer : Preprocessed_Source;\n    Diagnostics   : Langkit_Support.Diagnostics.Diagnostics_Vectors.Vector;\n\n   --  Preprocess the \"Input_Buffer\" source, writing the result to\n   --  ``Output_Buffer``.\n\n   Preprocess (Cfg, Input_Buffer, Output_Buffer, Diagnostics);\n\n   if not Diagnostics.Is_Empty then\n      --  Raise some error\n\n   else\n      declare\n         Buffer : String renames\n           Output_Buffer.Buffer (1 .. Output_Buffer.Last)\n      begin\n         --  Use the preprocessed source in \"Buffer\"\n      end;\n   end if;\n\nPreprocessing for a whole Ada project is determined by a set of file\nconfigurations: optionally several ``File_Config`` values for sources with\nspecific file names (see the ``File_Config_Maps.Map`` type), plus an\nadditional ``File_Config`` value to use for files not described in this\nmap (the \"default\" file config).\n\nOne can either create these data structures by hand, or parsing GNATprep's\n\"preprocessor data file\". In the latter case, the\n``Parse_Preprocesor_Data_File`` and ``Create_Preprocessor_Data`` functions\nwill cover each case to create the final \"aggregated\" configuration: a\n``Preprocessor_Data`` value.\n\n.. code-block:: ada\n\n   Path : constant Any_Path :=\n     Create_Path_From_Environ (\"ADA_INCLUDE_PATH\");\n   --  This path allows to find the preprocessor data file and the\n   --  definition files it references in the current directory or in any of\n   --  the directories pointed by the \"ADA_INCLUDE_PATH\" environment\n   --  variable.\n\n   Prep : constant Preprocessor_Data :=\n     Parse_Preprocessor_Data_File (\"prep-data.txt\", Path);\n   --  Parse the \"prep-data.txt\" preprocessor data file and create a full\n   --  preprocessor configuration from it.\n\nFrom there, it is possible to call the \"Preprocess\" procedure taking a\n\"Preprocessor_Data\" argument, plus the file name for the source file to\npreprocess (used to look up the corresponding file configuration).\n\n.. code-block:: ada\n\n   --  Preprocess the \"Input_Buffer\" source as being the content of a\n   --  \"foo.adb\" Ada source file, writing the result to \"Output_Buffer\".\n\n   Preprocess (Prep, \"foo.adb\", Input_Buffer, Output_Buffer, Diagnostics);\n\n   if not Diagnostics.Is_Empty then\n      --  Raise some error\n\n   else\n      declare\n         Buffer : String renames\n           Output_Buffer.Buffer (1 .. Output_Buffer.Last)\n      begin\n         --  Use the preprocessed source in \"Buffer\"\n      end;\n   end if;\n\nFinally, in order to instruct a Libadalang analysis context to\nautomatically preprocess source files when loading files through the\n``Get_From_File`` function, one needs to use the file reader mechanism (see\n``Langkit_Support.File_Readers``): first create a ``File_Reader_Reference``\nvalue that implements preprocessing (see the ``Create_Preprocessor`` and\n``Create_Preprocessor_From_File`` functions defined in this package) and\nthen pass it to the ``Create_Context`` context constructor.\n\n.. code-block:: ada\n\n   FR  : constant File_Reader_Reference :=\n     Create_Preprocessor_From_File (\"prep-data.txt\", Path);\n   Ctx : constant Analysis_Context := Create_Context (File_Reader => FR);\n\n   --  Analyze the \"foo.adb\" source file after preprocessing it according\n   --  to configuration for \"foo.adb\" files in \"prep-data.txt\". The\n   --  analysis of any other source file that this implies will also\n   --  trigger preprocessing for these files.\n\n   U : constant Analysis_Unit := Ctx.Get_From_File (\"foo.adb\");",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Project_Provider",
    qualified_name: "Libadalang.Project_Provider",
    signature: "libadalang.project_provider",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Rewriting",
    qualified_name: "Libadalang.Rewriting",
    signature: "libadalang.rewriting",
    enclosing: "libadalang",
    is_private: false,
    documentation: "This package provides support for tree-based source code rewriting.\n\n.. ATTENTION:: This is an experimental feature, so even if it is exposed to\nallow experiments, it is totally unsupported and the API is very likely to\nchange in the future.",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Sources",
    qualified_name: "Libadalang.Sources",
    signature: "libadalang.sources",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Unit_Files",
    qualified_name: "Libadalang.Unit_Files",
    signature: "libadalang.unit_files",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
    {
    name: "Libadalang.Unparsing",
    qualified_name: "Libadalang.Unparsing",
    signature: "libadalang.unparsing",
    enclosing: "libadalang",
    is_private: false,
    documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
    documentation_snippet: "",
    },
]
}
---