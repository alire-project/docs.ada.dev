---
crate: usb_embedded
layout: gnatdoc
gnatdoc: {
name: "USB.Device.HID.Gamepad",
qualified_name: "USB.Device.HID.Gamepad",
signature: "usb.device.hid.gamepad",
enclosing: "usb.device.hid",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2018-2021, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Axis",
       qualified_name: "USB.Device.HID.Gamepad.Axis",
       signature: "usb.device.hid.gamepad.axis",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis is (X, Y, Z, Rx, Ry, Rz);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Instance",
       qualified_name: "USB.Device.HID.Gamepad.Instance",
       signature: "usb.device.hid.gamepad.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance\nis new Parent (Gamepad_Report_Size)\nwith private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Parent",
       qualified_name: "USB.Device.HID.Gamepad.Parent",
       signature: "usb.device.hid.gamepad.parent",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Parent is Abstract_HID_Class;",
       }   ,
   ]
,constants:    [
       {
       name: "Gamepad_Report_Size",
       qualified_name: "USB.Device.HID.Gamepad.Gamepad_Report_Size",
       signature: "usb.device.hid.gamepad.gamepad_report_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Gamepad_Report_Size : constant := 7;",
       }   ,
   ]
,}
---
