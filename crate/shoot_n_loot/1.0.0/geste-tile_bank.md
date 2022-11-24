---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE.Tile_Bank",
qualified_name: "GESTE.Tile_Bank",
signature: "geste.tile_bank",
enclosing: "geste",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Instance",
       qualified_name: "GESTE.Tile_Bank.Instance",
       signature: "geste.tile_bank.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance (Tiles      : not null Tile_Array_Ref;\n               Collisions :          Tile_Collisions_Array_Ref;\n               Palette    :          Palette_Ref)\nis tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Const_Ref",
       qualified_name: "GESTE.Tile_Bank.Const_Ref",
       signature: "geste.tile_bank.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref is access constant Class;",
       }   ,
       {
       name: "Ref",
       qualified_name: "GESTE.Tile_Bank.Ref",
       signature: "geste.tile_bank.ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ref is access all Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "GESTE.Tile_Bank.Class",
       signature: "geste.tile_bank.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
   ]
,}
---
