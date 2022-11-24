---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Lib",
qualified_name: "Lib",
signature: "lib",
enclosing: "",
is_private: false,
documentation: "This package contains routines for accessing and outputting the library\ninformation. It contains the routine to load subsidiary units.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Compiler_State_Type",
       qualified_name: "Lib.Compiler_State_Type",
       signature: "lib.compiler_state_type",
       enclosing: "",
       is_private: false,
       documentation: "Indicates current state of compilation. This is used to implement the\nfunction In_Extended_Main_Source_Unit.\n\n@enum Parsing\n@enum Analyzing",
       documentation_snippet: "type Compiler_State_Type is (Parsing, Analyzing);",
       }   ,
       {
       name: "Fatal_Type",
       qualified_name: "Lib.Fatal_Type",
       signature: "lib.fatal_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum None\n  No error detected for this unit\n@enum Error_Detected\n  Fatal error detected that prevents moving to the next phase. For\n  example, a fatal error during parsing inhibits semantic analysis.\n@enum Error_Ignored\n  A fatal error was detected, but we are in Try_Semantics mode (as set\n  by -gnatq or -gnatQ). This does not stop the compiler from proceding,\n  but tools can use this status (e.g. ASIS looking at the generated\n  tree) to know that a fatal error was detected.",
       documentation_snippet: "type Fatal_Type is (\n   None,\n   Error_Detected,\n   Error_Ignored);",
       }   ,
   ]
,array_types:    [
       {
       name: "Unit_Ref_Table",
       qualified_name: "Lib.Unit_Ref_Table",
       signature: "lib.unit_ref_table",
       enclosing: "",
       is_private: false,
       documentation: "Type to hold list of indirect references to unit number table",
       documentation_snippet: "type Unit_Ref_Table is array (Pos range <>) of Unit_Number_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Main_CPU",
       qualified_name: "Lib.Default_Main_CPU",
       signature: "lib.default_main_cpu",
       enclosing: "",
       is_private: false,
       documentation: "Value used in Main_CPU field to indicate default main affinity",
       documentation_snippet: "Default_Main_CPU : constant Int := -1;",
       }   ,
       {
       name: "Default_Main_Priority",
       qualified_name: "Lib.Default_Main_Priority",
       signature: "lib.default_main_priority",
       enclosing: "",
       is_private: false,
       documentation: "Value used in Main_Priority field to indicate default main priority",
       documentation_snippet: "Default_Main_Priority : constant Int := -1;",
       }   ,
   ]
,variables:    [
       {
       name: "Analysing_Subunit_Of_Main",
       qualified_name: "Lib.Analysing_Subunit_Of_Main",
       signature: "lib.analysing_subunit_of_main",
       enclosing: "",
       is_private: false,
       documentation: "Set to True when analyzing a subunit of the main source. When True, if\nthe subunit is preprocessed and -gnateG is specified, then the\npreprocessed file (.prep) is written.",
       documentation_snippet: "Analysing_Subunit_Of_Main : Boolean := False;",
       }   ,
       {
       name: "Compiler_State",
       qualified_name: "Lib.Compiler_State",
       signature: "lib.compiler_state",
       enclosing: "",
       is_private: false,
       documentation: "Indicates current state of compilation. This is used to implement the\nfunction In_Extended_Main_Source_Unit.",
       documentation_snippet: "Compiler_State : Compiler_State_Type;",
       }   ,
       {
       name: "Current_Sem_Unit",
       qualified_name: "Lib.Current_Sem_Unit",
       signature: "lib.current_sem_unit",
       enclosing: "",
       is_private: false,
       documentation: "Unit number of unit currently being analyzed/expanded. This is set when\never a new unit is entered, saving and restoring the old value, so that\nit always reflects the unit currently being analyzed. The initial value\nof Main_Unit ensures that a proper value is set initially, and in\nparticular for analysis of configuration pragmas in gnat.adc.",
       documentation_snippet: "Current_Sem_Unit : Unit_Number_Type := Main_Unit;",
       }   ,
       {
       name: "Main_Unit_Entity",
       qualified_name: "Lib.Main_Unit_Entity",
       signature: "lib.main_unit_entity",
       enclosing: "",
       is_private: false,
       documentation: "Entity of main unit, same as Cunit_Entity (Main_Unit) except where\nMain_Unit is a body with a separate spec, in which case it is the\nentity for the spec.",
       documentation_snippet: "Main_Unit_Entity : Entity_Id;",
       }   ,
       {
       name: "Parsing_Main_Extended_Source",
       qualified_name: "Lib.Parsing_Main_Extended_Source",
       signature: "lib.parsing_main_extended_source",
       enclosing: "",
       is_private: false,
       documentation: "Set True if we are currently parsing a file that is part of the main\nextended source (the main unit, its spec, or one of its subunits). This\nflag to implement In_Extended_Main_Source_Unit.",
       documentation_snippet: "Parsing_Main_Extended_Source : Boolean := False;",
       }   ,
   ]
,}
---
