---
crate: startup_gen
layout: gnatdoc
gnatdoc: {
name: "Setup",
qualified_name: "Setup",
signature: "setup",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                               startup-gen                                --\n                                                                          --\n                        Copyright (C) 2019, AdaCore                       --\n                                                                          --\n This is  free  software;  you can redistribute it and/or modify it under --\n terms of the  GNU  General Public License as published by the Free Soft- --\n ware  Foundation;  either version 3,  or (at your option) any later ver- --\n sion.  This software is distributed in the hope  that it will be useful, --\n but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN- --\n TABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public --\n License for more details.  You should have received  a copy of the  GNU  --\n General Public License distributed with GNAT; see file  COPYING. If not, --\n see <http://www.gnu.org/licenses/>.                                      --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Command_Line_Values",
       qualified_name: "Setup.Command_Line_Values",
       signature: "setup.command_line_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Command_Line_Values is tagged record\n   Project_File      : aliased String_Access := null;\n   Linker_File       : aliased String_Access := null;\n   Startup_Code_File : aliased String_Access := null;\n   Print_Tags        : aliased Boolean       := False;\nend record;",
       }   ,
   ]
,}
---
