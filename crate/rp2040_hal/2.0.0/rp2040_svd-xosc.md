---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.XOSC",
qualified_name: "RP2040_SVD.XOSC",
signature: "rp2040_svd.xosc",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "CTRL_ENABLE_Field",
       qualified_name: "RP2040_SVD.XOSC.CTRL_ENABLE_Field",
       signature: "rp2040_svd.xosc.ctrl_enable_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_ENABLE_Field is\n   CTRL_ENABLE_Field_Reset,\n   DISABLE,\n   ENABLE)\n  with Size => 12;",
       }   ,
       {
       name: "CTRL_FREQ_RANGE_Field",
       qualified_name: "RP2040_SVD.XOSC.CTRL_FREQ_RANGE_Field",
       signature: "rp2040_svd.xosc.ctrl_freq_range_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_FREQ_RANGE_Field is\n   CTRL_FREQ_RANGE_Field_Reset,\n   Val_1_15MHZ,\n   RESERVED_1,\n   RESERVED_2,\n   RESERVED_3)\n  with Size => 12;",
       }   ,
       {
       name: "STATUS_FREQ_RANGE_Field",
       qualified_name: "RP2040_SVD.XOSC.STATUS_FREQ_RANGE_Field",
       signature: "rp2040_svd.xosc.status_freq_range_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STATUS_FREQ_RANGE_Field is\n  (Val_1_15MHZ,\n   RESERVED_1,\n   RESERVED_2,\n   RESERVED_3)\n  with Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "COUNT_Register",
       qualified_name: "RP2040_SVD.XOSC.COUNT_Register",
       signature: "rp2040_svd.xosc.count_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type COUNT_Register is record\n   COUNT         : COUNT_COUNT_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "CTRL_Register",
       qualified_name: "RP2040_SVD.XOSC.CTRL_Register",
       signature: "rp2040_svd.xosc.ctrl_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_Register is record\n   FREQ_RANGE     : CTRL_FREQ_RANGE_Field := CTRL_FREQ_RANGE_Field_Reset;\n   ENABLE         : CTRL_ENABLE_Field := CTRL_ENABLE_Field_Reset;\n   Reserved_24_31 : HAL.UInt8 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "STARTUP_Register",
       qualified_name: "RP2040_SVD.XOSC.STARTUP_Register",
       signature: "rp2040_svd.xosc.startup_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STARTUP_Register is record\n   DELAY_k        : STARTUP_DELAY_Field := 16#C4#;\n   Reserved_14_19 : HAL.UInt6 := 16#0#;\n   X4             : Boolean := False;\n   Reserved_21_31 : HAL.UInt11 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "STATUS_Register",
       qualified_name: "RP2040_SVD.XOSC.STATUS_Register",
       signature: "rp2040_svd.xosc.status_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STATUS_Register is record\n   FREQ_RANGE     : STATUS_FREQ_RANGE_Field := RP2040_SVD.XOSC.Val_1_15MHZ;\n   Reserved_2_11  : HAL.UInt10 := 16#0#;\n   ENABLED        : Boolean := False;\n   Reserved_13_23 : HAL.UInt11 := 16#0#;\n   BADWRITE       : Boolean := False;\n   Reserved_25_30 : HAL.UInt6 := 16#0#;\n   STABLE         : Boolean := False;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "XOSC_Peripheral",
       qualified_name: "RP2040_SVD.XOSC.XOSC_Peripheral",
       signature: "rp2040_svd.xosc.xosc_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type XOSC_Peripheral is record\n   CTRL    : aliased CTRL_Register;\n   STATUS  : aliased STATUS_Register;\n   DORMANT : aliased HAL.UInt32;\n   STARTUP : aliased STARTUP_Register;\n   COUNT   : aliased COUNT_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "COUNT_COUNT_Field",
       qualified_name: "RP2040_SVD.XOSC.COUNT_COUNT_Field",
       signature: "rp2040_svd.xosc.count_count_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype COUNT_COUNT_Field is HAL.UInt8;",
       }   ,
       {
       name: "STARTUP_DELAY_Field",
       qualified_name: "RP2040_SVD.XOSC.STARTUP_DELAY_Field",
       signature: "rp2040_svd.xosc.startup_delay_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype STARTUP_DELAY_Field is HAL.UInt14;",
       }   ,
   ]
,variables:    [
       {
       name: "XOSC_Periph",
       qualified_name: "RP2040_SVD.XOSC.XOSC_Periph",
       signature: "rp2040_svd.xosc.xosc_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XOSC_Periph : aliased XOSC_Peripheral\n  with Import, Address => XOSC_Base;",
       }   ,
   ]
,}
---
