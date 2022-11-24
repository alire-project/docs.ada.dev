---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Stacks",
qualified_name: "SAL.Gen_Unbounded_Definite_Stacks",
signature: "sal.gen_unbounded_definite_stacks",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nStack implementation.\n\nCopyright (C) 1998-2000, 2002-2003, 2009, 2015, 2017 - 2021 Free Software Foundation, Inc.\n\nSAL is free software; you can redistribute it and/or modify it\nunder terms of the GNU General Public License as published by the\nFree Software Foundation; either version 3, or (at your option)\nany later version. SAL is distributed in the hope that it will be\nuseful, but WITHOUT ANY WARRANTY; without even the implied\nwarranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\nSee the GNU General Public License for more details. You should\nhave received a copy of the GNU General Public License distributed\nwith SAL; see file COPYING. If not, write to the Free Software\nFoundation, 59 Temple Place - Suite 330, Boston, MA 02111-1307,\nUSA.\n\nAs a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Stacks.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_stacks.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Definite_Stacks.Cursor",
       signature: "sal.gen_unbounded_definite_stacks.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Stack",
       qualified_name: "SAL.Gen_Unbounded_Definite_Stacks.Stack",
       signature: "sal.gen_unbounded_definite_stacks.stack",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stack is new Ada.Finalization.Controlled with private\nwith\n  Constant_Indexing => Constant_Reference,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Element_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Stack",
       qualified_name: "SAL.Gen_Unbounded_Definite_Stacks.Empty_Stack",
       signature: "sal.gen_unbounded_definite_stacks.empty_stack",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Stack : constant Stack;",
       }   ,
   ]
,}
---
