---
crate: tiled_code_gen
layout: gnatdoc
gnatdoc: {
name: "TCG.Object_Groups",
qualified_name: "TCG.Object_Groups",
signature: "tcg.object_groups",
enclosing: "tcg",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                             tiled-code-gen                               --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object_Group",
       qualified_name: "TCG.Object_Groups.Object_Group",
       signature: "tcg.object_groups.object_group",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Group is private;",
       }   ,
       {
       name: "Object_Group_Id",
       qualified_name: "TCG.Object_Groups.Object_Group_Id",
       signature: "tcg.object_groups.object_group_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Group_Id is new Integer;",
       }   ,
       {
       name: "Object_Kind",
       qualified_name: "TCG.Object_Groups.Object_Kind",
       signature: "tcg.object_groups.object_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Kind is (Rectangle_Obj, Point_Obj, Ellipse_Obj,\n                     Polygon_Obj, Tile_Obj, Text_Obj);",
       }   ,
   ]
,array_types:    [
       {
       name: "Polygon",
       qualified_name: "TCG.Object_Groups.Polygon",
       signature: "tcg.object_groups.polygon",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Polygon is array (Positive range <>) of Point;",
       }   ,
   ]
,record_types:    [
       {
       name: "Object",
       qualified_name: "TCG.Object_Groups.Object",
       signature: "tcg.object_groups.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Kind : Object_Kind := Rectangle_Obj)\nis record\n   Name            : String_Access;\n   Id              : Natural;\n   Pt              : Point;\n   Width, Height   : Float;\n   Points          : Polygon_Access;\n   Str             : String_Access;\n   Flip_Vertical   : Boolean;\n   Flip_Horizontal : Boolean;\n   Tile_Id         : TCG.Tilesets.Map_Tile_Id;\nend record;",
       }   ,
       {
       name: "Point",
       qualified_name: "TCG.Object_Groups.Point",
       signature: "tcg.object_groups.point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point is record\n   X, Y : Float;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Polygon_Access",
       qualified_name: "TCG.Object_Groups.Polygon_Access",
       signature: "tcg.object_groups.polygon_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Polygon_Access is access all Polygon;",
       }   ,
       {
       name: "String_Access",
       qualified_name: "TCG.Object_Groups.String_Access",
       signature: "tcg.object_groups.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is access all String;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Layer",
       qualified_name: "TCG.Object_Groups.No_Layer",
       signature: "tcg.object_groups.no_layer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Layer : constant Object_Group;",
       }   ,
   ]
,}
---
