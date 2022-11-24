---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Network.SocketStatus",
qualified_name: "Sf.Network.SocketStatus",
signature: "sf.network.socketstatus",
enclosing: "sf.network",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n//////////////////////////////////////////////////////////\n/ @brief Define the status that can be returned by the socket functions\n/\n//////////////////////////////////////////////////////////\n/< The socket has sent / received the data\n/< The socket is not ready to send / receive data yet\n/< The socket sent a part of the data\n/< The TCP socket has been disconnected\n/< An unexpected error happened",
documentation_snippet: "",
simple_types:    [
       {
       name: "sfSocketStatus",
       qualified_name: "Sf.Network.SocketStatus.sfSocketStatus",
       signature: "sf.network.socketstatus.sfsocketstatus",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSocketStatus is \n  (sfSocketDone,\n   sfSocketNotReady,\n   sfSocketPartial,\n   sfSocketDisconnected,\n   sfSocketError);",
       }   ,
   ]
,}
---
