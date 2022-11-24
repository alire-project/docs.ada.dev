---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE.Grid",
qualified_name: "GESTE.Grid",
signature: "geste.grid",
enclosing: "geste",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Grid_Data",
       qualified_name: "GESTE.Grid.Grid_Data",
       signature: "geste.grid.grid_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grid_Data is array (Natural range <>, Natural range <>) of Tile_Index;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "GESTE.Grid.Instance",
       signature: "geste.grid.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance (Data : not null Grid_Data_Ref;\n               Bank : not null Tile_Bank.Const_Ref)\nis new Parent with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Const_Ref",
       qualified_name: "GESTE.Grid.Const_Ref",
       signature: "geste.grid.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref is access constant Class;",
       }   ,
       {
       name: "Grid_Data_Ref",
       qualified_name: "GESTE.Grid.Grid_Data_Ref",
       signature: "geste.grid.grid_data_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Grid_Data_Ref is access constant Grid_Data;",
       }   ,
       {
       name: "Ref",
       qualified_name: "GESTE.Grid.Ref",
       signature: "geste.grid.ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ref is access all Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "GESTE.Grid.Class",
       signature: "geste.grid.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
       {
       name: "Parent",
       qualified_name: "GESTE.Grid.Parent",
       signature: "geste.grid.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Layer.Instance;",
       }   ,
   ]
,}
---
