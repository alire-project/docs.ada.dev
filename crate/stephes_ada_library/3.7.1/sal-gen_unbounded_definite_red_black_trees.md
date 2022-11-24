---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees",
qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees",
signature: "sal.gen_unbounded_definite_red_black_trees",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Element_Type\n  Element_Type must have valid default initialization; one\n  non-initialized object of this type is declared, in Tree.Nil.\n@formal Key_Type\n@formal Key\n@formal Key_Compare",
documentation_snippet: "",
simple_types:    [
       {
       name: "Constant_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Constant_Reference_Type",
       signature: "sal.gen_unbounded_definite_red_black_trees.constant_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Constant_Reference_Type (Element : not null access constant Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
       {
       name: "Cursor",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Cursor",
       signature: "sal.gen_unbounded_definite_red_black_trees.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Direction_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Direction_Type",
       signature: "sal.gen_unbounded_definite_red_black_trees.direction_type",
       enclosing: "",
       is_private: false,
       documentation: "Direction of Iterators.\nIf Ascending, Next may be called.\nIf Descending, Previous may be called.\nIf Unknown, neither.\n\n@enum Ascending\n@enum Descending\n@enum Unknown",
       documentation_snippet: "type Direction_Type is (Ascending, Descending, Unknown);",
       }   ,
       {
       name: "Variable_Reference_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Variable_Reference_Type",
       signature: "sal.gen_unbounded_definite_red_black_trees.variable_reference_type",
       enclosing: "",
       is_private: false,
       documentation: "User must not change value of Key thru this reference; if Key is\nchanged, use Delete, Insert.",
       documentation_snippet: "type Variable_Reference_Type (Element : not null access Element_Type) is private with\n  Implicit_Dereference => Element;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Iterator",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Iterator",
       signature: "sal.gen_unbounded_definite_red_black_trees.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Iterator (Container : not null access constant Tree) is new Iterators.Reversible_Iterator with private;",
       }   ,
       {
       name: "Tree",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Tree",
       signature: "sal.gen_unbounded_definite_red_black_trees.tree",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tree is new Ada.Finalization.Controlled with private\nwith\n  Constant_Indexing => Constant_Ref,\n  Variable_Indexing => Variable_Ref,\n  Default_Iterator  => Iterate,\n  Iterator_Element  => Element_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Known_Direction_Type",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Known_Direction_Type",
       signature: "sal.gen_unbounded_definite_red_black_trees.known_direction_type",
       enclosing: "",
       is_private: false,
       documentation: "Direction of Iterators.\nIf Ascending, Next may be called.\nIf Descending, Previous may be called.\nIf Unknown, neither.",
       documentation_snippet: "subtype Known_Direction_Type is Direction_Type range Ascending .. Descending;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Tree",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.Empty_Tree",
       signature: "sal.gen_unbounded_definite_red_black_trees.empty_tree",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Tree : constant Tree;",
       }   ,
       {
       name: "No_Element",
       qualified_name: "SAL.Gen_Unbounded_Definite_Red_Black_Trees.No_Element",
       signature: "sal.gen_unbounded_definite_red_black_trees.no_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Element : constant Cursor;",
       }   ,
   ]
,}
---
