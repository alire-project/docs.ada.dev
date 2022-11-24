---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Memory_Streams",
qualified_name: "SAL.Memory_Streams",
signature: "sal.memory_streams",
enclosing: "sal",
is_private: false,
documentation: "Abstract:\n\nA memory stream type, for reading objects from some communication\nchannel.\n\nCopyright (C) 2005, 2009, 2018 Stephen Leake.  All Rights Reserved.\n\nThis library is free software; you can redistribute it and/or\nmodify it under terms of the GNU General Public License as\npublished by the Free Software Foundation; either version 3, or (at\nyour option) any later version. This library is distributed in the\nhope that it will be useful, but WITHOUT ANY WARRANTY; without even\nthe implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR\nPURPOSE. See the GNU General Public License for more details. You\nshould have received a copy of the GNU General Public License\ndistributed with this program; see file COPYING. If not, write to\nthe Free Software Foundation, 59 Temple Place - Suite 330, Boston,\nMA 02111-1307, USA.\n\nAs a special exception, if other files instantiate generics from\nthis unit, or you link this unit with other files to produce an\nexecutable, this  unit  does not  by itself cause  the resulting\nexecutable to be covered by the GNU General Public License. This\nexception does not however invalidate any other reasons why the\nexecutable file  might be covered by the  GNU Public License.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Stream_Type",
       qualified_name: "SAL.Memory_Streams.Stream_Type",
       signature: "sal.memory_streams.stream_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stream_Type (Max_Length : Ada.Streams.Stream_Element_Count) is\n  new Ada.Streams.Root_Stream_Type with private;",
       }   ,
   ]
,}
---
