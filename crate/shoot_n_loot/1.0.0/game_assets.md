---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "Game_Assets",
qualified_name: "Game_Assets",
signature: "game_assets",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object_Kind",
       qualified_name: "Game_Assets.Object_Kind",
       signature: "game_assets.object_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Kind is (Rectangle_Obj, Point_Obj,\n  Ellipse_Obj, Polygon_Obj, Tile_Obj, Text_Obj);",
       }   ,
   ]
,array_types:    [
       {
       name: "Object_Array",
       qualified_name: "Game_Assets.Object_Array",
       signature: "game_assets.object_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Array is array (Natural range <>)\n   of Object;",
       }   ,
   ]
,record_types:    [
       {
       name: "Object",
       qualified_name: "Game_Assets.Object",
       signature: "game_assets.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object\n  (Kind : Object_Kind := Rectangle_Obj)\nis record\n   Name           : String_Access;\n   Id             : Natural;\n   X              : GESTE.Maths_Types.Value;\n   Y              : GESTE.Maths_Types.Value;\n   Width          : GESTE.Maths_Types.Value;\n   Height         : GESTE.Maths_Types.Value;\n   Str            : String_Access;\n   Flip_Vertical  : Boolean;\n   Flip_Horizontal: Boolean;\n   Tile_Id        : GESTE_Config.Tile_Index;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "String_Access",
       qualified_name: "Game_Assets.String_Access",
       signature: "game_assets.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is access all String;",
       }   ,
   ]
,variables:    [
       {
       name: "Palette",
       qualified_name: "Game_Assets.Palette",
       signature: "game_assets.palette",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Palette : aliased GESTE.Palette_Type := (\n   0 =>  10067,\n   1 =>  64278,\n   2 =>  0,\n   3 =>  36308,\n   4 =>  18363,\n   5 =>  29149,\n   6 =>  392,\n   7 =>  1162,\n   8 =>  52619,\n   9 =>  34954,\n   10 =>  22533,\n   11 =>  27596,\n   12 =>  62973,\n   13 =>  26185,\n   14 =>  64110,\n   15 =>  18364,\n   16 =>  11725,\n   17 =>  26259,\n   18 =>  58756,\n   19 =>  55774,\n   20 =>  62917,\n   21 =>  44708,\n   22 =>  27054,\n   23 =>  1132,\n   24 =>  49143,\n   25 =>  22181,\n   26 =>  49864,\n   27 =>  44251,\n   28 =>  62180,\n   29 =>  42690,\n   30 =>  58600,\n   31 =>  59193,\n   32 =>  59134,\n   33 =>  33023,\n   34 =>  6342,\n   35 =>  45716,\n   36 =>  15591,\n   37 =>  56286,\n   38 =>  42597,\n   39 =>  51491,\n   40 =>  46029,\n   41 =>  48639,\n   42 =>  24592,\n   43 =>  10314,\n   44 =>  12403,\n   45 =>  11082,\n   46 =>  80,\n   47 =>  60250,\n   48 =>  65535,\n   49 =>  59199,\n   50 =>  59343,\n   51 =>  58669,\n   52 =>  24840,\n   53 =>  16638,\n   54 =>  49404,\n   55 =>  251,\n   56 =>  16577,\n   57 =>  136,\n   58 =>  57343,\n   59 =>  8642,\n   60 =>  32239,\n   61 =>  31182,\n   62 =>  20876,\n   63 =>  10306,\n   64 =>  11363,\n   65 =>  1057,\n   66 =>  21933,\n   67 =>  31183,\n   68 =>  19556,\n   69 =>  30126,\n   70 =>  10307,\n   71 =>  1,\n   72 =>  20877,\n   73 =>  9250,\n   74 =>  38399,\n   75 =>  33020,\n   76 =>  16894,\n   77 =>  9065);",
       }   ,
   ]
,}
---
