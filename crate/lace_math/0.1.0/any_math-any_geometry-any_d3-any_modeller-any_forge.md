---
crate: lace_math
layout: gnatdoc
gnatdoc: {
name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge",
qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge",
signature: "any_math.any_geometry.any_d3.any_modeller.any_forge",
enclosing: "any_math.any_geometry.any_d3.any_modeller",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Latitude",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Latitude",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.latitude",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Latitude  is range -90 ..  90;",
       }   ,
       {
       name: "Longitude",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Longitude",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.longitude",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Longitude is range   0 .. 359;",
       }   ,
   ]
,array_types:    [
       {
       name: "longitude_Line",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.longitude_Line",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.longitude_line",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type longitude_Line is array (Latitude)  of Vertex;",
       }   ,
       {
       name: "polar_Model",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.polar_Model",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.polar_model",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type polar_Model    is array (Longitude) of longitude_Line;",
       }   ,
       {
       name: "Triangle",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Triangle",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.triangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Triangle  is array (Positive range 1 .. 3) of Positive;",
       }   ,
       {
       name: "Triangles",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Triangles",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.triangles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Triangles is array (Positive range <>)     of Triangle;",
       }   ,
       {
       name: "Vertices",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Vertices",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.vertices",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertices  is array (Positive range <>)     of Vertex;",
       }   ,
   ]
,record_types:    [
       {
       name: "Vertex",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.Vertex",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.vertex",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertex is\n   record\n      Id   : Positive := no_Id;\n      Site : any_Geometry.any_d3.Site;\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "no_Id",
       qualified_name: "any_Math.any_Geometry.any_d3.any_Modeller.any_Forge.no_Id",
       signature: "any_math.any_geometry.any_d3.any_modeller.any_forge.no_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "no_Id : constant := Positive'Last;",
       }   ,
   ]
,}
---
