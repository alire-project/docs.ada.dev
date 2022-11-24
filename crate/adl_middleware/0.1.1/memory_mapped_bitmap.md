---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Memory_Mapped_Bitmap",
qualified_name: "Memory_Mapped_Bitmap",
signature: "memory_mapped_bitmap",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2017, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Memory_Mapped_Bitmap_Buffer",
       qualified_name: "Memory_Mapped_Bitmap.Memory_Mapped_Bitmap_Buffer",
       signature: "memory_mapped_bitmap.memory_mapped_bitmap_buffer",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Addr\n@field Actual_Width\n  Width and Height of the buffer. Note that it's the user-visible width\n  (see below for the meaning of the Swapped value).\n@field Actual_Height\n  Width and Height of the buffer. Note that it's the user-visible width\n  (see below for the meaning of the Swapped value).\n@field Actual_Color_Mode\n  The buffer color mode. Note that not all color modes are supported by\n  the hardware acceleration (if any), so you need to check your actual\n  hardware to optimize buffer transfers.\n@field Currently_Swapped\n  If Swap is set, then operations on this buffer will consider:\n  Width0 = Height\n  Height0 = Width\n  Y0 = Buffer.Width - X - 1\n  X0 = Y\n  \n  As an example, the Bitmap buffer that corresponds to a 240x320\n  swapped display (to display images in landscape mode) with have\n  the following values:\n  Width => 320\n  Height => 240\n  Swapped => True\n  So Put_Pixel (Buffer, 30, 10, Color) will place the pixel at\n  Y0 = 320 - 30 - 1 = 289\n  X0 = 10\n@field Native_Source",
       documentation_snippet: "type Memory_Mapped_Bitmap_Buffer is new Parent with record\n   Addr              : System.Address;\n   Actual_Width      : Natural;\n   Actual_Height     : Natural;\n   Actual_Color_Mode : Bitmap_Color_Mode;\n   Currently_Swapped : Boolean := False;\n   Native_Source : UInt32 := 0;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Memory_Mapped_Bitmap_Buffer",
       qualified_name: "Memory_Mapped_Bitmap.Any_Memory_Mapped_Bitmap_Buffer",
       signature: "memory_mapped_bitmap.any_memory_mapped_bitmap_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Memory_Mapped_Bitmap_Buffer is access all Memory_Mapped_Bitmap_Buffer'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "Memory_Mapped_Bitmap.Parent",
       signature: "memory_mapped_bitmap.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Soft_Drawing_Bitmap_Buffer;",
       }   ,
   ]
,}
---
