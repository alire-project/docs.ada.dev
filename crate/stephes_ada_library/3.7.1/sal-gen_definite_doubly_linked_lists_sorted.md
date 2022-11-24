---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted",
qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted",
signature: "sal.gen_definite_doubly_linked_lists_sorted",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Element_Compare",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.Constant_Reference_Type",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.Cursor",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.Variable_Reference_Type",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "List",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.List",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is new Ada.Finalization.Controlled with private\nwith\n   Constant_Indexing => Constant_Reference,\n   Variable_Indexing => Variable_Reference,\n   Default_Iterator  => Iterate,\n   Iterator_Element  => Element_Type;",
       }   ,
   ]
,access_types:    [
       {
       name: "List_Access",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.List_Access",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Access is access all List;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_List",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Sorted.Empty_List",
       signature: "sal.gen_definite_doubly_linked_lists_sorted.empty_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_List : constant List;",
       }   ,
   ]
,}
---
