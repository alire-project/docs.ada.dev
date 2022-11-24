---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted",
qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted",
signature: "sal.gen_unbounded_definite_vectors_sorted",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Key_Type\n@formal To_Key\n@formal Key_Compare\n@formal Default_Element",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_vectors_sorted.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Cursor",
       signature: "sal.gen_unbounded_definite_vectors_sorted.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Find_Reference_Constant_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Find_Reference_Constant_Type",
       signature: "sal.gen_unbounded_definite_vectors_sorted.find_reference_constant_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Find_Reference_Constant_Type (Element : access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Find_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Find_Reference_Type",
       signature: "sal.gen_unbounded_definite_vectors_sorted.find_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Find_Reference_Type (Element : access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Vector",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Vector",
       signature: "sal.gen_unbounded_definite_vectors_sorted.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector is new Ada.Finalization.Controlled with private with\n   Constant_Indexing => Constant_Ref,\n   Default_Iterator  => Iterate,\n   Iterator_Element  => Element_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Vector",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.Empty_Vector",
       signature: "sal.gen_unbounded_definite_vectors_sorted.empty_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Vector : constant Vector;",
       }   ,
       {
       name: "No_Element",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors_Sorted.No_Element",
       signature: "sal.gen_unbounded_definite_vectors_sorted.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---
