---
crate: lvgl_ada_examples
layout: gnatdoc
gnatdoc: {
name: "Lv.Hal.Disp",
qualified_name: "Lv.Hal.Disp",
signature: "lv.hal.disp",
enclosing: "lv.hal",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Disp_T",
       qualified_name: "Lv.Hal.Disp.Disp_T",
       signature: "lv.hal.disp.disp_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Disp_T is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Color_Array",
       qualified_name: "Lv.Hal.Disp.Color_Array",
       signature: "lv.hal.disp.color_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Array is\n  array (0 .. Natural'Last) of aliased Lv.Color.Color_T with\n     Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Disp_Drv_T",
       qualified_name: "Lv.Hal.Disp.Disp_Drv_T",
       signature: "lv.hal.disp.disp_drv_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Disp_Drv_T is record\n   Disp_Flush : access procedure\n     (X1    : Int32_T;\n      Y1    : Int32_T;\n      X2    : Int32_T;\n      Y2    : Int32_T;\n      Color : access constant Color_Array);\n   Disp_Fill : access procedure\n     (X1    : Int32_T;\n      Y1    : Int32_T;\n      X2    : Int32_T;\n      Y2    : Int32_T;\n      Color : Lv.Color.Color_T);\n   Disp_Map : access procedure\n     (X1    : Int32_T;\n      Y1    : Int32_T;\n      X2    : Int32_T;\n      Y2    : Int32_T;\n      Color : access constant Color_Array);\n   Mem_Blend : access procedure\n     (Dest   : access Color_Array;\n      Src    : access constant Color_Array;\n      Length : Uint32_T;\n      Opa    : Lv.Color.Opa_T);\n   Mem_Fill : access procedure\n     (Dest   : access Color_Array;\n      Length : Uint32_T;\n      Color  : Lv.Color.Color_T);\n   Vdb_Wr : access procedure\n     (Arg1 : access Uint8_T;\n      Arg2 : Lv.Area.Coord_T;\n      Arg3 : Lv.Area.Coord_T;\n      Arg4 : Lv.Area.Coord_T;\n      Arg5 : Lv.Color.Color_T;\n      Arg6 : Lv.Color.Opa_T);\nend record;",
       }   ,
   ]
,}
---
