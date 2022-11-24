---
crate: usb_embedded
layout: gnatdoc
gnatdoc: {
name: "USB.HAL.Device",
qualified_name: "USB.HAL.Device",
signature: "usb.hal.device",
enclosing: "usb.hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                        Copyright (C) 2021, AdaCore                       --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "UDC_Event_Kind",
       qualified_name: "USB.HAL.Device.UDC_Event_Kind",
       signature: "usb.hal.device.udc_event_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UDC_Event_Kind is (None,\n                        Reset,\n                        Setup_Request,\n                        Transfer_Complete);",
       }   ,
   ]
,record_types:    [
       {
       name: "UDC_Event",
       qualified_name: "USB.HAL.Device.UDC_Event",
       signature: "usb.hal.device.udc_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UDC_Event (Kind : UDC_Event_Kind := None) is record\n   case Kind is\n      when Setup_Request =>\n         Req    : Setup_Data;\n         Req_EP : EP_Id;\n      when Transfer_Complete =>\n         EP   : EP_Addr;\n         BCNT : Packet_Size;\n      when others => null;\n   end case;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "USB_Device_Controller",
       qualified_name: "USB.HAL.Device.USB_Device_Controller",
       signature: "usb.hal.device.usb_device_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_Device_Controller is interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_USB_Device_Controller",
       qualified_name: "USB.HAL.Device.Any_USB_Device_Controller",
       signature: "usb.hal.device.any_usb_device_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_USB_Device_Controller is access all USB_Device_Controller'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Event",
       qualified_name: "USB.HAL.Device.No_Event",
       signature: "usb.hal.device.no_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Event : constant UDC_Event := (Kind => None);",
       }   ,
   ]
,}
---
