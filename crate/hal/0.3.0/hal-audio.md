---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.Audio",
qualified_name: "HAL.Audio",
signature: "hal.audio",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Audio_Frequency",
       qualified_name: "HAL.Audio.Audio_Frequency",
       signature: "hal.audio.audio_frequency",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Frequency is\n  (Audio_Freq_8kHz,\n   Audio_Freq_11kHz,\n   Audio_Freq_16kHz,\n   Audio_Freq_22kHz,\n   Audio_Freq_32kHz,\n   Audio_Freq_44kHz,\n   Audio_Freq_48kHz,\n   Audio_Freq_96kHz)\n  with Size => 32;",
       }   ,
       {
       name: "Audio_Volume",
       qualified_name: "HAL.Audio.Audio_Volume",
       signature: "hal.audio.audio_volume",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Volume is new Natural range 0 .. 100;",
       }   ,
   ]
,array_types:    [
       {
       name: "Audio_Buffer",
       qualified_name: "HAL.Audio.Audio_Buffer",
       signature: "hal.audio.audio_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Buffer is array (Natural range <>) of Integer_16\n  with Component_Size => 16, Alignment => 2;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Audio_Stream",
       qualified_name: "HAL.Audio.Audio_Stream",
       signature: "hal.audio.audio_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Audio_Stream is limited interface;",
       }   ,
   ]
,}
---
