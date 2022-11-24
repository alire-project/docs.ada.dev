---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "Markers",
qualified_name: "Game_Assets.level_4.Markers",
signature: "game_assets.level_4.markers",
enclosing: "game_assets.level_4",
is_private: false,
documentation: "",
documentation_snippet: "",
constants:    [
       {
       name: "Finish",
       qualified_name: "Game_Assets.level_4.Markers.Finish",
       signature: "game_assets.level_4.markers.finish",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Finish : aliased constant Object := (\n  Kind => POINT_OBJ,\n  Id   =>  16,\n  Name => new String'(\"Finish\"),\n  X    =>  1.52000E+02,\n  Y    =>  1.12000E+02,\n  Width =>  8.00000E+00,\n  Height =>  8.00000E+00,\n  Flip_Vertical => FALSE,\n  Flip_Horizontal => FALSE,\n  Tile_Id =>  66,\n  Str => null\n  );",
       }   ,
       {
       name: "Spawn",
       qualified_name: "Game_Assets.level_4.Markers.Spawn",
       signature: "game_assets.level_4.markers.spawn",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Spawn : aliased constant Object := (\n  Kind => POINT_OBJ,\n  Id   =>  12,\n  Name => new String'(\"Spawn\"),\n  X    =>  8.00000E+00,\n  Y    =>  9.60000E+01,\n  Width =>  8.00000E+00,\n  Height =>  8.00000E+00,\n  Flip_Vertical => FALSE,\n  Flip_Horizontal => TRUE,\n  Tile_Id =>  4,\n  Str => null\n  );",
       }   ,
   ]
,variables:    [
       {
       name: "Objects",
       qualified_name: "Game_Assets.level_4.Markers.Objects",
       signature: "game_assets.level_4.markers.objects",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Objects : Object_Array :=\n  (\n     0 => (\n      Kind => POINT_OBJ,\n      Id   =>  12,\n      Name => new String'(\"Spawn\"),\n      X    =>  8.00000E+00,\n      Y    =>  9.60000E+01,\n      Width =>  8.00000E+00,\n      Height =>  8.00000E+00,\n      Flip_Vertical => FALSE,\n      Flip_Horizontal => TRUE,\n      Tile_Id =>  4,\n      Str => null\n    ),\n     1 => (\n      Kind => POINT_OBJ,\n      Id   =>  16,\n      Name => new String'(\"Finish\"),\n      X    =>  1.52000E+02,\n      Y    =>  1.12000E+02,\n      Width =>  8.00000E+00,\n      Height =>  8.00000E+00,\n      Flip_Vertical => FALSE,\n      Flip_Horizontal => FALSE,\n      Tile_Id =>  66,\n      Str => null\n    )\n  );",
       }   ,
   ]
,}
---
