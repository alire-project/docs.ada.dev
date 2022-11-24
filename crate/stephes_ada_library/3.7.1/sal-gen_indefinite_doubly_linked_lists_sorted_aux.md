---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux",
qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux",
signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n@formal Compare_Aux\n@formal Element_Compare",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux.Constant_Reference_Type",
       signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux.Cursor",
       signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux.Variable_Reference_Type",
       signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "List",
       qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux.List",
       signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List is new Ada.Finalization.Controlled with private\nwith\n  Constant_Indexing => Constant_Reference,\n  Variable_Indexing => Variable_Reference,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Element_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_List",
       qualified_name: "SAL.Gen_Indefinite_Doubly_Linked_Lists_Sorted_Aux.Empty_List",
       signature: "sal.gen_indefinite_doubly_linked_lists_sorted_aux.empty_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_List : constant List;",
       }   ,
   ]
,}
---
