---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Tree_Traversal_Iterator",
qualified_name: "Langkit_Support.Tree_Traversal_Iterator",
signature: "langkit_support.tree_traversal_iterator",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0\n\n@formal Node_Type\n  Type for the node of trees to traverse\n@formal No_Node\n  Special value to represent the absence of a node\n@formal Node_Array\n  Type to use for array of nodes\n@formal First_Child_Index\n  Return the index of the first child in N\n@formal Last_Child_Index\n  Return the index of the last child in N\n@formal Get_Child\n  Return the Index-th child in N. Trees are allowed to have \"holes\" in\n  children, so Get_Child can return No_Node.\n@formal Get_Parent\n  Return the parent node for N. Returning No_Node means that N is the root\n  node.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Traverse_Iterator",
       qualified_name: "Langkit_Support.Tree_Traversal_Iterator.Traverse_Iterator",
       signature: "langkit_support.tree_traversal_iterator.traverse_iterator",
       enclosing: "",
       is_private: false,
       documentation: "Iterator type for Traverse (see below)",
       documentation_snippet: "type Traverse_Iterator is new Iterators.Iterator with private;",
       }   ,
   ]
,}
---
