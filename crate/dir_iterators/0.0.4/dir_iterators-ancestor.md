---
crate: dir_iterators
layout: gnatdoc
gnatdoc: {
name: "Dir_Iterators.Ancestor",
qualified_name: "Dir_Iterators.Ancestor",
signature: "dir_iterators.ancestor",
enclosing: "dir_iterators",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "Dir_Iterators.Ancestor.Cursor",
       signature: "dir_iterators.ancestor.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Ancestor_Dir_Iterator",
       qualified_name: "Dir_Iterators.Ancestor.Ancestor_Dir_Iterator",
       signature: "dir_iterators.ancestor.ancestor_dir_iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ancestor_Dir_Iterator is\n    new Ada.Finalization.Limited_Controlled and\n        Ancestor_Dir_Iterator_Interfaces.Forward_Iterator with private;",
       }   ,
       {
       name: "Ancestor_Dir_Walk",
       qualified_name: "Dir_Iterators.Ancestor.Ancestor_Dir_Walk",
       signature: "dir_iterators.ancestor.ancestor_dir_walk",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ancestor_Dir_Walk is tagged limited private with\n    Default_Iterator  => Iterate,\n    Iterator_Element  => String,\n    Constant_Indexing => Element_Value;",
       }   ,
   ]
,}
---
