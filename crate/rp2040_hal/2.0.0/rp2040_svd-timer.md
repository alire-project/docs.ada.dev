---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.TIMER",
qualified_name: "RP2040_SVD.TIMER",
signature: "rp2040_svd.timer",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "DBGPAUSE_DBG_Field_Array",
       qualified_name: "RP2040_SVD.TIMER.DBGPAUSE_DBG_Field_Array",
       signature: "rp2040_svd.timer.dbgpause_dbg_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DBGPAUSE_DBG_Field_Array is array (0 .. 1) of Boolean\n  with Component_Size => 1, Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "ARMED_Register",
       qualified_name: "RP2040_SVD.TIMER.ARMED_Register",
       signature: "rp2040_svd.timer.armed_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ARMED_Register is record\n   ARMED         : ARMED_ARMED_Field := 16#0#;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "DBGPAUSE_DBG_Field",
       qualified_name: "RP2040_SVD.TIMER.DBGPAUSE_DBG_Field",
       signature: "rp2040_svd.timer.dbgpause_dbg_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DBGPAUSE_DBG_Field\n  (As_Array : Boolean := False)\nis record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt2;\n      when True =>\n         Arr : DBGPAUSE_DBG_Field_Array;\n   end case;\nend record\n  with Unchecked_Union, Size => 2;",
       }   ,
       {
       name: "DBGPAUSE_Register",
       qualified_name: "RP2040_SVD.TIMER.DBGPAUSE_Register",
       signature: "rp2040_svd.timer.dbgpause_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DBGPAUSE_Register is record\n   Reserved_0_0  : HAL.Bit := 16#1#;\n   DBG           : DBGPAUSE_DBG_Field := (As_Array => False, Val => 16#1#);\n   Reserved_3_31 : HAL.UInt29 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "INTE_Register",
       qualified_name: "RP2040_SVD.TIMER.INTE_Register",
       signature: "rp2040_svd.timer.inte_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type INTE_Register is record\n   ALARM_0       : Boolean := False;\n   ALARM_1       : Boolean := False;\n   ALARM_2       : Boolean := False;\n   ALARM_3       : Boolean := False;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "INTF_Register",
       qualified_name: "RP2040_SVD.TIMER.INTF_Register",
       signature: "rp2040_svd.timer.intf_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type INTF_Register is record\n   ALARM_0       : Boolean := False;\n   ALARM_1       : Boolean := False;\n   ALARM_2       : Boolean := False;\n   ALARM_3       : Boolean := False;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "INTR_Register",
       qualified_name: "RP2040_SVD.TIMER.INTR_Register",
       signature: "rp2040_svd.timer.intr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type INTR_Register is record\n   ALARM_0       : Boolean := False;\n   ALARM_1       : Boolean := False;\n   ALARM_2       : Boolean := False;\n   ALARM_3       : Boolean := False;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "INTS_Register",
       qualified_name: "RP2040_SVD.TIMER.INTS_Register",
       signature: "rp2040_svd.timer.ints_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type INTS_Register is record\n   ALARM_0       : Boolean;\n   ALARM_1       : Boolean;\n   ALARM_2       : Boolean;\n   ALARM_3       : Boolean;\n   Reserved_4_31 : HAL.UInt28;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PAUSE_Register",
       qualified_name: "RP2040_SVD.TIMER.PAUSE_Register",
       signature: "rp2040_svd.timer.pause_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PAUSE_Register is record\n   PAUSE         : Boolean := False;\n   Reserved_1_31 : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TIMER_Peripheral",
       qualified_name: "RP2040_SVD.TIMER.TIMER_Peripheral",
       signature: "rp2040_svd.timer.timer_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TIMER_Peripheral is record\n   TIMEHW   : aliased HAL.UInt32;\n   TIMELW   : aliased HAL.UInt32;\n   TIMEHR   : aliased HAL.UInt32;\n   TIMELR   : aliased HAL.UInt32;\n   ALARM0   : aliased HAL.UInt32;\n   ALARM1   : aliased HAL.UInt32;\n   ALARM2   : aliased HAL.UInt32;\n   ALARM3   : aliased HAL.UInt32;\n   ARMED    : aliased ARMED_Register;\n   TIMERAWH : aliased HAL.UInt32;\n   TIMERAWL : aliased HAL.UInt32;\n   DBGPAUSE : aliased DBGPAUSE_Register;\n   PAUSE    : aliased PAUSE_Register;\n   INTR     : aliased INTR_Register;\n   INTE     : aliased INTE_Register;\n   INTF     : aliased INTF_Register;\n   INTS     : aliased INTS_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ARMED_ARMED_Field",
       qualified_name: "RP2040_SVD.TIMER.ARMED_ARMED_Field",
       signature: "rp2040_svd.timer.armed_armed_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ARMED_ARMED_Field is HAL.UInt4;",
       }   ,
   ]
,variables:    [
       {
       name: "TIMER_Periph",
       qualified_name: "RP2040_SVD.TIMER.TIMER_Periph",
       signature: "rp2040_svd.timer.timer_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TIMER_Periph : aliased TIMER_Peripheral\n  with Import, Address => TIMER_Base;",
       }   ,
   ]
,}
---
