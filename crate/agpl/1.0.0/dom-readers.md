---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "DOM.Readers",
qualified_name: "DOM.Readers",
signature: "dom.readers",
enclosing: "dom",
is_private: false,
documentation: "---------------------------------------------------------------------\n                XML/Ada - An XML suite for Ada95                   --\n                                                                   --\n                       Copyright (C) 2001-2002                     --\n                            ACT-Europe                             --\n                                                                   --\n This library is free software; you can redistribute it and/or     --\n modify it under the terms of the GNU General Public               --\n License as published by the Free Software Foundation; either      --\n version 2 of the License, or (at your option) any later version.  --\n                                                                   --\n This library is distributed in the hope that it will be useful,   --\n but WITHOUT ANY WARRANTY; without even the implied warranty of    --\n MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU --\n General Public License for more details.                          --\n                                                                   --\n You should have received a copy of the GNU General Public         --\n License along with this library; if not, write to the             --\n Free Software Foundation, Inc., 59 Temple Place - Suite 330,      --\n Boston, MA 02111-1307, USA.                                       --\n                                                                   --\n As a special exception, if other files instantiate generics from  --\n this unit, or you link this unit with other files to produce an   --\n executable, this  unit  does not  by itself cause  the resulting  --\n executable to be covered by the GNU General Public License. This  --\n exception does not however invalidate any other reasons why the   --\n executable file  might be covered by the  GNU Public License.     --\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Tree_Reader",
       qualified_name: "DOM.Readers.Tree_Reader",
       signature: "dom.readers.tree_reader",
       enclosing: "",
       is_private: false,
       documentation: "Special SAX Reader that creates a DOM tree in its callbacks.\nNote that in case of a fatal error, it is your responsability to\nfree the tree, since it is left in the state it was when the error\nwas raised (for post-death analysis, if required).",
       documentation_snippet: "type Tree_Reader is new Reader with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Tree_Reader_Access",
       qualified_name: "DOM.Readers.Tree_Reader_Access",
       signature: "dom.readers.tree_reader_access",
       enclosing: "",
       is_private: false,
       documentation: "Special SAX Reader that creates a DOM tree in its callbacks.\nNote that in case of a fatal error, it is your responsability to\nfree the tree, since it is left in the state it was when the error\nwas raised (for post-death analysis, if required).",
       documentation_snippet: "type Tree_Reader_Access is access all Tree_Reader'Class;",
       }   ,
   ]
,}
---
