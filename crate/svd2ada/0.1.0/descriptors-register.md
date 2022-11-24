---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Register",
qualified_name: "Descriptors.Register",
signature: "descriptors.register",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2016, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Register_T",
       qualified_name: "Descriptors.Register.Register_T",
       signature: "descriptors.register.register_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Register_T is record\n   Xml_Id           : Unbounded.Unbounded_String;\n   Name             : Unbounded.Unbounded_String;\n   Display_Name     : Unbounded.Unbounded_String;\n   Description      : Unbounded.Unbounded_String;\n   Alternate_Group  : Unbounded.Unbounded_String;\n   Alternate_Reg    : Unbounded.Unbounded_String;\n   Address_Offset   : Natural;\n   Reg_Properties   : Register_Properties_T;\n   Mod_Write_Values : Modified_Write_Values_Type := Modify;\n   Read_Action      : Read_Action_Type := Undefined_Read_Action;\n   Fields           : Field_Vectors.Vector;\n   Type_Name        : Unbounded.Unbounded_String;\n   Is_Overlapping   : Boolean := False;\n   Overlap_Suffix   : Unbounded.Unbounded_String;\n   Type_Holder      : Register_Access := null;\n   Ada_Type         : Type_Holders.Holder;\n   Dim              : Positive := 1;\n   Dim_Increment    : Natural := 4;\n   Dim_Index        : Unbounded.Unbounded_String;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Register_Db",
       qualified_name: "Descriptors.Register.Register_Db",
       signature: "descriptors.register.register_db",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Register_Db is interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Register_Access",
       qualified_name: "Descriptors.Register.Register_Access",
       signature: "descriptors.register.register_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Register_Access is access all Register_T;",
       }   ,
   ]
,}
---
