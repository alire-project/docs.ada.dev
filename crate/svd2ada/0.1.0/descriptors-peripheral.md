---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Peripheral",
qualified_name: "Descriptors.Peripheral",
signature: "descriptors.peripheral",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2016, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
interface_types:    [
       {
       name: "Peripheral_Db",
       qualified_name: "Descriptors.Peripheral.Peripheral_Db",
       signature: "descriptors.peripheral.peripheral_db",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Peripheral_Db is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Peripheral_T",
       qualified_name: "Descriptors.Peripheral.Peripheral_T",
       signature: "descriptors.peripheral.peripheral_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Peripheral_T is new Register_Db and Cluster_Db with record\n   Name            : Unbounded.Unbounded_String;\n   Type_Name       : Unbounded.Unbounded_String;\n   Version         : Unbounded.Unbounded_String;\n   Description     : Unbounded.Unbounded_String;\n   Group_Name      : Unbounded.Unbounded_String;\n   Prepend_To_Name : Unbounded.Unbounded_String;\n   Append_To_Name  : Unbounded.Unbounded_String;\n   Base_Address    : Unsigned := 0;\n   Reg_Properties  : Register_Properties_T := Null_Register_Property;\n   Address_Blocks  : Address_Block_Vectors.Vector;\n   Interrupts      : Interrupt_Vectors.Vector;\n   Content         : Peripheral_Element_Vectors.Vector;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Peripheral_Access",
       qualified_name: "Descriptors.Peripheral.Peripheral_Access",
       signature: "descriptors.peripheral.peripheral_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Peripheral_Access is access all Peripheral_T;",
       }   ,
   ]
,}
---
