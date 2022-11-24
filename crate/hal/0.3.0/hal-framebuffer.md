---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.Framebuffer",
qualified_name: "HAL.Framebuffer",
signature: "hal.framebuffer",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Display_Orientation",
       qualified_name: "HAL.Framebuffer.Display_Orientation",
       signature: "hal.framebuffer.display_orientation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Display_Orientation is\n  (Default, Landscape, Portrait);",
       }   ,
       {
       name: "Wait_Mode",
       qualified_name: "HAL.Framebuffer.Wait_Mode",
       signature: "hal.framebuffer.wait_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wait_Mode is (Polling, Interrupt);",
       }   ,
   ]
,interface_types:    [
       {
       name: "Frame_Buffer_Display",
       qualified_name: "HAL.Framebuffer.Frame_Buffer_Display",
       signature: "hal.framebuffer.frame_buffer_display",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Frame_Buffer_Display is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Frame_Buffer_Display",
       qualified_name: "HAL.Framebuffer.Any_Frame_Buffer_Display",
       signature: "hal.framebuffer.any_frame_buffer_display",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Frame_Buffer_Display is access all Frame_Buffer_Display'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "FB_Color_Mode",
       qualified_name: "HAL.Framebuffer.FB_Color_Mode",
       signature: "hal.framebuffer.fb_color_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype FB_Color_Mode is HAL.Bitmap.Bitmap_Color_Mode range\n  HAL.Bitmap.ARGB_8888 .. HAL.Bitmap.M_1;",
       }   ,
   ]
,}
---
