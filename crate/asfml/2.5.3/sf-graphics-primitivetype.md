---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.PrimitiveType",
qualified_name: "Sf.Graphics.PrimitiveType",
signature: "sf.graphics.primitivetype",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Types of primitives that a sf::VertexArray can render\n/\n/ Points and lines have no area, therefore their thickness\n/ will always be 1 pixel, regardless the current transform\n/ and view.\n/\n//////////////////////////////////////////////////////////\n/< List of individual points\n/< List of individual lines\n/< List of connected lines, a point uses the previous point to form a line\n/< List of individual triangles\n/< List of connected triangles, a point uses the two previous points to form a triangle\n/< List of connected triangles, a point uses the common center and the previous point to form a triangle\n/< List of individual quads\n/< @deprecated Use sfLineStrip instead\n/< @deprecated Use sfTriangleStrip instead\n/< @deprecated Use sfTriangleFan instead",
documentation_snippet: "",
subtypes:    [
       {
       name: "sfPrimitiveType",
       qualified_name: "Sf.Graphics.PrimitiveType.sfPrimitiveType",
       signature: "sf.graphics.primitivetype.sfprimitivetype",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype sfPrimitiveType is sfUint32;",
       }   ,
   ]
,constants:    [
       {
       name: "sfLines",
       qualified_name: "Sf.Graphics.PrimitiveType.sfLines",
       signature: "sf.graphics.primitivetype.sflines",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfLines : constant sfPrimitiveType := 1;",
       }   ,
       {
       name: "sfLinesStrip",
       qualified_name: "Sf.Graphics.PrimitiveType.sfLinesStrip",
       signature: "sf.graphics.primitivetype.sflinesstrip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfLinesStrip : constant sfPrimitiveType := 2;",
       }   ,
       {
       name: "sfLineStrip",
       qualified_name: "Sf.Graphics.PrimitiveType.sfLineStrip",
       signature: "sf.graphics.primitivetype.sflinestrip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfLineStrip : constant sfPrimitiveType := 2;",
       }   ,
       {
       name: "sfPoints",
       qualified_name: "Sf.Graphics.PrimitiveType.sfPoints",
       signature: "sf.graphics.primitivetype.sfpoints",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfPoints : constant sfPrimitiveType := 0;",
       }   ,
       {
       name: "sfQuads",
       qualified_name: "Sf.Graphics.PrimitiveType.sfQuads",
       signature: "sf.graphics.primitivetype.sfquads",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfQuads : constant sfPrimitiveType := 6;",
       }   ,
       {
       name: "sfTriangleFan",
       qualified_name: "Sf.Graphics.PrimitiveType.sfTriangleFan",
       signature: "sf.graphics.primitivetype.sftrianglefan",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTriangleFan : constant sfPrimitiveType := 5;",
       }   ,
       {
       name: "sfTriangles",
       qualified_name: "Sf.Graphics.PrimitiveType.sfTriangles",
       signature: "sf.graphics.primitivetype.sftriangles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTriangles : constant sfPrimitiveType := 3;",
       }   ,
       {
       name: "sfTrianglesFan",
       qualified_name: "Sf.Graphics.PrimitiveType.sfTrianglesFan",
       signature: "sf.graphics.primitivetype.sftrianglesfan",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTrianglesFan : constant sfPrimitiveType := 5;",
       }   ,
       {
       name: "sfTrianglesStrip",
       qualified_name: "Sf.Graphics.PrimitiveType.sfTrianglesStrip",
       signature: "sf.graphics.primitivetype.sftrianglesstrip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTrianglesStrip : constant sfPrimitiveType := 4;",
       }   ,
       {
       name: "sfTriangleStrip",
       qualified_name: "Sf.Graphics.PrimitiveType.sfTriangleStrip",
       signature: "sf.graphics.primitivetype.sftrianglestrip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTriangleStrip : constant sfPrimitiveType := 4;",
       }   ,
   ]
,}
---