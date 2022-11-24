---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Enumerate",
qualified_name: "Descriptors.Enumerate",
signature: "descriptors.enumerate",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2016, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Enumerate_T",
       qualified_name: "Descriptors.Enumerate.Enumerate_T",
       signature: "descriptors.enumerate.enumerate_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Enumerate_T is record\n   Name   : Unbounded.Unbounded_String;\n   Values : Enumerate_Values_Vectors.Vector;\n   Usage  : Enum_Usage_Type := Read_Write;\nend record;",
       }   ,
       {
       name: "Enumerate_Value",
       qualified_name: "Descriptors.Enumerate.Enumerate_Value",
       signature: "descriptors.enumerate.enumerate_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Enumerate_Value is record\n   Name      : Unbounded.Unbounded_String;\n   Descr     : Unbounded.Unbounded_String;\n   Value     : Unsigned;\n   IsDefault : Boolean := False;\nend record;",
       }   ,
   ]
,}
---
