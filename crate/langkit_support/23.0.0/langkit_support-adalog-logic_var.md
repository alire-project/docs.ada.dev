---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Adalog.Logic_Var",
qualified_name: "Langkit_Support.Adalog.Logic_Var",
signature: "langkit_support.adalog.logic_var",
enclosing: "langkit_support.adalog",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0\n\n@formal Value_Type\n  Type of the values associated to variables, assumed to have by-reference\n  semantics.\n@formal Inc_Ref\n@formal Dec_Ref\n  Associated ref-counting primitives\n@formal Value_Image\n  Image of values, for debugging purposes",
documentation_snippet: "",
array_types:    [
       {
       name: "Logic_Var_Array",
       qualified_name: "Langkit_Support.Adalog.Logic_Var.Logic_Var_Array",
       signature: "langkit_support.adalog.logic_var.logic_var_array",
       enclosing: "",
       is_private: false,
       documentation: "Array of values of this variable, for convenience. To be used in other\ngeneric packages taking a formal Logic_Var package as argument.",
       documentation_snippet: "type Logic_Var_Array is array (Positive range <>) of Logic_Var;",
       }   ,
       {
       name: "Value_Array",
       qualified_name: "Langkit_Support.Adalog.Logic_Var.Value_Array",
       signature: "langkit_support.adalog.logic_var.value_array",
       enclosing: "",
       is_private: false,
       documentation: "Array of values of this variable, for convenience. To be used in other\ngeneric packages taking a formal Logic_Var package as argument.",
       documentation_snippet: "type Value_Array is array (Positive range <>) of Value_Type;",
       }   ,
   ]
,record_types:    [
       {
       name: "Logic_Var_Record",
       qualified_name: "Langkit_Support.Adalog.Logic_Var.Logic_Var_Record",
       signature: "langkit_support.adalog.logic_var.logic_var_record",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Reset\n  Whether this variable is reset, i.e. whether it has no value\n@field Value\n  The value of this logic variable, when it is set (see the ``Reset``\n  component).\n@field Dbg_Name\n  Access to a string representing the name of this variable, for\n  debugging purposes.\n@field Id\n@field Aliased_To",
       documentation_snippet: "type Logic_Var_Record is record\n   Reset : Boolean := True;\n   Value : Value_Type;\n   Dbg_Name : String_Access;\n   Id : Natural := 0;\n   Aliased_To : Logic_Var := null;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Logic_Var",
       qualified_name: "Langkit_Support.Adalog.Logic_Var.Logic_Var",
       signature: "langkit_support.adalog.logic_var.logic_var",
       enclosing: "",
       is_private: false,
       documentation: "Reference to a logic variable",
       documentation_snippet: "type Logic_Var is access all Logic_Var_Record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Logic_Var",
       qualified_name: "Langkit_Support.Adalog.Logic_Var.No_Logic_Var",
       signature: "langkit_support.adalog.logic_var.no_logic_var",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Logic_Var : constant Logic_Var := null;",
       }   ,
   ]
,}
---
