---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE.Sprite.Animated",
qualified_name: "GESTE.Sprite.Animated",
signature: "geste.sprite.animated",
enclosing: "geste.sprite",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2019 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Frame_Counter",
       qualified_name: "GESTE.Sprite.Animated.Frame_Counter",
       signature: "geste.sprite.animated.frame_counter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Frame_Counter is new Natural;",
       }   ,
   ]
,array_types:    [
       {
       name: "Animation_Array",
       qualified_name: "GESTE.Sprite.Animated.Animation_Array",
       signature: "geste.sprite.animated.animation_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Animation_Array is array (Natural range <>) of Animation_Step;",
       }   ,
   ]
,record_types:    [
       {
       name: "Animation_Step",
       qualified_name: "GESTE.Sprite.Animated.Animation_Step",
       signature: "geste.sprite.animated.animation_step",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Animation_Step is record\n   Tile      : GESTE_Config.Tile_Index;\n   Frame_Cnt : Frame_Counter;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "GESTE.Sprite.Animated.Instance",
       signature: "geste.sprite.animated.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance is new Parent with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Animation",
       qualified_name: "GESTE.Sprite.Animated.Animation",
       signature: "geste.sprite.animated.animation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Animation is not null access constant Animation_Array;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "GESTE.Sprite.Animated.Parent",
       signature: "geste.sprite.animated.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Sprite.Instance;",
       }   ,
   ]
,variables:    [
       {
       name: "No_Animation",
       qualified_name: "GESTE.Sprite.Animated.No_Animation",
       signature: "geste.sprite.animated.no_animation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Animation : Animation := No_Animation_Array'Access;",
       }   ,
       {
       name: "No_Animation_Array",
       qualified_name: "GESTE.Sprite.Animated.No_Animation_Array",
       signature: "geste.sprite.animated.no_animation_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Animation_Array : aliased Animation_Array :=\n  (1 .. 0 => (GESTE_Config.No_Tile,\n              Frame_Counter'Last));",
       }   ,
   ]
,}
---
