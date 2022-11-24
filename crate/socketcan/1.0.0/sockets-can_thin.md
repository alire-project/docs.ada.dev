---
crate: socketcan
layout: gnatdoc
gnatdoc: {
name: "Sockets.Can_Thin",
qualified_name: "Sockets.Can_Thin",
signature: "sockets.can_thin",
enclosing: "sockets",
is_private: false,
documentation: "kernel socket address structure redefined here for CAN",
documentation_snippet: "",
record_types:    [
       {
       name: "Can_Addr_Type",
       qualified_name: "Sockets.Can_Thin.Can_Addr_Type",
       signature: "sockets.can_thin.can_addr_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Can_Addr_Type is record\n   rx_id : aliased Can_Frame.Can_Id_Type;\n   tx_id : aliased Can_Frame.Can_Id_Type;\nend record;",
       }   ,
       {
       name: "Ifreq",
       qualified_name: "Sockets.Can_Thin.Ifreq",
       signature: "sockets.can_thin.ifreq",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Ifr_Name\n  Interface name, e.g. \"can0\"\n@field Ifr_Index\n  Interface index\n@field Unused\n  NOT USED",
       documentation_snippet: "type Ifreq is record\n   Ifr_Name  : Ifr_Name_Array;\n   Ifr_Index : Interfaces.C.Unsigned;\n   Unused    : Interfaces.C.Char_Array (1 .. 20);\nend record;",
       }   ,
       {
       name: "kernel_sockaddr_storage",
       qualified_name: "Sockets.Can_Thin.kernel_sockaddr_storage",
       signature: "sockets.can_thin.kernel_sockaddr_storage",
       enclosing: "",
       is_private: false,
       documentation: "\n@field ss_family\n  address family\n@field data\n  implementation-specific field",
       documentation_snippet: "type kernel_sockaddr_storage is record\n   ss_family : aliased Interfaces.C.unsigned_short;\n   data      : aliased data_array;\nend record;",
       }   ,
       {
       name: "sockaddr_can",
       qualified_name: "Sockets.Can_Thin.sockaddr_can",
       signature: "sockets.can_thin.sockaddr_can",
       enclosing: "",
       is_private: false,
       documentation: "\n@field can_family\n  address family number AF_CAN.\n@field can_ifindex\n  CAN network interface index.\n@field can_addr\n  protocol specific address information",
       documentation_snippet: "type sockaddr_can is record\n   can_family  : aliased Interfaces.C.Unsigned_Short;\n   can_ifindex : aliased Interfaces.C.Unsigned;\n   can_addr    : aliased Can_Addr_Type;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "data_array",
       qualified_name: "Sockets.Can_Thin.data_array",
       signature: "sockets.can_thin.data_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype data_array is Interfaces.C.char_array (0 .. 125);",
       }   ,
       {
       name: "Ifr_Name_Array",
       qualified_name: "Sockets.Can_Thin.Ifr_Name_Array",
       signature: "sockets.can_thin.ifr_name_array",
       enclosing: "",
       is_private: false,
       documentation: "struct ifreq is much more complicated than presented below.  It\nis a collection of unions used for various protocols.  Since we\nare limiting use of this structure to CANbus interfaces, we\nhave the liberty to declutter the unions and limit the\nrepresentation of the structure to just the CAN-specfic data\nitems.  Also, we will be only using the structure for finding\nthe interface by name.  Use this at your own risk!",
       documentation_snippet: "subtype Ifr_Name_Array is Interfaces.C.char_array (0 .. IFNAMSIZ - 1);",
       }   ,
   ]
,constants:    [
       {
       name: "IFNAMSIZ",
       qualified_name: "Sockets.Can_Thin.IFNAMSIZ",
       signature: "sockets.can_thin.ifnamsiz",
       enclosing: "",
       is_private: false,
       documentation: "struct ifreq is much more complicated than presented below.  It\nis a collection of unions used for various protocols.  Since we\nare limiting use of this structure to CANbus interfaces, we\nhave the liberty to declutter the unions and limit the\nrepresentation of the structure to just the CAN-specfic data\nitems.  Also, we will be only using the structure for finding\nthe interface by name.  Use this at your own risk!",
       documentation_snippet: "IFNAMSIZ : constant := 16;",
       }   ,
   ]
,}
---
