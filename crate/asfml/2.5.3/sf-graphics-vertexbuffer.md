---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.VertexBuffer",
qualified_name: "Sf.Graphics.VertexBuffer",
signature: "sf.graphics.vertexbuffer",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n/ @brief Usage specifiers\n/\n/ If data is going to be updated once or more every frame,\n/ set the usage to sfVertexBufferStream. If data is going\n/ to be set once and used for a long time without being\n/ modified, set the usage to sfVertexBufferUsageStatic.\n/ For everything else sfVertexBufferUsageDynamic should\n/ be a good compromise.\n/\n//////////////////////////////////////////////////////////\n/< Constantly changing data\n/< Occasionally changing data\n/< Rarely changing data",
documentation_snippet: "",
simple_types:    [
       {
       name: "sfVertexBufferUsage",
       qualified_name: "Sf.Graphics.VertexBuffer.sfVertexBufferUsage",
       signature: "sf.graphics.vertexbuffer.sfvertexbufferusage",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfVertexBufferUsage is\n  (sfVertexBufferStream,\n   sfVertexBufferDynamic,\n   sfVertexBufferStatic);",
       }   ,
   ]
,}
---
