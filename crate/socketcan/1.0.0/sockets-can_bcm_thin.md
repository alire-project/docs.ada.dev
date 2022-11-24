---
crate: socketcan
layout: gnatdoc
gnatdoc: {
name: "Sockets.Can_Bcm_Thin",
qualified_name: "Sockets.Can_Bcm_Thin",
signature: "sockets.can_bcm_thin",
enclosing: "sockets",
is_private: false,
documentation: "Copyright (C) 2020 Glen Cornell <glen.m.cornell@gmail.com>\n\nThis program is free software: you can redistribute it and/or\nmodify it under the terms of the GNU General Public License as\npublished by the Free Software Foundation, either version 3 of the\nLicense, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU\nGeneral Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see\n<http://www.gnu.org/licenses/>.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Flag_Type",
       qualified_name: "Sockets.Can_Bcm_Thin.Flag_Type",
       signature: "sockets.can_bcm_thin.flag_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flag_Type is mod 2 ** 32;",
       }   ,
       {
       name: "Frame_Count_Type",
       qualified_name: "Sockets.Can_Bcm_Thin.Frame_Count_Type",
       signature: "sockets.can_bcm_thin.frame_count_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Frame_Count_Type is range 0..256;",
       }   ,
       {
       name: "Opcode_Type",
       qualified_name: "Sockets.Can_Bcm_Thin.Opcode_Type",
       signature: "sockets.can_bcm_thin.opcode_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum TX_SETUP\n  create (cyclic) transmission task\n@enum TX_DELETE\n  remove (cyclic) transmission task\n@enum TX_READ\n  read properties of (cyclic) transmission task\n@enum TX_SEND\n  send one CAN frame\n@enum RX_SETUP\n  create RX content filter subscription\n@enum RX_DELETE\n  remove RX content filter subscription\n@enum RX_READ\n  read properties of RX content filter subscription\n@enum TX_STATUS\n  reply to TX_READ request\n@enum TX_EXPIRED\n  notification on performed transmissions (count=0)\n@enum RX_STATUS\n  reply to RX_READ request\n@enum RX_TIMEOUT\n  cyclic message is absent\n@enum RX_CHANGED\n  updated CAN frame (detected content change)",
       documentation_snippet: "type Opcode_Type is\n  (TX_SETUP,\n   TX_DELETE,\n   TX_READ,\n   TX_SEND,\n   RX_SETUP,\n   RX_DELETE,\n   RX_READ,\n   TX_STATUS,\n   TX_EXPIRED,\n   RX_STATUS,\n   RX_TIMEOUT,\n   RX_CHANGED);",
       }   ,
   ]
,array_types:    [
       {
       name: "Frame_Array_Type",
       qualified_name: "Sockets.Can_Bcm_Thin.Frame_Array_Type",
       signature: "sockets.can_bcm_thin.frame_array_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Frame_Array_Type is array \n  (Frame_Count_Type range <>) of \n  aliased Sockets.Can_Frame.Can_Frame;",
       }   ,
   ]
,record_types:    [
       {
       name: "Bcm_Msg_Head",
       qualified_name: "Sockets.Can_Bcm_Thin.Bcm_Msg_Head",
       signature: "sockets.can_bcm_thin.bcm_msg_head",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Opcode\n  Opcode\n@field Flags\n  Special flags, see below.\n@field Count\n  number of frames to send before changing interval.\n@field Ival1\n  interval for the first \"count\" frames.\n@field Ival2\n  interval for the following frames.\n@field Can_Id\n  CAN ID of frames to be sent or received.\n@field Nframes\n  Number of frames to be sent or received.",
       documentation_snippet: "type Bcm_Msg_Head is record\n   Opcode  : aliased Opcode_Type;\n   Flags   : aliased Flag_Type;\n   Count   : aliased Frame_Count_Type;\n   Ival1   : aliased Timeval;\n   Ival2   : aliased Timeval;\n   Can_Id  : aliased Sockets.Can_Frame.Can_Id_Type;\n   Nframes : aliased Frame_Count_Type;\nend record;",
       }   ,
       {
       name: "Timeval",
       qualified_name: "Sockets.Can_Bcm_Thin.Timeval",
       signature: "sockets.can_bcm_thin.timeval",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Timeval is record\n   Tv_Sec  : aliased Interfaces.C.Long;\n   Tv_Usec : aliased Interfaces.C.Long;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "CAN_FD_FRAME",
       qualified_name: "Sockets.Can_Bcm_Thin.CAN_FD_FRAME",
       signature: "sockets.can_bcm_thin.can_fd_frame",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CAN_FD_FRAME       : constant Flag_Type := 16#00000800#;",
       }   ,
       {
       name: "RX_ANNOUNCE_RESUME",
       qualified_name: "Sockets.Can_Bcm_Thin.RX_ANNOUNCE_RESUME",
       signature: "sockets.can_bcm_thin.rx_announce_resume",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RX_ANNOUNCE_RESUME : constant Flag_Type := 16#00000100#;",
       }   ,
       {
       name: "RX_CHECK_DLC",
       qualified_name: "Sockets.Can_Bcm_Thin.RX_CHECK_DLC",
       signature: "sockets.can_bcm_thin.rx_check_dlc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RX_CHECK_DLC       : constant Flag_Type := 16#00000040#;",
       }   ,
       {
       name: "RX_FILTER_ID",
       qualified_name: "Sockets.Can_Bcm_Thin.RX_FILTER_ID",
       signature: "sockets.can_bcm_thin.rx_filter_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RX_FILTER_ID       : constant Flag_Type := 16#00000020#;",
       }   ,
       {
       name: "RX_NO_AUTOTIMER",
       qualified_name: "Sockets.Can_Bcm_Thin.RX_NO_AUTOTIMER",
       signature: "sockets.can_bcm_thin.rx_no_autotimer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RX_NO_AUTOTIMER    : constant Flag_Type := 16#00000080#;",
       }   ,
       {
       name: "RX_RTR_FRAME",
       qualified_name: "Sockets.Can_Bcm_Thin.RX_RTR_FRAME",
       signature: "sockets.can_bcm_thin.rx_rtr_frame",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RX_RTR_FRAME       : constant Flag_Type := 16#00000400#;",
       }   ,
       {
       name: "SETTIMER",
       qualified_name: "Sockets.Can_Bcm_Thin.SETTIMER",
       signature: "sockets.can_bcm_thin.settimer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SETTIMER           : constant Flag_Type := 16#00000001#;",
       }   ,
       {
       name: "STARTTIMER",
       qualified_name: "Sockets.Can_Bcm_Thin.STARTTIMER",
       signature: "sockets.can_bcm_thin.starttimer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "STARTTIMER         : constant Flag_Type := 16#00000002#;",
       }   ,
       {
       name: "TX_ANNOUNCE",
       qualified_name: "Sockets.Can_Bcm_Thin.TX_ANNOUNCE",
       signature: "sockets.can_bcm_thin.tx_announce",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TX_ANNOUNCE        : constant Flag_Type := 16#00000008#;",
       }   ,
       {
       name: "TX_COUNTEVT",
       qualified_name: "Sockets.Can_Bcm_Thin.TX_COUNTEVT",
       signature: "sockets.can_bcm_thin.tx_countevt",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TX_COUNTEVT        : constant Flag_Type := 16#00000004#;",
       }   ,
       {
       name: "TX_CP_CAN_ID",
       qualified_name: "Sockets.Can_Bcm_Thin.TX_CP_CAN_ID",
       signature: "sockets.can_bcm_thin.tx_cp_can_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TX_CP_CAN_ID       : constant Flag_Type := 16#00000010#;",
       }   ,
       {
       name: "TX_RESET_MULTI_IDX",
       qualified_name: "Sockets.Can_Bcm_Thin.TX_RESET_MULTI_IDX",
       signature: "sockets.can_bcm_thin.tx_reset_multi_idx",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TX_RESET_MULTI_IDX : constant Flag_Type := 16#00000200#;",
       }   ,
   ]
,}
---