---
crate: lace_math
layout: gnatdoc
gnatdoc: {
name: "any_Math.any_Geometry",
qualified_name: "any_Math.any_Geometry",
signature: "any_math.any_geometry",
enclosing: "any_math",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Triangles",
       qualified_name: "any_Math.any_Geometry.Triangles",
       signature: "any_math.any_geometry.triangles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    Triangles  is array (Index range <>) of Triangle;",
       }   ,
       {
       name: "Vertex_Ids",
       qualified_name: "any_Math.any_Geometry.Vertex_Ids",
       signature: "any_math.any_geometry.vertex_ids",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type    Vertex_Ids is array (Index range <>) of Vertex_Id;",
       }   ,
   ]
,record_types:    [
       {
       name: "Model",
       qualified_name: "any_Math.any_Geometry.Model",
       signature: "any_math.any_geometry.model",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model is abstract tagged\n   record\n      Triangles : access Model_Triangles'Class;\n   end record;",
       }   ,
       {
       name: "Model_Options",
       qualified_name: "any_Math.any_Geometry.Model_Options",
       signature: "any_math.any_geometry.model_options",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model_Options is tagged null record;",
       }   ,
       {
       name: "Model_Triangles",
       qualified_name: "any_Math.any_Geometry.Model_Triangles",
       signature: "any_math.any_geometry.model_triangles",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Model_Triangles (Triangle_Count : Index) is tagged\n   record\n      Triangles : any_Geometry.Triangles (1 .. Triangle_Count);\n   end record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Item",
       qualified_name: "any_Math.any_Geometry.Item",
       signature: "any_math.any_geometry.item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Item is abstract tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Triangle",
       qualified_name: "any_Math.any_Geometry.Triangle",
       signature: "any_math.any_geometry.triangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Triangle   is Vertex_Ids (1 .. 3);",
       }   ,
       {
       name: "Vertex_Id",
       qualified_name: "any_Math.any_Geometry.Vertex_Id",
       signature: "any_math.any_geometry.vertex_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Vertex_Id  is Index;",
       }   ,
   ]
,constants:    [
       {
       name: "default_Model_Options",
       qualified_name: "any_Math.any_Geometry.default_Model_Options",
       signature: "any_math.any_geometry.default_model_options",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "default_Model_Options : constant Model_Options;",
       }   ,
   ]
,}
---
