---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE_Fonts",
qualified_name: "GESTE_Fonts",
signature: "geste_fonts",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
array_types:    [
       {
       name: "Font_Bitmap",
       qualified_name: "GESTE_Fonts.Font_Bitmap",
       signature: "geste_fonts.font_bitmap",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Bitmap is array (Natural range <>) of Interfaces.Unsigned_8;",
       }   ,
   ]
,record_types:    [
       {
       name: "Bitmap_Font",
       qualified_name: "GESTE_Fonts.Bitmap_Font",
       signature: "geste_fonts.bitmap_font",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bitmap_Font is record\n   Bytes_Per_Glyph : Positive;\n   Glyph_Width     : Positive;\n   Glyph_Height    : Positive;\n   Data            : Font_Bitmap_Ref;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Bitmap_Font_Ref",
       qualified_name: "GESTE_Fonts.Bitmap_Font_Ref",
       signature: "geste_fonts.bitmap_font_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bitmap_Font_Ref is access constant Bitmap_Font;",
       }   ,
       {
       name: "Font_Bitmap_Ref",
       qualified_name: "GESTE_Fonts.Font_Bitmap_Ref",
       signature: "geste_fonts.font_bitmap_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Font_Bitmap_Ref is not null access constant Font_Bitmap;",
       }   ,
   ]
,}
---
