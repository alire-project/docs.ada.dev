---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Iterators",
qualified_name: "Libadalang.Iterators",
signature: "libadalang.iterators",
enclosing: "libadalang",
is_private: false,
documentation: "------------------\n Iterators core --\n------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Ada_Node_Predicate_Array",
       qualified_name: "Libadalang.Iterators.Ada_Node_Predicate_Array",
       signature: "libadalang.iterators.ada_node_predicate_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ada_Node_Predicate_Array is array (Positive range <>) of Ada_Node_Predicate;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Ada_Node_Predicate_Interface",
       qualified_name: "Libadalang.Iterators.Ada_Node_Predicate_Interface",
       signature: "libadalang.iterators.ada_node_predicate_interface",
       enclosing: "",
       is_private: false,
       documentation: "Predicate on nodes.\n\nUseful predicates often rely on values from some context, so predicates\nthat are mere accesses to a function are not powerful enough. Having a\nfull interface for this makes it possible to package both the predicate\ncode and some data it needs.\n\nNote that predicates are not thread-safe: make sure you don't use a\npredicate from multiple threads, as they can contain caches.",
       documentation_snippet: "type Ada_Node_Predicate_Interface is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Traverse_Iterator",
       qualified_name: "Libadalang.Iterators.Traverse_Iterator",
       signature: "libadalang.iterators.traverse_iterator",
       enclosing: "",
       is_private: false,
       documentation: "Iterator that yields nodes from a tree",
       documentation_snippet: "type Traverse_Iterator is new Ada_Node_Iterators.Iterator with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Ada_Node_Predicate",
       qualified_name: "Libadalang.Iterators.Ada_Node_Predicate",
       signature: "libadalang.iterators.ada_node_predicate",
       enclosing: "",
       is_private: false,
       documentation: "Ref-counted reference to a predicate",
       documentation_snippet: "subtype Ada_Node_Predicate is Ada_Node_Predicate_References.Ref;",
       }   ,
   ]
,}
---
