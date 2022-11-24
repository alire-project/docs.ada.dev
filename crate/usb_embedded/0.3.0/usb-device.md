---
crate: usb_embedded
layout: gnatdoc
gnatdoc: {
name: "USB.Device",
qualified_name: "USB.Device",
signature: "usb.device",
enclosing: "usb",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2018-2021, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Init_Result",
       qualified_name: "USB.Device.Init_Result",
       signature: "usb.device.init_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Init_Result is (Ok, Not_Enough_EPs, Not_Enough_EP_Buffer);",
       }   ,
   ]
,interface_types:    [
       {
       name: "USB_Device_Class",
       qualified_name: "USB.Device.USB_Device_Class",
       signature: "usb.device.usb_device_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_Device_Class is limited interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "USB_Device_Stack",
       qualified_name: "USB.Device.USB_Device_Stack",
       signature: "usb.device.usb_device_stack",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_Device_Stack (Max_Classes : Class_Index) is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_USB_Device_Class",
       qualified_name: "USB.Device.Any_USB_Device_Class",
       signature: "usb.device.any_usb_device_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_USB_Device_Class is access all USB_Device_Class'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class_Index",
       qualified_name: "USB.Device.Class_Index",
       signature: "usb.device.class_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class_Index is UInt8;",
       }   ,
   ]
,}
---
