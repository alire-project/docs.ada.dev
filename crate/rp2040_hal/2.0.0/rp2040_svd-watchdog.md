---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.WATCHDOG",
qualified_name: "RP2040_SVD.WATCHDOG",
signature: "rp2040_svd.watchdog",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "CTRL_PAUSE_DBG_Field_Array",
       qualified_name: "RP2040_SVD.WATCHDOG.CTRL_PAUSE_DBG_Field_Array",
       signature: "rp2040_svd.watchdog.ctrl_pause_dbg_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_PAUSE_DBG_Field_Array is array (0 .. 1) of Boolean\n  with Component_Size => 1, Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "CTRL_PAUSE_DBG_Field",
       qualified_name: "RP2040_SVD.WATCHDOG.CTRL_PAUSE_DBG_Field",
       signature: "rp2040_svd.watchdog.ctrl_pause_dbg_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_PAUSE_DBG_Field\n  (As_Array : Boolean := False)\nis record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt2;\n      when True =>\n         Arr : CTRL_PAUSE_DBG_Field_Array;\n   end case;\nend record\n  with Unchecked_Union, Size => 2;",
       }   ,
       {
       name: "CTRL_Register",
       qualified_name: "RP2040_SVD.WATCHDOG.CTRL_Register",
       signature: "rp2040_svd.watchdog.ctrl_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_Register is record\n   TIME           : CTRL_TIME_Field := 16#0#;\n   PAUSE_JTAG     : Boolean := True;\n   PAUSE_DBG      : CTRL_PAUSE_DBG_Field :=\n                     (As_Array => False, Val => 16#1#);\n   Reserved_27_29 : HAL.UInt3 := 16#0#;\n   ENABLE         : Boolean := False;\n   TRIGGER        : Boolean := False;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "LOAD_Register",
       qualified_name: "RP2040_SVD.WATCHDOG.LOAD_Register",
       signature: "rp2040_svd.watchdog.load_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type LOAD_Register is record\n   LOAD           : LOAD_LOAD_Field := 16#0#;\n   Reserved_24_31 : HAL.UInt8 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "REASON_Register",
       qualified_name: "RP2040_SVD.WATCHDOG.REASON_Register",
       signature: "rp2040_svd.watchdog.reason_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type REASON_Register is record\n   TIMER         : Boolean;\n   FORCE         : Boolean;\n   Reserved_2_31 : HAL.UInt30;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TICK_Register",
       qualified_name: "RP2040_SVD.WATCHDOG.TICK_Register",
       signature: "rp2040_svd.watchdog.tick_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TICK_Register is record\n   CYCLES         : TICK_CYCLES_Field := 16#0#;\n   ENABLE         : Boolean := True;\n   RUNNING        : Boolean := False;\n   COUNT          : TICK_COUNT_Field := 16#0#;\n   Reserved_20_31 : HAL.UInt12 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "WATCHDOG_Peripheral",
       qualified_name: "RP2040_SVD.WATCHDOG.WATCHDOG_Peripheral",
       signature: "rp2040_svd.watchdog.watchdog_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WATCHDOG_Peripheral is record\n   CTRL     : aliased CTRL_Register;\n   LOAD     : aliased LOAD_Register;\n   REASON   : aliased REASON_Register;\n   SCRATCH0 : aliased HAL.UInt32;\n   SCRATCH1 : aliased HAL.UInt32;\n   SCRATCH2 : aliased HAL.UInt32;\n   SCRATCH3 : aliased HAL.UInt32;\n   SCRATCH4 : aliased HAL.UInt32;\n   SCRATCH5 : aliased HAL.UInt32;\n   SCRATCH6 : aliased HAL.UInt32;\n   SCRATCH7 : aliased HAL.UInt32;\n   TICK     : aliased TICK_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CTRL_TIME_Field",
       qualified_name: "RP2040_SVD.WATCHDOG.CTRL_TIME_Field",
       signature: "rp2040_svd.watchdog.ctrl_time_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRL_TIME_Field is HAL.UInt24;",
       }   ,
       {
       name: "LOAD_LOAD_Field",
       qualified_name: "RP2040_SVD.WATCHDOG.LOAD_LOAD_Field",
       signature: "rp2040_svd.watchdog.load_load_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype LOAD_LOAD_Field is HAL.UInt24;",
       }   ,
       {
       name: "TICK_COUNT_Field",
       qualified_name: "RP2040_SVD.WATCHDOG.TICK_COUNT_Field",
       signature: "rp2040_svd.watchdog.tick_count_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TICK_COUNT_Field is HAL.UInt9;",
       }   ,
       {
       name: "TICK_CYCLES_Field",
       qualified_name: "RP2040_SVD.WATCHDOG.TICK_CYCLES_Field",
       signature: "rp2040_svd.watchdog.tick_cycles_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TICK_CYCLES_Field is HAL.UInt9;",
       }   ,
   ]
,variables:    [
       {
       name: "WATCHDOG_Periph",
       qualified_name: "RP2040_SVD.WATCHDOG.WATCHDOG_Periph",
       signature: "rp2040_svd.watchdog.watchdog_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "WATCHDOG_Periph : aliased WATCHDOG_Peripheral\n  with Import, Address => WATCHDOG_Base;",
       }   ,
   ]
,}
---
