---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.XIP_CTRL",
qualified_name: "RP2040_SVD.XIP_CTRL",
signature: "rp2040_svd.xip_ctrl",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CTRL_Register",
       qualified_name: "RP2040_SVD.XIP_CTRL.CTRL_Register",
       signature: "rp2040_svd.xip_ctrl.ctrl_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_Register is record\n   EN            : Boolean := True;\n   ERR_BADWRITE  : Boolean := True;\n   Reserved_2_2  : HAL.Bit := 16#0#;\n   POWER_DOWN    : Boolean := False;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "FLUSH_Register",
       qualified_name: "RP2040_SVD.XIP_CTRL.FLUSH_Register",
       signature: "rp2040_svd.xip_ctrl.flush_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FLUSH_Register is record\n   FLUSH         : Boolean := False;\n   Reserved_1_31 : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "STAT_Register",
       qualified_name: "RP2040_SVD.XIP_CTRL.STAT_Register",
       signature: "rp2040_svd.xip_ctrl.stat_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STAT_Register is record\n   FLUSH_READY   : Boolean;\n   FIFO_EMPTY    : Boolean;\n   FIFO_FULL     : Boolean;\n   Reserved_3_31 : HAL.UInt29;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "STREAM_ADDR_Register",
       qualified_name: "RP2040_SVD.XIP_CTRL.STREAM_ADDR_Register",
       signature: "rp2040_svd.xip_ctrl.stream_addr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STREAM_ADDR_Register is record\n   Reserved_0_1 : HAL.UInt2 := 16#0#;\n   STREAM_ADDR  : STREAM_ADDR_STREAM_ADDR_Field := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "STREAM_CTR_Register",
       qualified_name: "RP2040_SVD.XIP_CTRL.STREAM_CTR_Register",
       signature: "rp2040_svd.xip_ctrl.stream_ctr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STREAM_CTR_Register is record\n   STREAM_CTR     : STREAM_CTR_STREAM_CTR_Field := 16#0#;\n   Reserved_22_31 : HAL.UInt10 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "XIP_CTRL_Peripheral",
       qualified_name: "RP2040_SVD.XIP_CTRL.XIP_CTRL_Peripheral",
       signature: "rp2040_svd.xip_ctrl.xip_ctrl_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type XIP_CTRL_Peripheral is record\n   CTRL        : aliased CTRL_Register;\n   FLUSH       : aliased FLUSH_Register;\n   STAT        : aliased STAT_Register;\n   CTR_HIT     : aliased HAL.UInt32;\n   CTR_ACC     : aliased HAL.UInt32;\n   STREAM_ADDR : aliased STREAM_ADDR_Register;\n   STREAM_CTR  : aliased STREAM_CTR_Register;\n   STREAM_FIFO : aliased HAL.UInt32;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "STREAM_ADDR_STREAM_ADDR_Field",
       qualified_name: "RP2040_SVD.XIP_CTRL.STREAM_ADDR_STREAM_ADDR_Field",
       signature: "rp2040_svd.xip_ctrl.stream_addr_stream_addr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype STREAM_ADDR_STREAM_ADDR_Field is HAL.UInt30;",
       }   ,
       {
       name: "STREAM_CTR_STREAM_CTR_Field",
       qualified_name: "RP2040_SVD.XIP_CTRL.STREAM_CTR_STREAM_CTR_Field",
       signature: "rp2040_svd.xip_ctrl.stream_ctr_stream_ctr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype STREAM_CTR_STREAM_CTR_Field is HAL.UInt22;",
       }   ,
   ]
,variables:    [
       {
       name: "XIP_CTRL_Periph",
       qualified_name: "RP2040_SVD.XIP_CTRL.XIP_CTRL_Periph",
       signature: "rp2040_svd.xip_ctrl.xip_ctrl_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XIP_CTRL_Periph : aliased XIP_CTRL_Peripheral\n  with Import, Address => XIP_CTRL_Base;",
       }   ,
   ]
,}
---
