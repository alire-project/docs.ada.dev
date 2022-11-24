---
crate: svd2ada
layout: gnatdoc
gnatdoc: {
name: "Descriptors.Cluster",
qualified_name: "Descriptors.Cluster",
signature: "descriptors.cluster",
enclosing: "descriptors",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                          SVD Binding Generator                           --\n                                                                          --\n                    Copyright (C) 2015-2019, AdaCore                      --\n                                                                          --\n SVD2Ada is free software;  you can  redistribute it  and/or modify it    --\n under terms of the  GNU General Public License as published  by the Free --\n Software  Foundation;  either version 3,  or (at your option) any later  --\n version.  SVD2Ada is distributed in the hope that it will be useful, but --\n WITHOUT ANY WARRANTY;  without even the  implied warranty of MERCHANTA-  --\n BILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  --\n License for  more details.  You should have  received  a copy of the GNU --\n General Public License  distributed with SVD2Ada; see file COPYING3.  If --\n not, go to http://www.gnu.org/licenses for a complete copy of the        --\n license.                                                                 --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Peripheral_Element_Type",
       qualified_name: "Descriptors.Cluster.Peripheral_Element_Type",
       signature: "descriptors.cluster.peripheral_element_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Peripheral_Element_Type is (Register_Element, Cluster_Element);",
       }   ,
   ]
,record_types:    [
       {
       name: "Peripheral_Element",
       qualified_name: "Descriptors.Cluster.Peripheral_Element",
       signature: "descriptors.cluster.peripheral_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Peripheral_Element (Kind : Peripheral_Element_Type := Register_Element)\nis record\n   case Kind is\n      when Register_Element =>\n         Reg     : Register_Access;\n      when Cluster_Element =>\n         Cluster : Cluster_Access;\n   end case;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Cluster_Db",
       qualified_name: "Descriptors.Cluster.Cluster_Db",
       signature: "descriptors.cluster.cluster_db",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cluster_Db is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Cluster_T",
       qualified_name: "Descriptors.Cluster.Cluster_T",
       signature: "descriptors.cluster.cluster_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cluster_T is new Register_Db and Cluster_Db with record\n   Name            : Unbounded_String;\n   Xml_Id          : Unbounded_String;\n   Type_Name       : Unbounded_String;\n   Type_Holder     : Cluster_Access := null;\n   Ada_Type        : Type_Holders.Holder;\n   Description     : Unbounded_String;\n   Is_Overlapping   : Boolean := False;\n   Overlap_Suffix   : Unbounded_String;\n   Address_Offset  : Natural;\n   Reg_Properties  : Register_Properties_T := Null_Register_Property;\n   Dim             : Positive := 1;\n   Dim_Increment   : Natural := 4;\n   Dim_Index       : Unbounded_String;\n   Content         : Peripheral_Element_Vectors.Vector;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Cluster_Access",
       qualified_name: "Descriptors.Cluster.Cluster_Access",
       signature: "descriptors.cluster.cluster_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cluster_Access is access all Cluster_T;",
       }   ,
   ]
,}
---
