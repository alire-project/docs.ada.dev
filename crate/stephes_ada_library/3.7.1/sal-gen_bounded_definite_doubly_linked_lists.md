---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists",
qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists",
signature: "sal.gen_bounded_definite_doubly_linked_lists",
enclosing: "sal",
is_private: false,
documentation: "Abstract :\n\nA generic bounded doubly linked list with definite elements; no dynamic memory.\n\nCopyright (C) 2017 - 2021 Free Software Foundation, Inc.\n\nThis library is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or (at\nyour option) any later version. This library is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without even\nthe implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR\nPURPOSE. See the GNU General Public License for more details. You\nshould have received a copy of the GNU General Public License\ndistributed with this program; see file COPYING. If not, write to\nthe Free Software Foundation, 59 Temple Place - Suite 330, Boston,\nMA 02111-1307, USA.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.Constant_Reference_Type",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.Cursor",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.Variable_Reference_Type",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "List",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.List",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List (Size : Peek_Type) is tagged private\nwith\n   Constant_Indexing => Constant_Ref,\n   Variable_Indexing => Variable_Ref,\n   Default_Iterator  => Iterate,\n   Iterator_Element  => Element_Type;",
       }   ,
   ]
,access_types:    [
       {
       name: "List_Access",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.List_Access",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Access is access all List;",
       }   ,
       {
       name: "List_Access_Constant",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.List_Access_Constant",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.list_access_constant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Access_Constant is access constant List;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Element",
       qualified_name: "SAL.Gen_Bounded_Definite_Doubly_Linked_Lists.No_Element",
       signature: "sal.gen_bounded_definite_doubly_linked_lists.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---
