---
crate: templates_parser
layout: gnatdoc
gnatdoc: {
name: "Templates_Parser.Utils",
qualified_name: "Templates_Parser.Utils",
signature: "templates_parser.utils",
enclosing: "templates_parser",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                             Templates Parser                             --\n                                                                          --\n                     Copyright (C) 2004-2014, AdaCore                     --\n                                                                          --\n  This library is free software;  you can redistribute it and/or modify   --\n  it under terms of the  GNU General Public License  as published by the  --\n  Free Software  Foundation;  either version 3,  or (at your  option) any --\n  later version. This library is distributed in the hope that it will be  --\n  useful, but WITHOUT ANY WARRANTY;  without even the implied warranty of --\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    --\n                                                                          --\n  As a special exception under Section 7 of GPL version 3, you are        --\n  granted additional permissions described in the GCC Runtime Library     --\n  Exception, version 3.1, as published by the Free Software Foundation.   --\n                                                                          --\n  You should have received a copy of the GNU General Public License and   --\n  a copy of the GCC Runtime Library Exception along with this program;    --\n  see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see   --\n  <http://www.gnu.org/licenses/>.                                         --\n                                                                          --\n  As a special exception, if other files instantiate generics from this   --\n  unit, or you link this unit with other files to produce an executable,  --\n  this  unit  does not  by itself cause  the resulting executable to be   --\n  covered by the GNU General Public License. This exception does not      --\n  however invalidate any other reasons why the executable file  might be  --\n  covered by the  GNU Public License.                                     --\n----------------------------------------------------------------------------",
documentation_snippet: "",
constants:    [
       {
       name: "BOM_Utf8",
       qualified_name: "Templates_Parser.Utils.BOM_Utf8",
       signature: "templates_parser.utils.bom_utf8",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "BOM_Utf8 : constant String :=\n             Character'Val (16#EF#)\n             & Character'Val (16#BB#)\n             & Character'Val (16#BF#);",
       }   ,
       {
       name: "Directory_Separator",
       qualified_name: "Templates_Parser.Utils.Directory_Separator",
       signature: "templates_parser.utils.directory_separator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Directory_Separator : constant Character;",
       }   ,
       {
       name: "Is_Windows",
       qualified_name: "Templates_Parser.Utils.Is_Windows",
       signature: "templates_parser.utils.is_windows",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Is_Windows          : constant Boolean :=\n                        Environment_Variables.Exists (\"OS\") and then\n                        Environment_Variables.Value (\"OS\") = \"Windows_NT\";",
       }   ,
       {
       name: "Path_Separator",
       qualified_name: "Templates_Parser.Utils.Path_Separator",
       signature: "templates_parser.utils.path_separator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Path_Separator      : constant Character;",
       }   ,
   ]
,}
---
