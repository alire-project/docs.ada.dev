---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Base_Types.Register_Properties",
qualified_name: "Base_Types.Register_Properties",
signature: "base_types.register_properties",
enclosing: "base_types",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2016, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Register_Properties_T",
       qualified_name: "Base_Types.Register_Properties.Register_Properties_T",
       signature: "base_types.register_properties.register_properties_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Register_Properties_T is record\n   Size        : Natural := 0;\n   Reg_Access  : Access_Type := Read_Write;\n   Protection  : Protection_Type := Undefined_Protection;\n   Reset_Value : Unsigned := 0;\n   Reset_Mask  : Unsigned := 0;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Register_Property",
       qualified_name: "Base_Types.Register_Properties.Null_Register_Property",
       signature: "base_types.register_properties.null_register_property",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Register_Property : constant Register_Properties_T := (others => <>);",
       }   ,
   ]
,}
---
