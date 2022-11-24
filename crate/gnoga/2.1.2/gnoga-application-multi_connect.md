---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Application.Multi_Connect",
qualified_name: "Gnoga.Application.Multi_Connect",
signature: "gnoga.application.multi_connect",
enclosing: "gnoga.application",
is_private: false,
documentation: "This package allows for the creation of GUI applications with multiple\nconnections to the same app.",
documentation_snippet: "",
access_types:    [
       {
       name: "Application_Connect_Event",
       qualified_name: "Gnoga.Application.Multi_Connect.Application_Connect_Event",
       signature: "gnoga.application.multi_connect.application_connect_event",
       enclosing: "",
       is_private: false,
       documentation: "On each connection an Application_Connect_Event registered in\nOn_Connect_Handler will be called. Main_Window will be attached\nto the window of the browser. Connection can optionally be used\nto allow for \"clean up\" upon close of connection, or to prevent\nfinalization of the called Application_Connect_Event procedure\nuntil the connection is closed. This allows for Gnoga objects to\nbe created on the stack within the procedure and not be finalized\nprematurely and still able to respond to events, etc.\nUse: Connection.Hold;\n\n@param Main_Window\n@param Connection",
       documentation_snippet: "type Application_Connect_Event is access procedure\n  (Main_Window : in out Gnoga.Gui.Window.Window_Type'Class;\n   Connection  :        access Connection_Holder_Type);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Connection_Holder_Type",
       qualified_name: "Gnoga.Application.Multi_Connect.Connection_Holder_Type",
       signature: "gnoga.application.multi_connect.connection_holder_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Connection_Holder_Type is Gnoga.Server.Connection.Connection_Holder_Type;",
       }   ,
   ]
,}
---
