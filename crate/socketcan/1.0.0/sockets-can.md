---
crate: socketcan
layout: gnatdoc
gnatdoc: {
name: "Sockets.Can",
qualified_name: "Sockets.Can",
signature: "sockets.can",
enclosing: "sockets",
is_private: false,
documentation: "SETUP:\n\nThe Linux kernel must be compiled with support for SocketCAN\n(\"can\" and \"can_raw\" modules) with a driver for your specific CAN\ncontroller interface.  There is a virtual CAN driver for testing\npurposes which can be loaded and created in Linux with the\ncommands below.\n\n$ modprobe can\n$ modprobe can_raw\n$ modprobe vcan\n$ sudo ip link add dev vcan0 type vcan\n$ sudo ip link set up vcan0\n$ ip link show vcan0\n3: vcan0: <NOARP,UP,LOWER_UP> mtu 16 qdisc noqueue state UNKNOWN \n    link/can\n\nEXAMPLES:\n\nThe following code snippet is a working example of the SocketCAN\nAPI that sends a packet using the raw interface. It is based on\nthe notes documented in the Linux Kernel.\n\nwith Gnat.Sockets;\nwith Sockets.Can;\nwith Sockets.Can_Frame;\nprocedure Socketcan_Test is\n   Socket       : Sockets.Can.Socket_Type;\n   Address      : Sockets.Can.Sock_Addr_Type;\n   Frame        : Sockets.Can_Frame.Can_Frame;\nbegin\n   Sockets.Can.Create_Socket(Socket);\n   Address.If_Index := Sockets.Can.If_Name_To_Index(\"vcan0\");\n   Sockets.Can.Bind_Socket(Socket, Address);\n   frame.can_id  := 16#123#;\n   frame.can_dlc := 2;\n   frame.Data(0) := 16#11#;\n   frame.Data(1) := 16#22#;\n   Sockets.Can.Send_Socket(Socket, Frame);\nend Socketcan_Test;\n\nThe packet can be analyzed on the vcan0 interface using the\ncandump utility which is part of the SocketCAN can-utils package.\nOn another shell, type the following command to view the output of\nthe program ablve.\n\n$ candump vcan0\n  vcan0  123  [2] 11 22",
documentation_snippet: "",
simple_types:    [
       {
       name: "Family_Type",
       qualified_name: "Sockets.Can.Family_Type",
       signature: "sockets.can.family_type",
       enclosing: "",
       is_private: false,
       documentation: "Address family (or protocol family) identifies the\ncommunication domain and groups protocols with similar address\nformats.  This is represented as the \"domain\" parameter in the\nsocket(2) man page.\n\n@enum Family_Can",
       documentation_snippet: "type Family_Type is (Family_Can);",
       }   ,
       {
       name: "Mode_Type",
       qualified_name: "Sockets.Can.Mode_Type",
       signature: "sockets.can.mode_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mode_Type is (Socket_Dgram, Socket_Raw);",
       }   ,
       {
       name: "Protocol_Type",
       qualified_name: "Sockets.Can.Protocol_Type",
       signature: "sockets.can.protocol_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Protocol_Type is (Can_Raw, Can_Bcm);",
       }   ,
   ]
,array_types:    [
       {
       name: "Can_Filter_Array_Type",
       qualified_name: "Sockets.Can.Can_Filter_Array_Type",
       signature: "sockets.can.can_filter_array_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Can_Filter_Array_Type is array (Positive range <>) of Can_Filter;",
       }   ,
   ]
,record_types:    [
       {
       name: "Can_Filter",
       qualified_name: "Sockets.Can.Can_Filter",
       signature: "sockets.can.can_filter",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Can_Id\n  relevant bits of CAN ID which are not masked out.\n@field Can_Mask\n  CAN mask (see description)",
       documentation_snippet: "type Can_Filter is record\n   Can_Id   : aliased Can_Frame.Can_Id_Type;\n   Can_Mask : aliased Can_Frame.Can_Id_Type;\nend record;",
       }   ,
       {
       name: "Sock_Addr_Type",
       qualified_name: "Sockets.Can.Sock_Addr_Type",
       signature: "sockets.can.sock_addr_type",
       enclosing: "",
       is_private: false,
       documentation: "Socket addresses fully define a socket connection with protocol family,\nan Internet address and a port.\n\n@field Family\n@field If_Index",
       documentation_snippet: "   type Sock_Addr_Type (Family : Family_Type := Family_Can) is record\n      case Family is\n	 when Family_Can =>\n	    If_Index : Natural := 0;\n      end case;\n   end record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Can_Stream",
       qualified_name: "Sockets.Can.Can_Stream",
       signature: "sockets.can.can_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Can_Stream is new Ada.Streams.Root_Stream_Type with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Request_Flag_Type",
       qualified_name: "Sockets.Can.Request_Flag_Type",
       signature: "sockets.can.request_flag_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Request_Flag_Type is Gnat.Sockets.Request_Flag_Type;",
       }   ,
       {
       name: "Socket_Type",
       qualified_name: "Sockets.Can.Socket_Type",
       signature: "sockets.can.socket_type",
       enclosing: "",
       is_private: false,
       documentation: "Sockets are used to implement a reliable bi-directional\npoint-to-point, datagram-based connection between\nhosts.",
       documentation_snippet: "subtype Socket_Type is Gnat.Sockets.Socket_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Request_Flag",
       qualified_name: "Sockets.Can.No_Request_Flag",
       signature: "sockets.can.no_request_flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Request_Flag : constant Request_Flag_Type := Gnat.Sockets.No_Request_Flag;",
       }   ,
   ]
,}
---
