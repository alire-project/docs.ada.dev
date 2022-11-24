---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Segmented_Thing",
qualified_name: "Agpl.Segmented_Thing",
signature: "agpl.segmented_thing",
enclosing: "agpl",
is_private: false,
documentation: "----------------------------------------------------------------------\n Object                                                             --\n----------------------------------------------------------------------\n\n@formal Segment_Data\n@formal Index_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Segmented_Thing.Object",
       signature: "agpl.segmented_thing.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Chunk_Type",
       qualified_name: "Agpl.Segmented_Thing.Chunk_Type",
       signature: "agpl.segmented_thing.chunk_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Chunk_Type is record\n   Data  : Segment_Data;\n   First : Index_Type;\n   Last  : Index_Type;\nend record;",
       }   ,
   ]
,}
---
