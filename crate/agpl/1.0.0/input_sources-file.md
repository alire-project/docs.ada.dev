---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Input_Sources.File",
qualified_name: "Input_Sources.File",
signature: "input_sources.file",
enclosing: "input_sources",
is_private: false,
documentation: "---------------------------------------------------------------------\n                XML/Ada - An XML suite for Ada95                   --\n                                                                   --\n                       Copyright (C) 2001-2002                     --\n                            ACT-Europe                             --\n                                                                   --\n This library is free software; you can redistribute it and/or     --\n modify it under the terms of the GNU General Public               --\n License as published by the Free Software Foundation; either      --\n version 2 of the License, or (at your option) any later version.  --\n                                                                   --\n This library is distributed in the hope that it will be useful,   --\n but WITHOUT ANY WARRANTY; without even the implied warranty of    --\n MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU --\n General Public License for more details.                          --\n                                                                   --\n You should have received a copy of the GNU General Public         --\n License along with this library; if not, write to the             --\n Free Software Foundation, Inc., 59 Temple Place - Suite 330,      --\n Boston, MA 02111-1307, USA.                                       --\n                                                                   --\n As a special exception, if other files instantiate generics from  --\n this unit, or you link this unit with other files to produce an   --\n executable, this  unit  does not  by itself cause  the resulting  --\n executable to be covered by the GNU General Public License. This  --\n exception does not however invalidate any other reasons why the   --\n executable file  might be covered by the  GNU Public License.     --\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "File_Input",
       qualified_name: "Input_Sources.File.File_Input",
       signature: "input_sources.file.file_input",
       enclosing: "",
       is_private: false,
       documentation: "A special implementation of a reader, that reads from a file.",
       documentation_snippet: "type File_Input is new Input_Source with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "File_Input_Access",
       qualified_name: "Input_Sources.File.File_Input_Access",
       signature: "input_sources.file.file_input_access",
       enclosing: "",
       is_private: false,
       documentation: "A special implementation of a reader, that reads from a file.",
       documentation_snippet: "type File_Input_Access is access all File_Input'Class;",
       }   ,
   ]
,}
---
