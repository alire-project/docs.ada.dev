---
crate: lace_math
layout: gnatdoc
gnatdoc: {
name: "any_Math.any_Geometry.any_d2",
qualified_name: "any_Math.any_Geometry.any_d2",
signature: "any_math.any_geometry.any_d2",
enclosing: "any_math.any_geometry",
is_private: false,
documentation: "-------\n  Sites",
documentation_snippet: "",
simple_types:    [
       {
       name: "Line",
       qualified_name: "any_Math.any_Geometry.any_d2.Line",
       signature: "any_math.any_geometry.any_d2.line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Sites",
       qualified_name: "any_Math.any_Geometry.any_d2.Sites",
       signature: "any_math.any_geometry.any_d2.sites",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    Sites is array (Positive range <>) of Site;",
       }   ,
   ]
,record_types:    [
       {
       name: "bounding_Box",
       qualified_name: "any_Math.any_Geometry.any_d2.bounding_Box",
       signature: "any_math.any_geometry.any_d2.bounding_box",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type bounding_Box is\n   record\n      Lower,\n      Upper : Site;\n   end record;",
       }   ,
       {
       name: "Circle",
       qualified_name: "any_Math.any_Geometry.any_d2.Circle",
       signature: "any_math.any_geometry.any_d2.circle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Circle is\n   record\n      Radius : Real;\n   end record;",
       }   ,
       {
       name: "polar_Site",
       qualified_name: "any_Math.any_Geometry.any_d2.polar_Site",
       signature: "any_math.any_geometry.any_d2.polar_site",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type polar_Site is\n   record\n      Angle  : Radians;\n      Extent : Real;\n   end record;",
       }   ,
       {
       name: "Polygon",
       qualified_name: "any_Math.any_Geometry.any_d2.Polygon",
       signature: "any_math.any_geometry.any_d2.polygon",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Polygon (Vertex_Count : Positive) is\n   record\n      Vertices : Sites (1 .. Vertex_Count);\n   end record;",
       }   ,
       {
       name: "Triangle",
       qualified_name: "any_Math.any_Geometry.any_d2.Triangle",
       signature: "any_math.any_geometry.any_d2.triangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Triangle is\n   record\n      Vertices : Sites (1 .. 3);\n   end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Site",
       qualified_name: "any_Math.any_Geometry.any_d2.Site",
       signature: "any_math.any_geometry.any_d2.site",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Site  is Vector_2;",
       }   ,
   ]
,constants:    [
       {
       name: "null_Bounds",
       qualified_name: "any_Math.any_Geometry.any_d2.null_Bounds",
       signature: "any_math.any_geometry.any_d2.null_bounds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "null_Bounds : constant bounding_Box;",
       }   ,
   ]
,}
---
