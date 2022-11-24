---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE_Config",
qualified_name: "GESTE_Config",
signature: "geste_config",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Color_Index",
       qualified_name: "GESTE_Config.Color_Index",
       signature: "geste_config.color_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Index is range  0 ..  77;",
       }   ,
       {
       name: "Tile_Index",
       qualified_name: "GESTE_Config.Tile_Index",
       signature: "geste_config.tile_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Index is range 0 .. 194;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Output_Color",
       qualified_name: "GESTE_Config.Output_Color",
       signature: "geste_config.output_color",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Output_Color is Interfaces.Unsigned_16;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Tile",
       qualified_name: "GESTE_Config.No_Tile",
       signature: "geste_config.no_tile",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Tile : constant Tile_Index := 0;",
       }   ,
       {
       name: "Tile_Size",
       qualified_name: "GESTE_Config.Tile_Size",
       signature: "geste_config.tile_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Tile_Size : constant :=  8;",
       }   ,
       {
       name: "Transparent",
       qualified_name: "GESTE_Config.Transparent",
       signature: "geste_config.transparent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Transparent : constant Output_Color :=  10067;",
       }   ,
   ]
,}
---
