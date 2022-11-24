---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets",
qualified_name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets",
signature: "sal.gen_unbounded_sparse_ordered_sets",
enclosing: "sal",
is_private: false,
documentation: "Abstract :\n\nUnbounded sparse sets.\n\nCopyright (C) 2020 - 2022 Free Software Foundation All Rights Reserved.\n\nThis library is free software;  you can redistribute it and/or modify it\nunder terms of the  GNU General Public License  as published by the Free\nSoftware  Foundation;  either version 3,  or (at your  option) any later\nversion. This library is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-\nTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\n@formal Index_Type\n  Index_Type must have a valid default initialization; it is used as\n  Gen_Unbounded_Definite_Red_Black_Trees.Element_Type.\n@formal Index_Compare",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets.Constant_Reference_Type",
       signature: "sal.gen_unbounded_sparse_ordered_sets.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Index_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets.Cursor",
       signature: "sal.gen_unbounded_sparse_ordered_sets.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Iterator",
       qualified_name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets.Iterator",
       signature: "sal.gen_unbounded_sparse_ordered_sets.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator (<>) is new Iterators.Forward_Iterator with private;",
       }   ,
       {
       name: "Set",
       qualified_name: "SAL.Gen_Unbounded_Sparse_Ordered_Sets.Set",
       signature: "sal.gen_unbounded_sparse_ordered_sets.set",
       enclosing: "",
       is_private: false,
       documentation: "We'd like to have Constant_Indexing return a Boolean, so we could\nuse 'if Set (Item) then'. But then the default iterator would\nalways return True, instead of Index_Type; we can't specify a\ndifferent Constant_Indexing function for the default iterator.",
       documentation_snippet: "type Set is tagged private\nwith\n  Constant_Indexing => Constant_Ref,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Index_Type;",
       }   ,
   ]
,}
---
