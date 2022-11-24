---
crate: usb_embedded
layout: gnatdoc
gnatdoc: {
name: "USB.Device.MIDI",
qualified_name: "USB.Device.MIDI",
signature: "usb.device.midi",
enclosing: "usb.device",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2018-2021, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Default_MIDI_Class",
       qualified_name: "USB.Device.MIDI.Default_MIDI_Class",
       signature: "usb.device.midi.default_midi_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_MIDI_Class (TX_Buffer_Size, RX_Buffer_Size : BBqueue.Count)\nis limited new USB_Device_Class with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "MIDI_Event",
       qualified_name: "USB.Device.MIDI.MIDI_Event",
       signature: "usb.device.midi.midi_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype MIDI_Event is Standard.HAL.UInt32;",
       }   ,
   ]
,}
---
