---
crate: basalt
layout: gnatdoc
gnatdoc: {
name: "Basalt.Slicer",
qualified_name: "Basalt.Slicer",
signature: "basalt.slicer",
enclosing: "basalt",
is_private: false,
documentation: "Slicer context\n\n@formal Index",
documentation_snippet: "",
simple_types:    [
       {
       name: "Context",
       qualified_name: "Basalt.Slicer.Context",
       signature: "basalt.slicer.context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Context is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Slice",
       qualified_name: "Basalt.Slicer.Slice",
       signature: "basalt.slicer.slice",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Slice is record\n   First : Index;\n   Last  : Index;\nend record with\n   Dynamic_Predicate => Slice.First <= Slice.Last;",
       }   ,
   ]
,}
---
