---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Vectors",
qualified_name: "SAL.Gen_Unbounded_Definite_Vectors",
signature: "sal.gen_unbounded_definite_vectors",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Index_Type\n@formal Element_Type\n@formal Default_Element",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_vectors.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Cursor",
       signature: "sal.gen_unbounded_definite_vectors.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Variable_Reference_Type",
       signature: "sal.gen_unbounded_definite_vectors.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Vector",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Vector",
       signature: "sal.gen_unbounded_definite_vectors.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector is new Ada.Finalization.Controlled with private with\n  Constant_Indexing => Constant_Ref,\n  Variable_Indexing => Variable_Ref,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Element_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Extended_Index",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Extended_Index",
       signature: "sal.gen_unbounded_definite_vectors.extended_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Extended_Index is Index_Type'Base\n  range Index_Type'First - 1 ..\n        Index_Type'Min (Index_Type'Base'Last - 1, Index_Type'Last) + 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Vector",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Empty_Vector",
       signature: "sal.gen_unbounded_definite_vectors.empty_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Vector : constant Vector;",
       }   ,
       {
       name: "No_Index",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.No_Index",
       signature: "sal.gen_unbounded_definite_vectors.no_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Index : constant Extended_Index := Extended_Index'First;",
       }   ,
   ]
,}
---
