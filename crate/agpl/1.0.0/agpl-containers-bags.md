---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Bags",
qualified_name: "Agpl.Containers.Bags",
signature: "agpl.containers.bags",
enclosing: "agpl.containers",
is_private: false,
documentation: "A bag is a container for unordered objects.\nIts interesting properties are:\nO (1) access to any position (though you can't know what's in that position,\n but this can be useful in randomized algorithms).\nO (1) insertion and deletion of objects in the bag.\nDirect access to the array of objects\n (Take care of using the Last function and not the 'Last attribute)\n\n@formal Item_type\n@formal Bag_Context\n  Bag-specific info\n@formal Initial_size\n  Use something meaningful to your app.\n@formal Grow_factor",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Containers.Bags.Object",
       signature: "agpl.containers.bags.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is new Bag_Vectors.Object with private;",
       }   ,
   ]
,}
---
