---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Names",
qualified_name: "GPR.Names",
signature: "gpr.names",
enclosing: "gpr",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                           GPR PROJECT MANAGER                            --\n                                                                          --\n          Copyright (C) 2001-2021, Free Software Foundation, Inc.         --\n                                                                          --\n This library is free software;  you can redistribute it and/or modify it --\n under terms of the  GNU General Public License  as published by the Free --\n Software  Foundation;  either version 3,  or (at your  option) any later --\n version. This library is distributed in the hope that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE.                            --\n                                                                          --\n As a special exception under Section 7 of GPL version 3, you are granted --\n additional permissions described in the GCC Runtime Library Exception,   --\n version 3.1, as published by the Free Software Foundation.               --\n                                                                          --\n You should have received a copy of the GNU General Public License and    --\n a copy of the GCC Runtime Library Exception along with this program;     --\n see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see    --\n <http://www.gnu.org/licenses/>.                                          --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Casing_Type",
       qualified_name: "GPR.Names.Casing_Type",
       signature: "gpr.names.casing_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum All_Upper_Case\n  All letters are upper case\n@enum All_Lower_Case\n  All letters are lower case\n@enum Mixed_Case\n  The initial letter, and any letters after underlines are upper case.\n  All other letters are lower case\n@enum Unknown",
       documentation_snippet: "type Casing_Type is\n  (All_Upper_Case,\n   All_Lower_Case,\n   Mixed_Case,\n   Unknown\n  );",
       }   ,
       {
       name: "Char_Code_Base",
       qualified_name: "GPR.Names.Char_Code_Base",
       signature: "gpr.names.char_code_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Char_Code_Base is mod 2 ** 32;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Char_Code",
       qualified_name: "GPR.Names.Char_Code",
       signature: "gpr.names.char_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Char_Code is Char_Code_Base range 0 .. 16#7FFF_FFFF#;",
       }   ,
       {
       name: "Known_Casing",
       qualified_name: "GPR.Names.Known_Casing",
       signature: "gpr.names.known_casing",
       enclosing: "",
       is_private: false,
       documentation: "Exclude Unknown casing",
       documentation_snippet: "subtype Known_Casing is Casing_Type range All_Upper_Case .. Mixed_Case;",
       }   ,
   ]
,variables:    [
       {
       name: "Name_Buffer",
       qualified_name: "GPR.Names.Name_Buffer",
       signature: "gpr.names.name_buffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Name_Buffer : String (1 .. 1_000_000);",
       }   ,
       {
       name: "Name_Len",
       qualified_name: "GPR.Names.Name_Len",
       signature: "gpr.names.name_len",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Name_Len    : Natural := 0;",
       }   ,
   ]
,}
---
