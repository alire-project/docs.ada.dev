---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Device",
qualified_name: "Descriptors.Device",
signature: "descriptors.device",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2016, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Device_T",
       qualified_name: "Descriptors.Device.Device_T",
       signature: "descriptors.device.device_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Device_T is new Peripheral_Db with record\n   Name              : Unbounded.Unbounded_String;\n   Version           : Unbounded.Unbounded_String;\n   Description       : Unbounded.Unbounded_String;\n   Short_Desc        : Unbounded.Unbounded_String;\n   Address_Unit_Bits : Unsigned := 0;\n   Width             : Natural := 0;\n   Has_FPU           : Boolean := True;\n   Reg_Properties    : Register_Properties.Register_Properties_T;\n   Peripherals       : Peripheral_Vectors.Vector;\nend record;",
       }   ,
   ]
,}
---
