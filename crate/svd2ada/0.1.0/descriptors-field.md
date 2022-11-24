---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Field",
qualified_name: "Descriptors.Field",
signature: "descriptors.field",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2020, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Field_T",
       qualified_name: "Descriptors.Field.Field_T",
       signature: "descriptors.field.field_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Field_T is record\n   Name             : Unbounded.Unbounded_String;\n   Description      : Unbounded.Unbounded_String;\n   LSB              : Natural;\n   Size             : Natural;\n   Acc              : Access_Type;\n   Mod_Write_Values : Modified_Write_Values_Type := Modify;\n   Read_Action      : Read_Action_Type := Undefined_Read_Action;\n   Enums            : Descriptors.Enumerate.Enumerate_Vectors.Vector;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Field",
       qualified_name: "Descriptors.Field.Null_Field",
       signature: "descriptors.field.null_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Field : constant Field_T :=\n               (Unbounded.Null_Unbounded_String,\n                Unbounded.Null_Unbounded_String,\n                0,\n                0,\n                Read_Write,\n                others => <>);",
       }   ,
   ]
,}
---
