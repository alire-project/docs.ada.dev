---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.USB_Device",
qualified_name: "STM32.USB_Device",
signature: "stm32.usb_device",
enclosing: "stm32",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n                                                                           --\n                              STM32F0 USB                                  --\n                                                                           --\n                  Copyright (C) 2022      Marc PoulhiÃ¨s                    --\n                                                                           --\n    STM32F0 USB is free software: you can redistribute it and/or           --\n    modify it under the terms of the GNU General Public License as         --\n    published by the Free Software Foundation, either version 3 of the     --\n    License, or (at your option) any later version.                        --\n                                                                           --\n    STM32F0 USB is distributed in the hope that it will be useful,         --\n    but WITHOUT ANY WARRANTY; without even the implied warranty of         --\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU       --\n    General Public License for more details.                               --\n                                                                           --\n    You should have received a copy of the GNU General Public License      --\n    along with STM32F0 USB. If not, see <http://www.gnu.org/licenses/>.    --\n                                                                           --\n-----------------------------------------------------------------------------\n\n  SPDX-License-Identifier: GPL-3.0-or-later",
documentation_snippet: "",
tagged_types:    [
       {
       name: "UDC",
       qualified_name: "STM32.USB_Device.UDC",
       signature: "stm32.usb_device.udc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type UDC is new USB_Device_Controller with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Num_Endpoints",
       qualified_name: "STM32.USB_Device.Num_Endpoints",
       signature: "stm32.usb_device.num_endpoints",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Num_Endpoints : constant := 8;",
       }   ,
   ]
,}
---
