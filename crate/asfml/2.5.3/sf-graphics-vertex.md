---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.Vertex",
qualified_name: "Sf.Graphics.Vertex",
signature: "sf.graphics.vertex",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ Define a point with color and texture coordinates\n//////////////////////////////////////////////////////////\n/< Position of the vertex\n/< Color of the vertex\n/< Coordinates of the texture's pixel to map to the vertex",
documentation_snippet: "",
record_types:    [
       {
       name: "sfVertex",
       qualified_name: "Sf.Graphics.Vertex.sfVertex",
       signature: "sf.graphics.vertex.sfvertex",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfVertex is record\n   position : aliased Sf.System.Vector2.sfVector2f;\n   color : aliased Sf.Graphics.Color.sfColor;\n   texCoords : aliased Sf.System.Vector2.sfVector2f;\nend record;",
       }   ,
   ]
,}
---
