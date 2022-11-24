---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "GESTE.Text",
qualified_name: "GESTE.Text",
signature: "geste.text",
enclosing: "geste",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                   GESTE                                  --\n                                                                          --\n                    Copyright (C) 2018 Fabien Chouteau                    --\n                                                                          --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Instance",
       qualified_name: "GESTE.Text.Instance",
       signature: "geste.text.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance (Da_Font           : not null GESTE_Fonts.Bitmap_Font_Ref;\n               Number_Of_Columns : Positive;\n               Number_Of_Lines   : Positive;\n               Foreground        : Output_Color;\n               Background        : Output_Color)\nis new Parent with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Const_Ref",
       qualified_name: "GESTE.Text.Const_Ref",
       signature: "geste.text.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref is access constant Class;",
       }   ,
       {
       name: "Ref",
       qualified_name: "GESTE.Text.Ref",
       signature: "geste.text.ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ref is access all Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "GESTE.Text.Class",
       signature: "geste.text.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
       {
       name: "Parent",
       qualified_name: "GESTE.Text.Parent",
       signature: "geste.text.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Layer.Instance;",
       }   ,
   ]
,}
---
