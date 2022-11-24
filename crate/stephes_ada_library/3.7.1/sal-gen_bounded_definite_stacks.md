---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Bounded_Definite_Stacks",
qualified_name: "SAL.Gen_Bounded_Definite_Stacks",
signature: "sal.gen_bounded_definite_stacks",
enclosing: "sal",
is_private: false,
documentation: "pragma Suppress (All_Checks); --  Users must check Is_Full before Push, Is_Empty before Pop etc.\n\n@formal Element_Type",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stack",
       qualified_name: "SAL.Gen_Bounded_Definite_Stacks.Stack",
       signature: "sal.gen_bounded_definite_stacks.stack",
       enclosing: "",
       is_private: false,
       documentation: "Tagged to allow Object.Method notation.",
       documentation_snippet: "type Stack (Size : Size_Type) is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Size_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Stacks.Size_Type",
       signature: "sal.gen_bounded_definite_stacks.size_type",
       enclosing: "",
       is_private: false,
       documentation: "The upper limit is needed to avoid overflow in Peek.\nZero included for Depth result.",
       documentation_snippet: "subtype Size_Type is Base_Peek_Type range 0 .. Base_Peek_Type'Last / 2;",
       }   ,
   ]
,}
---
