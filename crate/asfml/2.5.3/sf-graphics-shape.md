---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.Shape",
qualified_name: "Sf.Graphics.Shape",
signature: "sf.graphics.shape",
enclosing: "sf.graphics",
is_private: false,
documentation: "/< Type of the callback used to get the number of points in a shape",
documentation_snippet: "",
access_types:    [
       {
       name: "sfShapeGetPointCallback",
       qualified_name: "Sf.Graphics.Shape.sfShapeGetPointCallback",
       signature: "sf.graphics.shape.sfshapegetpointcallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfShapeGetPointCallback is access function\n  (size : sfSize_t; userData : Standard.System.Address) return Sf.System.Vector2.sfVector2f;",
       }   ,
       {
       name: "sfShapeGetPointCountCallback",
       qualified_name: "Sf.Graphics.Shape.sfShapeGetPointCountCallback",
       signature: "sf.graphics.shape.sfshapegetpointcountcallback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfShapeGetPointCountCallback is access function\n  (userData : Standard.System.Address) return sfSize_t;",
       }   ,
   ]
,}
---
