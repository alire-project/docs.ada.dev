---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Bounded_Definite_Vectors.Gen_Refs",
qualified_name: "SAL.Gen_Bounded_Definite_Vectors.Gen_Refs",
signature: "sal.gen_bounded_definite_vectors.gen_refs",
enclosing: "sal.gen_bounded_definite_vectors",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Vectors.Gen_Refs.Constant_Reference_Type",
       signature: "sal.gen_bounded_definite_vectors.gen_refs.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Vectors.Gen_Refs.Variable_Reference_Type",
       signature: "sal.gen_bounded_definite_vectors.gen_refs.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,}
---
