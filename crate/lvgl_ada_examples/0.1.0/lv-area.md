---
crate: lvgl_ada_examples
layout: gnatdoc
gnatdoc: {
name: "Lv.Area",
qualified_name: "Lv.Area",
signature: "lv.area",
enclosing: "lv",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Point_Array",
       qualified_name: "Lv.Area.Point_Array",
       signature: "lv.area.point_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point_Array is array (Natural range <>) of aliased Lv.Area.Point_T\n  with Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Area_T",
       qualified_name: "Lv.Area.Area_T",
       signature: "lv.area.area_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Area_T is record\n   X1 : aliased Coord_T;\n   Y1 : aliased Coord_T;\n   X2 : aliased Coord_T;\n   Y2 : aliased Coord_T;\nend record;",
       }   ,
       {
       name: "Point_T",
       qualified_name: "Lv.Area.Point_T",
       signature: "lv.area.point_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point_T is record\n   X : aliased Coord_T;\n   Y : aliased Coord_T;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Coord_T",
       qualified_name: "Lv.Area.Coord_T",
       signature: "lv.area.coord_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Coord_T is Int16_T;",
       }   ,
   ]
,constants:    [
       {
       name: "Lv_Coord_Max",
       qualified_name: "Lv.Area.Lv_Coord_Max",
       signature: "lv.area.lv_coord_max",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lv_Coord_Max : constant := (16383);",
       }   ,
       {
       name: "Lv_Coord_Min",
       qualified_name: "Lv.Area.Lv_Coord_Min",
       signature: "lv.area.lv_coord_min",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lv_Coord_Min : constant := (-16384);",
       }   ,
   ]
,}
---
