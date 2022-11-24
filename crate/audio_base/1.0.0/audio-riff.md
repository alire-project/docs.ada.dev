---
crate: audio_base
layout: gnatdoc
gnatdoc: {
name: "Audio.RIFF",
qualified_name: "Audio.RIFF",
signature: "audio.riff",
enclosing: "audio",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                                 AUDIO                                    --\n                                                                          --\n                         Common RIFF information                          --\n                                                                          --\n  The MIT License (MIT)                                                   --\n                                                                          --\n  Copyright (c) 2015 -- 2020 Gustavo A. Hoffmann                          --\n                                                                          --\n  Permission is hereby granted, free of charge, to any person obtaining   --\n  a copy of this software and associated documentation files (the         --\n  \"Software\"), to deal in the Software without restriction, including     --\n  without limitation the rights to use, copy, modify, merge, publish,     --\n  distribute, sublicense, and / or sell copies of the Software, and to    --\n  permit persons to whom the Software is furnished to do so, subject to   --\n  the following conditions:                                               --\n                                                                          --\n  The above copyright notice and this permission notice shall be          --\n  included in all copies or substantial portions of the Software.         --\n                                                                          --\n  THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,         --\n  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF      --\n  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  --\n  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY    --\n  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,    --\n  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE       --\n  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                  --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "RIFF_Chunk_Header",
       qualified_name: "Audio.RIFF.RIFF_Chunk_Header",
       signature: "audio.riff.riff_chunk_header",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RIFF_Chunk_Header is\n   record\n      ID   : FOURCC_String;\n      Size : Unsigned_32;\n   end record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "FOURCC_String",
       qualified_name: "Audio.RIFF.FOURCC_String",
       signature: "audio.riff.fourcc_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype FOURCC_String is String (1 .. 4);",
       }   ,
   ]
,}
---