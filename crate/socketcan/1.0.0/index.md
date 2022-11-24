---
crate: socketcan
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Sockets",
    qualified_name: "Sockets",
    signature: "sockets",
    enclosing: "",
    is_private: false,
    documentation: "Copyright (C) 2020 Glen Cornell <glen.m.cornell@gmail.com>\n\nThis program is free software: you can redistribute it and/or\nmodify it under the terms of the GNU General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see\n<http://www.gnu.org/licenses/>.",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Can",
    qualified_name: "Sockets.Can",
    signature: "sockets.can",
    enclosing: "sockets",
    is_private: false,
    documentation: "SETUP:\n\nThe Linux kernel must be compiled with support for SocketCAN\n(\"can\" and \"can_raw\" modules) with a driver for your specific CAN\ncontroller interface.  There is a virtual CAN driver for testing\npurposes which can be loaded and created in Linux with the\ncommands below.\n\n$ modprobe can\n$ modprobe can_raw\n$ modprobe vcan\n$ sudo ip link add dev vcan0 type vcan\n$ sudo ip link set up vcan0\n$ ip link show vcan0\n3: vcan0: <NOARP,UP,LOWER_UP> mtu 16 qdisc noqueue state UNKNOWN \n    link/can\n\nEXAMPLES:\n\nThe following code snippet is a working example of the SocketCAN\nAPI that sends a packet using the raw interface. It is based on\nthe notes documented in the Linux Kernel.\n\nwith Gnat.Sockets;\nwith Sockets.Can;\nwith Sockets.Can_Frame;\nprocedure Socketcan_Test is\n   Socket       : Sockets.Can.Socket_Type;\n   Address      : Sockets.Can.Sock_Addr_Type;\n   Frame        : Sockets.Can_Frame.Can_Frame;\nbegin\n   Sockets.Can.Create_Socket(Socket);\n   Address.If_Index := Sockets.Can.If_Name_To_Index(\"vcan0\");\n   Sockets.Can.Bind_Socket(Socket, Address);\n   frame.can_id  := 16#123#;\n   frame.can_dlc := 2;\n   frame.Data(0) := 16#11#;\n   frame.Data(1) := 16#22#;\n   Sockets.Can.Send_Socket(Socket, Frame);\nend Socketcan_Test;\n\nThe packet can be analyzed on the vcan0 interface using the\ncandump utility which is part of the SocketCAN can-utils package.\nOn another shell, type the following command to view the output of\nthe program ablve.\n\n$ candump vcan0\n  vcan0  123  [2] 11 22",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Can.Broadcast_Manager",
    qualified_name: "Sockets.Can.Broadcast_Manager",
    signature: "sockets.can.broadcast_manager",
    enclosing: "sockets.can",
    is_private: false,
    documentation: "Copyright (C) 2020 Glen Cornell <glen.m.cornell@gmail.com>\n\nThis program is free software: you can redistribute it and/or\nmodify it under the terms of the GNU General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see\n<http://www.gnu.org/licenses/>.",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Can_Bcm_Thin",
    qualified_name: "Sockets.Can_Bcm_Thin",
    signature: "sockets.can_bcm_thin",
    enclosing: "sockets",
    is_private: false,
    documentation: "Copyright (C) 2020 Glen Cornell <glen.m.cornell@gmail.com>\n\nThis program is free software: you can redistribute it and/or\nmodify it under the terms of the GNU General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see\n<http://www.gnu.org/licenses/>.",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Can_Frame",
    qualified_name: "Sockets.Can_Frame",
    signature: "sockets.can_frame",
    enclosing: "sockets",
    is_private: false,
    documentation: "Copyright (C) 2020 Glen Cornell <glen.m.cornell@gmail.com>\n\nThis program is free software: you can redistribute it and/or\nmodify it under the terms of the GNU General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see\n<http://www.gnu.org/licenses/>.",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Can_Thin",
    qualified_name: "Sockets.Can_Thin",
    signature: "sockets.can_thin",
    enclosing: "sockets",
    is_private: false,
    documentation: "kernel socket address structure redefined here for CAN",
    documentation_snippet: "",
    },
    {
    name: "Sockets.Os_Constants",
    qualified_name: "Sockets.Os_Constants",
    signature: "sockets.os_constants",
    enclosing: "sockets",
    is_private: false,
    documentation: "special address description flags for the CAN_ID",
    documentation_snippet: "",
    },
]
}
---
