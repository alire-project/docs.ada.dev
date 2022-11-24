---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Adalog.Solver_Interface",
qualified_name: "Langkit_Support.Adalog.Solver_Interface",
signature: "langkit_support.adalog.solver_interface",
enclosing: "langkit_support.adalog",
is_private: false,
documentation: "-----------------\n Functor types --\n-----------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Base_Functor_Type",
       qualified_name: "Langkit_Support.Adalog.Solver_Interface.Base_Functor_Type",
       signature: "langkit_support.adalog.solver_interface.base_functor_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Base_Functor_Type is abstract tagged record\n   Ref_Count : Natural;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Combiner_Type",
       qualified_name: "Langkit_Support.Adalog.Solver_Interface.Combiner_Type",
       signature: "langkit_support.adalog.solver_interface.combiner_type",
       enclosing: "",
       is_private: false,
       documentation: "Type to compute a value from multiple input values\n\n@field N\n@field Cache_Set\n@field Cache_Key\n@field Cache_Value",
       documentation_snippet: "type Combiner_Type (N : Positive) is\n  abstract new Base_Functor_Type with\nrecord\n   Cache_Set   : Boolean;\n   Cache_Key   : Value_Array (1 .. N);\n   Cache_Value : Value_Type;\nend record;",
       }   ,
       {
       name: "Converter_Type",
       qualified_name: "Langkit_Support.Adalog.Solver_Interface.Converter_Type",
       signature: "langkit_support.adalog.solver_interface.converter_type",
       enclosing: "",
       is_private: false,
       documentation: "Type to convert one value to another\n\n@field Cache_Set\n@field Cache_Key\n@field Cache_Value",
       documentation_snippet: "type Converter_Type is abstract new Base_Functor_Type with record\n   Cache_Set              : Boolean;\n   Cache_Key, Cache_Value : Value_Type;\nend record;",
       }   ,
       {
       name: "N_Predicate_Type",
       qualified_name: "Langkit_Support.Adalog.Solver_Interface.N_Predicate_Type",
       signature: "langkit_support.adalog.solver_interface.n_predicate_type",
       enclosing: "",
       is_private: false,
       documentation: "A predicate encapsulates the logic of applying a boolean predicate to a\nlist of values, returning whether the predicate succeeds.\n\n@field N\n@field Cache_Set\n@field Cache_Key\n@field Cache_Value",
       documentation_snippet: "type N_Predicate_Type (N : Positive) is\n  abstract new Base_Functor_Type with\nrecord\n   Cache_Set   : Boolean;\n   Cache_Key   : Value_Array (1 .. N);\n   Cache_Value : Boolean;\nend record;",
       }   ,
       {
       name: "Predicate_Type",
       qualified_name: "Langkit_Support.Adalog.Solver_Interface.Predicate_Type",
       signature: "langkit_support.adalog.solver_interface.predicate_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Predicate_Type is abstract new Base_Functor_Type with record\n   Cache_Set   : Boolean;\n   Cache_Key   : Value_Type;\n   Cache_Value : Boolean;\nend record;",
       }   ,
   ]
,}
---
