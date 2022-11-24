---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE",
qualified_name: "GESTE",
signature: "geste",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
packages:    [
       {
       name: "Layer",
       qualified_name: "GESTE.Layer",
       signature: "geste.layer",
       enclosing: "geste",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
access_types:           [
              {
              name: "Const_Ref",
              qualified_name: "GESTE.Layer.Const_Ref",
              signature: "geste.layer.const_ref",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Const_Ref is access constant Class;",
              }          ,
              {
              name: "Ref",
              qualified_name: "GESTE.Layer.Ref",
              signature: "geste.layer.ref",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Ref is access all Class;",
              }          ,
          ]
,subtypes:           [
              {
              name: "Class",
              qualified_name: "GESTE.Layer.Class",
              signature: "geste.layer.class",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Class is Instance'Class;",
              }          ,
              {
              name: "Instance",
              qualified_name: "GESTE.Layer.Instance",
              signature: "geste.layer.instance",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "subtype Instance is Layer_Type;",
              }          ,
          ]
,       }   ,
   ]
,simple_types:    [
       {
       name: "Layer_Priority",
       qualified_name: "GESTE.Layer_Priority",
       signature: "geste.layer_priority",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Layer_Priority is new Natural;",
       }   ,
   ]
,array_types:    [
       {
       name: "Output_Buffer",
       qualified_name: "GESTE.Output_Buffer",
       signature: "geste.output_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Output_Buffer is array (Output_Buffer_Index range <>) of Output_Color;",
       }   ,
       {
       name: "Palette_Type",
       qualified_name: "GESTE.Palette_Type",
       signature: "geste.palette_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Palette_Type is array (Color_Index) of Output_Color;",
       }   ,
       {
       name: "Tile",
       qualified_name: "GESTE.Tile",
       signature: "geste.tile",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile is array (0 .. Tile_Size - 1,\n                    0 .. Tile_Size - 1)\n  of Color_Index;",
       }   ,
       {
       name: "Tile_Array",
       qualified_name: "GESTE.Tile_Array",
       signature: "geste.tile_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Array is array (Tile_Index range <>) of Tile;",
       }   ,
       {
       name: "Tile_Collisions",
       qualified_name: "GESTE.Tile_Collisions",
       signature: "geste.tile_collisions",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Collisions is array (0 .. Tile_Size - 1,\n                               0 .. Tile_Size - 1)\n  of Boolean;",
       }   ,
       {
       name: "Tile_Collisions_Array",
       qualified_name: "GESTE.Tile_Collisions_Array",
       signature: "geste.tile_collisions_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Collisions_Array is array (Tile_Index range <>)\n  of Tile_Collisions;",
       }   ,
   ]
,record_types:    [
       {
       name: "Pix_Point",
       qualified_name: "GESTE.Pix_Point",
       signature: "geste.pix_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pix_Point is record\n   X, Y : Integer;\nend record;",
       }   ,
       {
       name: "Pix_Rect",
       qualified_name: "GESTE.Pix_Rect",
       signature: "geste.pix_rect",
       enclosing: "",
       is_private: false,
       documentation: "\n@field TL\n  Top Left\n@field BR\n  Bottom right",
       documentation_snippet: "type Pix_Rect is record\n   TL : Pix_Point;\n   BR : Pix_Point;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Layer_Type",
       qualified_name: "GESTE.Layer_Type",
       signature: "geste.layer_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Layer_Type is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Palette_Ref",
       qualified_name: "GESTE.Palette_Ref",
       signature: "geste.palette_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Palette_Ref is access constant Palette_Type;",
       }   ,
       {
       name: "Push_Pixels_Proc",
       qualified_name: "GESTE.Push_Pixels_Proc",
       signature: "geste.push_pixels_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Push_Pixels_Proc is\n  access procedure (Buffer : Output_Buffer);",
       }   ,
       {
       name: "Set_Drawing_Area_Proc",
       qualified_name: "GESTE.Set_Drawing_Area_Proc",
       signature: "geste.set_drawing_area_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Set_Drawing_Area_Proc is access procedure (Area : Pix_Rect);",
       }   ,
       {
       name: "Tile_Array_Ref",
       qualified_name: "GESTE.Tile_Array_Ref",
       signature: "geste.tile_array_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Array_Ref is access constant Tile_Array;",
       }   ,
       {
       name: "Tile_Collisions_Array_Ref",
       qualified_name: "GESTE.Tile_Collisions_Array_Ref",
       signature: "geste.tile_collisions_array_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tile_Collisions_Array_Ref is access constant Tile_Collisions_Array;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Output_Buffer_Index",
       qualified_name: "GESTE.Output_Buffer_Index",
       signature: "geste.output_buffer_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Output_Buffer_Index is Natural;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Collisions",
       qualified_name: "GESTE.No_Collisions",
       signature: "geste.no_collisions",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Collisions : constant Tile_Collisions_Array_Ref := null;",
       }   ,
       {
       name: "No_Palette",
       qualified_name: "GESTE.No_Palette",
       signature: "geste.no_palette",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Palette : constant Palette_Ref := null;",
       }   ,
   ]
,}
---
