---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Iterators",
qualified_name: "Langkit_Support.Iterators",
signature: "langkit_support.iterators",
enclosing: "langkit_support",
is_private: false,
documentation: "This generic package provides for each Element_Type an interface that\nused to implement iterators.\n\nBeyond the fact that it's super simple, the difference with standard\niterators is that iteration is destructive: once an element has been\nyielded, it's not possible to re-yield it once more.\n\nThe analogy with standard Ada containers is that there's no way to keep a\ncursor to preserve an iteration state.\n\n@formal Element_Type\n  Type for values produced at each iteration\n@formal Element_Array\n  Array type to use when consume the iterator into an array of elements",
documentation_snippet: "",
interface_types:    [
       {
       name: "Iterator",
       qualified_name: "Langkit_Support.Iterators.Iterator",
       signature: "langkit_support.iterators.iterator",
       enclosing: "",
       is_private: false,
       documentation: "Abstraction for iterating over a container",
       documentation_snippet: "type Iterator is interface;",
       }   ,
   ]
,}
---
