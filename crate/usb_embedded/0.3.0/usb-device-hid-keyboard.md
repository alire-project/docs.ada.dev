---
crate: usb_embedded
layout: gnatdoc
gnatdoc: {
name: "USB.Device.HID.Keyboard",
qualified_name: "USB.Device.HID.Keyboard",
signature: "usb.device.hid.keyboard",
enclosing: "usb.device.hid",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2018-2021, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "LEDs",
       qualified_name: "USB.Device.HID.Keyboard.LEDs",
       signature: "usb.device.hid.keyboard.leds",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type LEDs is (Num_Lock, Caps_Lock, Scroll_Lock, Compose, Kana);",
       }   ,
       {
       name: "Modifiers",
       qualified_name: "USB.Device.HID.Keyboard.Modifiers",
       signature: "usb.device.hid.keyboard.modifiers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Modifiers is (Ctrl_Left, Shift_Left, Alt_Left, Meta_Left,\n                   Ctrl_Right, Shift_Right, Alt_Right, Meta_Right);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "USB.Device.HID.Keyboard.Instance",
       signature: "usb.device.hid.keyboard.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance\nis new Parent (Keyboard_Report_Size)\nwith private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "USB.Device.HID.Keyboard.Parent",
       signature: "usb.device.hid.keyboard.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Abstract_HID_Class;",
       }   ,
   ]
,constants:    [
       {
       name: "Keyboard_Report_Size",
       qualified_name: "USB.Device.HID.Keyboard.Keyboard_Report_Size",
       signature: "usb.device.hid.keyboard.keyboard_report_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Keyboard_Report_Size : constant := Max_Key_Codes + 2;",
       }   ,
       {
       name: "Max_Key_Codes",
       qualified_name: "USB.Device.HID.Keyboard.Max_Key_Codes",
       signature: "usb.device.hid.keyboard.max_key_codes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Max_Key_Codes : constant := 6;",
       }   ,
   ]
,}
---
