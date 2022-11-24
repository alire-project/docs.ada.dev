---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count",
qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count",
signature: "sal.gen_definite_doubly_linked_lists_ref_count",
enclosing: "sal",
is_private: false,
documentation: "Abstract :\n\nA generic doubly linked list with definite elements, with\nreference counting on cursors to detect dangling references.\n\nWORKAROUND: there is a bug in GNAT Community 2020 (Eurocontrol\nticket V107-045) that causes reference counting to be inaccurate\nin some cases, so we support turning off the reference counting.\n\nRationale for not implementing reference types and iterators:\nConsider a typical reference type use:\n\ndeclare\n   A : Element_Type renames List.First;\n   To_Delete : Cursor := List.First;\nbegin\n   Delete (To_Delete);\nend;\n\nThe reference object exists only while evaluating the renames, so\nit cannot assert any kind of lock on the element or list that\nsurvives thru the call to Delete and is then released. We would\nhave to use something like:\n\ndeclare\n   A_Ref : constant Reference_Type := List.First;\n   A : Element_Type renames Element (A_Ref);\n   To_Delete : Cursor := List.First;\nbegin\n   Delete (To_Delete);\nend;\n\nWhere \"Reference_Type\" is opaque, and thus cannot be used for iterators.\n\nCopyright (C) 2017 - 2022 Free Software Foundation, Inc.\n\nThis library is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or (at\nyour option) any later version. This library is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without even\nthe implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR\nPURPOSE. See the GNU General Public License for more details. You\nshould have received a copy of the GNU General Public License\ndistributed with this program; see file COPYING. If not, write to\nthe Free Software Foundation, 59 Temple Place - Suite 330, Boston,\nMA 02111-1307, USA.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.Cursor",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.cursor",
       enclosing: "",
       is_private: false,
       documentation: "Cursor is not simply 'private', to allow implementing reference\ncounting.",
       documentation_snippet: "type Cursor is tagged private;",
       }   ,
       {
       name: "List",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.List",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.list",
       enclosing: "",
       is_private: false,
       documentation: "We cannot implement reference counting that detects reference\ntypes (see discussion above), so no reference types, no iterators.",
       documentation_snippet: "type List is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "List_Access",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.List_Access",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Access is access all List;",
       }   ,
       {
       name: "List_Access_Constant",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.List_Access_Constant",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.list_access_constant",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Access_Constant is access constant List;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_List",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.Empty_List",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.empty_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_List : constant List;",
       }   ,
       {
       name: "No_Element",
       qualified_name: "SAL.Gen_Definite_Doubly_Linked_Lists_Ref_Count.No_Element",
       signature: "sal.gen_definite_doubly_linked_lists_ref_count.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---
