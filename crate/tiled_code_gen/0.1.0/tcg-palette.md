---
crate: tiled_code_gen
layout: gnatdoc
gnatdoc: {
name: "TCG.Palette",
qualified_name: "TCG.Palette",
signature: "tcg.palette",
enclosing: "tcg",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                             tiled-code-gen                               --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Color_Id",
       qualified_name: "TCG.Palette.Color_Id",
       signature: "tcg.palette.color_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Id is new Natural;",
       }   ,
       {
       name: "Output_Color_Format",
       qualified_name: "TCG.Palette.Output_Color_Format",
       signature: "tcg.palette.output_color_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Output_Color_Format is (ARGB, RGB565, RGB565_Swap, RGB555, RGB888);",
       }   ,
   ]
,record_types:    [
       {
       name: "ARGB_Color",
       qualified_name: "TCG.Palette.ARGB_Color",
       signature: "tcg.palette.argb_color",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ARGB_Color is record\n   A, R, G, B : Component;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Component",
       qualified_name: "TCG.Palette.Component",
       signature: "tcg.palette.component",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Component is Interfaces.Unsigned_8;",
       }   ,
   ]
,}
---
