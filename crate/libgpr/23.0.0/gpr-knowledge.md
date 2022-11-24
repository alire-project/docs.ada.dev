---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Knowledge",
qualified_name: "GPR.Knowledge",
signature: "gpr.knowledge",
enclosing: "gpr",
is_private: false,
documentation: "This unit is responsible for parsing the gprconfig knowledge base",
documentation_snippet: "",
simple_types:    [
       {
       name: "Compiler",
       qualified_name: "GPR.Knowledge.Compiler",
       signature: "gpr.knowledge.compiler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Compiler is private;",
       }   ,
       {
       name: "Knowledge_Base",
       qualified_name: "GPR.Knowledge.Knowledge_Base",
       signature: "gpr.knowledge.knowledge_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Knowledge_Base is private;",
       }   ,
       {
       name: "Targets_Set_Id",
       qualified_name: "GPR.Knowledge.Targets_Set_Id",
       signature: "gpr.knowledge.targets_set_id",
       enclosing: "",
       is_private: false,
       documentation: "Identify a target aliases set",
       documentation_snippet: "type Targets_Set_Id is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Compiler_Iterator",
       qualified_name: "GPR.Knowledge.Compiler_Iterator",
       signature: "gpr.knowledge.compiler_iterator",
       enclosing: "",
       is_private: false,
       documentation: "An iterator that searches for all known compilers in a list of\ndirectories. Whenever a new compiler is found, the Callback primitive\noperation is called.",
       documentation_snippet: "type Compiler_Iterator is abstract tagged null record;",
       }   ,
       {
       name: "Double_String",
       qualified_name: "GPR.Knowledge.Double_String",
       signature: "gpr.knowledge.double_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Double_String is record\n   Positive_Regexp : Unbounded_String;\n   Negative_Regexp : Unbounded_String;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Compiler_Access",
       qualified_name: "GPR.Knowledge.Compiler_Access",
       signature: "gpr.knowledge.compiler_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Compiler_Access is access all Compiler;",
       }   ,
   ]
,constants:    [
       {
       name: "All_Target_Sets",
       qualified_name: "GPR.Knowledge.All_Target_Sets",
       signature: "gpr.knowledge.all_target_sets",
       enclosing: "",
       is_private: false,
       documentation: "Matches all target sets",
       documentation_snippet: "All_Target_Sets     : constant Targets_Set_Id;",
       }   ,
       {
       name: "No_Compiler",
       qualified_name: "GPR.Knowledge.No_Compiler",
       signature: "gpr.knowledge.no_compiler",
       enclosing: "",
       is_private: false,
       documentation: "Describes one of the compilers found on the PATH.\nPath is the directory that contains the compiler executable.\nPath_Order is used for sorting in the interactive menu: it indicates the\nindex in $PATH of the directory, so that we can show first the compilers\nthat are first in path.\nAny of these compilers can be selected by the user as part of a config.\nHowever, to prevent incompatibilities, a compiler can be marked as not\nselectable. This will be re-evaluated based on the current selection.\nComplete is set to True if all the information about the compiler was\ncomputed. It is set to False if the compiler was specified through a\ncommand line argument --config, and part of the info needs to be\ncomputed.\nIndex_In_List is used for the interactive menu, and is initialized\nautomatically.",
       documentation_snippet: "No_Compiler : constant Compiler;",
       }   ,
       {
       name: "Unknown_Targets_Set",
       qualified_name: "GPR.Knowledge.Unknown_Targets_Set",
       signature: "gpr.knowledge.unknown_targets_set",
       enclosing: "",
       is_private: false,
       documentation: "Special target set when a target is not known",
       documentation_snippet: "Unknown_Targets_Set : constant Targets_Set_Id;",
       }   ,
   ]
,variables:    [
       {
       name: "Pedantic_KB",
       qualified_name: "GPR.Knowledge.Pedantic_KB",
       signature: "gpr.knowledge.pedantic_kb",
       enclosing: "",
       is_private: false,
       documentation: "Expect strict accordance between the expected knowledge base scheme\nand actual files parsed. When parsing an older knowledge base some\nattributes may be missing (i.e. canonical target) and that would lead\nto Invalid_Knowledge_Base raised.",
       documentation_snippet: "Pedantic_KB : Boolean := False;",
       }   ,
   ]
,}
---
