---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.DSI",
qualified_name: "HAL.DSI",
signature: "hal.dsi",
enclosing: "hal",
is_private: false,
documentation: "Display Serial Interface",
documentation_snippet: "",
simple_types:    [
       {
       name: "DSI_Pkt_Data_Type",
       qualified_name: "HAL.DSI.DSI_Pkt_Data_Type",
       signature: "hal.dsi.dsi_pkt_data_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum DCS_Short_Pkt_Write_P0\n  DCS Short write, no parameter\n@enum DCS_Short_Pkt_Write_P1\n  DCS Short write, one parameter\n@enum Gen_Short_Pkt_Write_P0\n  Generic Short write, no parameter\n@enum Gen_Short_Pkt_Write_P1\n  Generic Short write, one parameter\n@enum Gen_Short_Pkt_Write_P2\n  Generic Short write, two parameters\n@enum DCS_Long_Pkt_Write\n  DCS Long write\n@enum Gen_Long_Pkt_Write\n  Generic Long write\n@enum DCS_Short_Pkt_Read\n  DCS Short read\n@enum Gen_Short_Pkg_Read_P0\n  Gen read, no parameter\n@enum Gen_Short_Pkg_Read_P1\n  Gen read, one parameter\n@enum Gen_Short_Pkg_Read_P2\n  Gen read, two parameter",
       documentation_snippet: "type DSI_Pkt_Data_Type is\n  (DCS_Short_Pkt_Write_P0,\n   DCS_Short_Pkt_Write_P1,\n   Gen_Short_Pkt_Write_P0,\n   Gen_Short_Pkt_Write_P1,\n   Gen_Short_Pkt_Write_P2,\n   DCS_Long_Pkt_Write,\n   Gen_Long_Pkt_Write,\n   DCS_Short_Pkt_Read,\n   Gen_Short_Pkg_Read_P0,\n   Gen_Short_Pkg_Read_P1,\n   Gen_Short_Pkg_Read_P2);",
       }   ,
   ]
,array_types:    [
       {
       name: "DSI_Data",
       qualified_name: "HAL.DSI.DSI_Data",
       signature: "hal.dsi.dsi_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DSI_Data is array (Positive range <>) of UInt8;",
       }   ,
   ]
,interface_types:    [
       {
       name: "DSI_Port",
       qualified_name: "HAL.DSI.DSI_Port",
       signature: "hal.dsi.dsi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DSI_Port is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_DSI_Port",
       qualified_name: "HAL.DSI.Any_DSI_Port",
       signature: "hal.dsi.any_dsi_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_DSI_Port is access all DSI_Port'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "DSI_Long_Write_Packet_Data_Type",
       qualified_name: "HAL.DSI.DSI_Long_Write_Packet_Data_Type",
       signature: "hal.dsi.dsi_long_write_packet_data_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DSI_Long_Write_Packet_Data_Type is DSI_Pkt_Data_Type range\n  DCS_Long_Pkt_Write .. Gen_Long_Pkt_Write;",
       }   ,
       {
       name: "DSI_Short_Write_Packet_Data_Type",
       qualified_name: "HAL.DSI.DSI_Short_Write_Packet_Data_Type",
       signature: "hal.dsi.dsi_short_write_packet_data_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DSI_Short_Write_Packet_Data_Type is DSI_Pkt_Data_Type range\n  DCS_Short_Pkt_Write_P0 .. Gen_Short_Pkt_Write_P2;",
       }   ,
       {
       name: "DSI_Virtual_Channel_ID",
       qualified_name: "HAL.DSI.DSI_Virtual_Channel_ID",
       signature: "hal.dsi.dsi_virtual_channel_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DSI_Virtual_Channel_ID is UInt2;",
       }   ,
   ]
,}
---
