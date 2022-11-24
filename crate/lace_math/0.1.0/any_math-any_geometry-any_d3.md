---
crate: lace_math
layout: gnatdoc
gnatdoc: {
name: "any_Math.any_Geometry.any_d3",
qualified_name: "any_Math.any_Geometry.any_d3",
signature: "any_math.any_geometry.any_d3",
enclosing: "any_math.any_geometry",
is_private: false,
documentation: "------------\n  Core Types",
documentation_snippet: "",
simple_types:    [
       {
       name: "Plane",
       qualified_name: "any_Math.any_Geometry.any_d3.Plane",
       signature: "any_math.any_geometry.any_d3.plane",
       enclosing: "",
       is_private: false,
       documentation: "A general plane equation.",
       documentation_snippet: "type Plane is new Vector_4;",
       }   ,
   ]
,array_types:    [
       {
       name: "Sites",
       qualified_name: "any_Math.any_Geometry.any_d3.Sites",
       signature: "any_math.any_geometry.any_d3.sites",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    Sites is array (Positive range <>) of Site;",
       }   ,
   ]
,record_types:    [
       {
       name: "a_Model",
       qualified_name: "any_Math.any_Geometry.any_d3.a_Model",
       signature: "any_math.any_geometry.any_d3.a_model",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type a_Model (Site_Count : Positive;\n               Tri_Count : Positive) is\n   record\n      Sites     : any_d3      .Sites     (1 .. Site_Count);\n      Triangles : any_Geometry.Triangles (1 ..  Tri_Count);\n   end record;",
       }   ,
       {
       name: "bounding_Box",
       qualified_name: "any_Math.any_Geometry.any_d3.bounding_Box",
       signature: "any_math.any_geometry.any_d3.bounding_box",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type bounding_Box is\n   record\n      Lower,\n      Upper : Site;\n   end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Site",
       qualified_name: "any_Math.any_Geometry.any_d3.Site",
       signature: "any_math.any_geometry.any_d3.site",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Site  is Vector_3;",
       }   ,
   ]
,constants:    [
       {
       name: "null_Bounds",
       qualified_name: "any_Math.any_Geometry.any_d3.null_Bounds",
       signature: "any_math.any_geometry.any_d3.null_bounds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "null_Bounds : constant bounding_Box;",
       }   ,
   ]
,}
---
