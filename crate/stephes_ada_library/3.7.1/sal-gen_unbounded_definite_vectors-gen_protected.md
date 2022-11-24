---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Vectors.Gen_Protected",
qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Gen_Protected",
signature: "sal.gen_unbounded_definite_vectors.gen_protected",
enclosing: "sal.gen_unbounded_definite_vectors",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Lock_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Gen_Protected.Lock_Type",
       signature: "sal.gen_unbounded_definite_vectors.gen_protected.lock_type",
       enclosing: "",
       is_private: false,
       documentation: "  For applications that require an extended read or write lock. If\n  Write, lock for write; otherwise lock for read.\n\n  Note that iterators do _not_ hold a read lock (due to a bug in\n  GNAT GPL 2017), so a separate lock is needed for iterator use.",
       documentation_snippet: "type Lock_Type (Container : not null access constant Vector; Write : Boolean)\n  is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
       {
       name: "Vector",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Gen_Protected.Vector",
       signature: "sal.gen_unbounded_definite_vectors.gen_protected.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Vector_Access_Constant",
       qualified_name: "SAL.Gen_Unbounded_Definite_Vectors.Gen_Protected.Vector_Access_Constant",
       signature: "sal.gen_unbounded_definite_vectors.gen_protected.vector_access_constant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector_Access_Constant is access constant Vector;",
       }   ,
   ]
,}
---
