---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Preprocessing",
qualified_name: "Libadalang.Preprocessing",
signature: "libadalang.preprocessing",
enclosing: "libadalang",
is_private: false,
documentation: "This package implements a preprocessor for Ada sources that is compatible\nwith GNATprep. It also provides a file reader implementing such a\npreprocessor, to be used in an analysis context. Please refer to GNATprep's\ndocumentation for a description of the main concepts, of preprocessor data\nfiles and of preprocessing features. The API provided here closely follows\nthese concepts.\n\nThe action of preprocessing an Ada source file is done according to\nparameters (definition of preprocessor symbols, how to format directives\nand disabled lines in the output, ...). The ``File_Config`` type is used to\nrepresent such parameters, and the ``Preprocess`` procedure taking a\n``File_Config`` argument can be used to preprocess a given source buffer.\n\n.. code-block:: ada\n\n   --  Create a file configuration using symbol definitions from GNATprep's\n   --  \"foo.txt\" definition file, replacing directives and disabled lines\n   --  with blank lines.\n\n   Cfg : constant File_Config :=\n     (Enabled => True,\n      Definitions => Parse_Definition_File (\"foo.txt\"),\n      Line_Mode   => Blank_Lines,\n      others      => <>);\n\n    Input_Buffer  : String := \"...\";\n    Output_Buffer : Preprocessed_Source;\n    Diagnostics   : Langkit_Support.Diagnostics.Diagnostics_Vectors.Vector;\n\n   --  Preprocess the \"Input_Buffer\" source, writing the result to\n   --  ``Output_Buffer``.\n\n   Preprocess (Cfg, Input_Buffer, Output_Buffer, Diagnostics);\n\n   if not Diagnostics.Is_Empty then\n      --  Raise some error\n\n   else\n      declare\n         Buffer : String renames\n           Output_Buffer.Buffer (1 .. Output_Buffer.Last)\n      begin\n         --  Use the preprocessed source in \"Buffer\"\n      end;\n   end if;\n\nPreprocessing for a whole Ada project is determined by a set of file\nconfigurations: optionally several ``File_Config`` values for sources with\nspecific file names (see the ``File_Config_Maps.Map`` type), plus an\nadditional ``File_Config`` value to use for files not described in this\nmap (the \"default\" file config).\n\nOne can either create these data structures by hand, or parsing GNATprep's\n\"preprocessor data file\". In the latter case, the\n``Parse_Preprocesor_Data_File`` and ``Create_Preprocessor_Data`` functions\nwill cover each case to create the final \"aggregated\" configuration: a\n``Preprocessor_Data`` value.\n\n.. code-block:: ada\n\n   Path : constant Any_Path :=\n     Create_Path_From_Environ (\"ADA_INCLUDE_PATH\");\n   --  This path allows to find the preprocessor data file and the\n   --  definition files it references in the current directory or in any of\n   --  the directories pointed by the \"ADA_INCLUDE_PATH\" environment\n   --  variable.\n\n   Prep : constant Preprocessor_Data :=\n     Parse_Preprocessor_Data_File (\"prep-data.txt\", Path);\n   --  Parse the \"prep-data.txt\" preprocessor data file and create a full\n   --  preprocessor configuration from it.\n\nFrom there, it is possible to call the \"Preprocess\" procedure taking a\n\"Preprocessor_Data\" argument, plus the file name for the source file to\npreprocess (used to look up the corresponding file configuration).\n\n.. code-block:: ada\n\n   --  Preprocess the \"Input_Buffer\" source as being the content of a\n   --  \"foo.adb\" Ada source file, writing the result to \"Output_Buffer\".\n\n   Preprocess (Prep, \"foo.adb\", Input_Buffer, Output_Buffer, Diagnostics);\n\n   if not Diagnostics.Is_Empty then\n      --  Raise some error\n\n   else\n      declare\n         Buffer : String renames\n           Output_Buffer.Buffer (1 .. Output_Buffer.Last)\n      begin\n         --  Use the preprocessed source in \"Buffer\"\n      end;\n   end if;\n\nFinally, in order to instruct a Libadalang analysis context to\nautomatically preprocess source files when loading files through the\n``Get_From_File`` function, one needs to use the file reader mechanism (see\n``Langkit_Support.File_Readers``): first create a ``File_Reader_Reference``\nvalue that implements preprocessing (see the ``Create_Preprocessor`` and\n``Create_Preprocessor_From_File`` functions defined in this package) and\nthen pass it to the ``Create_Context`` context constructor.\n\n.. code-block:: ada\n\n   FR  : constant File_Reader_Reference :=\n     Create_Preprocessor_From_File (\"prep-data.txt\", Path);\n   Ctx : constant Analysis_Context := Create_Context (File_Reader => FR);\n\n   --  Analyze the \"foo.adb\" source file after preprocessing it according\n   --  to configuration for \"foo.adb\" files in \"prep-data.txt\". The\n   --  analysis of any other source file that this implies will also\n   --  trigger preprocessing for these files.\n\n   U : constant Analysis_Unit := Ctx.Get_From_File (\"foo.adb\");",
documentation_snippet: "",
simple_types:    [
       {
       name: "Any_Line_Mode",
       qualified_name: "Libadalang.Preprocessing.Any_Line_Mode",
       signature: "libadalang.preprocessing.any_line_mode",
       enclosing: "",
       is_private: false,
       documentation: "Determine how the preprocessor treats directives and disabled lines in\nthe output.\n\n``Delete_Lines``\n\n  Just delete these lines: this breaks line number correspondance\n  between the original source and the preprocessed one. This corresponds\n  to GNATprep's default mode.\n\n``Blank_Lines``\n\n  Replace these lines with empty lines. This corresponds to GNATprep's\n  ``-b`` option.\n\n``Comment_Lines``\n\n  Preserve these lines and emit a ``--!`` comment marker in front of\n  them. This corresponds to GNATprep's ``-c`` option.\n\n@enum Delete_Lines\n@enum Blank_Lines\n@enum Comment_Lines",
       documentation_snippet: "type Any_Line_Mode is (Delete_Lines, Blank_Lines, Comment_Lines);",
       }   ,
       {
       name: "Preprocessor_Data",
       qualified_name: "Libadalang.Preprocessing.Preprocessor_Data",
       signature: "libadalang.preprocessing.preprocessor_data",
       enclosing: "",
       is_private: false,
       documentation: "File-specific Symbol/value associations and options to run the\npreprocessor.\n\nThis type is a reference to constant preprocessing configuration:\ncopying this object is cheap.",
       documentation_snippet: "type Preprocessor_Data is private;",
       }   ,
       {
       name: "Value_Kind",
       qualified_name: "Libadalang.Preprocessing.Value_Kind",
       signature: "libadalang.preprocessing.value_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Kind is (Empty, String_Literal, Symbol);",
       }   ,
   ]
,record_types:    [
       {
       name: "File_Config",
       qualified_name: "Libadalang.Preprocessing.File_Config",
       signature: "libadalang.preprocessing.file_config",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Enabled\n@field Definitions\n  Symbol/value associations for this file. Note that, in order\n  for the preprocessing to work correctly, symbols must be lower\n  case.\n@field Line_Mode\n  Determine how the preprocessor treats directives and disabled\n  lines in the output.\n@field Print_Symbols\n  Whether to print a sorted list of symbol and values on the\n  standard output. Actually unused in this module.\n@field Undefined_Is_False",
       documentation_snippet: "type File_Config (Enabled : Boolean := False) is record\n   case Enabled is\n      when False => null;\n      when True =>\n         Definitions : Definition_Maps.Map;\n         Line_Mode : Any_Line_Mode := Delete_Lines;\n         Print_Symbols : Boolean := False;\n         Undefined_Is_False : Boolean := False;\n   end case;\nend record;",
       }   ,
       {
       name: "Preprocessed_Source",
       qualified_name: "Libadalang.Preprocessing.Preprocessed_Source",
       signature: "libadalang.preprocessing.preprocessed_source",
       enclosing: "",
       is_private: false,
       documentation: "Buffer that contains preprocessed sources. ``Buffer'First`` should be 1,\nand the actual content lies in ``Buffer (1 .. Last)``.\n\n@field Buffer\n@field Last",
       documentation_snippet: "type Preprocessed_Source is record\n   Buffer : String_Access;\n   Last   : Natural;\nend record;",
       }   ,
       {
       name: "Value_Type",
       qualified_name: "Libadalang.Preprocessing.Value_Type",
       signature: "libadalang.preprocessing.value_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Type (Kind : Value_Kind := Empty) is record\n   case Kind is\n      when Empty          => null;\n      when String_Literal => String_Value : US.Unbounded_String;\n      when Symbol         => Symbol_Value : US.Unbounded_String;\n   end case;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Disabled_File_Config",
       qualified_name: "Libadalang.Preprocessing.Disabled_File_Config",
       signature: "libadalang.preprocessing.disabled_file_config",
       enclosing: "",
       is_private: false,
       documentation: "By default, the preprocessor is disabled on all Ada sources",
       documentation_snippet: "Disabled_File_Config : constant File_Config := (Enabled => False);",
       }   ,
       {
       name: "No_Preprocessor_Data",
       qualified_name: "Libadalang.Preprocessing.No_Preprocessor_Data",
       signature: "libadalang.preprocessing.no_preprocessor_data",
       enclosing: "",
       is_private: false,
       documentation: "No reference to preprocessor data",
       documentation_snippet: "No_Preprocessor_Data : constant Preprocessor_Data;",
       }   ,
   ]
,}
---
