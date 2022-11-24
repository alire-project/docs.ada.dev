---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Connection",
qualified_name: "Gnoga.Server.Connection",
signature: "gnoga.server.connection",
enclosing: "gnoga.server",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                   GNOGA - The GNU Omnificent GUI for Ada                 --\n                                                                          --\n                 G N O G A . S E R V E R . C O N N E C I O N              --\n                                                                          --\n                                 S p e c                                  --\n                                                                          --\n                                                                          --\n                     Copyright (C) 2014 David Botton                      --\n                                                                          --\n  This library is free software;  you can redistribute it and/or modify   --\n  it under terms of the  GNU General Public License  as published by the  --\n  Free Software  Foundation;  either version 3,  or (at your  option) any --\n  later version. This library is distributed in the hope that it will be  --\n  useful, but WITHOUT ANY WARRANTY;  without even the implied warranty of --\n  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    --\n                                                                          --\n  As a special exception under Section 7 of GPL version 3, you are        --\n  granted additional permissions described in the GCC Runtime Library     --\n  Exception, version 3.1, as published by the Free Software Foundation.   --\n                                                                          --\n  You should have received a copy of the GNU General Public License and   --\n  a copy of the GCC Runtime Library Exception along with this program;    --\n  see the files COPYING3 and COPYING.RUNTIME respectively.  If not, see   --\n  <http://www.gnu.org/licenses/>.                                         --\n                                                                          --\n  As a special exception, if other files instantiate generics from this   --\n  unit, or you link this unit with other files to produce an executable,  --\n  this  unit  does not  by itself cause  the resulting executable to be   --\n  covered by the GNU General Public License. This exception does not      --\n  however invalidate any other reasons why the executable file might be   --\n  covered by the  GNU Public License.                                     --\n                                                                          --\n  For more information please go to http://www.gnoga.com                  --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Gnoga_Connection_Type",
       qualified_name: "Gnoga.Server.Connection.Gnoga_Connection_Type",
       signature: "gnoga.server.connection.gnoga_connection_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Gnoga_Connection_Type is (HTTP, Long_Polling, WebSocket, None);",
       }   ,
   ]
,access_types:    [
       {
       name: "Connect_Event",
       qualified_name: "Gnoga.Server.Connection.Connect_Event",
       signature: "gnoga.server.connection.connect_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Connect_Event is access procedure\n  (ID         : in Gnoga.Types.Connection_ID;\n   Connection :    access Connection_Holder_Type);",
       }   ,
       {
       name: "Post_Event",
       qualified_name: "Gnoga.Server.Connection.Post_Event",
       signature: "gnoga.server.connection.post_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Post_Event is access procedure\n  (URI        : in     String;\n   Parameters : in out Gnoga.Types.Data_Map_Type);",
       }   ,
       {
       name: "Post_File_Event",
       qualified_name: "Gnoga.Server.Connection.Post_File_Event",
       signature: "gnoga.server.connection.post_file_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Post_File_Event is access procedure\n  (URI       : in String;\n   File_Name : in String;\n   Temp_Name : in String);",
       }   ,
       {
       name: "Post_Request_Event",
       qualified_name: "Gnoga.Server.Connection.Post_Request_Event",
       signature: "gnoga.server.connection.post_request_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Post_Request_Event is access procedure\n  (URI                 : in     String;\n   Accepted_Parameters :    out String);",
       }   ,
   ]
,}
---
