---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.DBGMCU",
qualified_name: "STM32_SVD.DBGMCU",
signature: "stm32_svd.dbgmcu",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "APB1_FZ_Register",
       qualified_name: "STM32_SVD.DBGMCU.APB1_FZ_Register",
       signature: "stm32_svd.dbgmcu.apb1_fz_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB1_FZ_Register is record\n   DBG_TIM2_STOP : Boolean := False;\n   DBG_TIM3_STOP : Boolean := False;\n   Reserved_2_3 : HAL.UInt2 := 16#0#;\n   DBG_TIM6_STOP : Boolean := False;\n   DBG_TIM7_STOP : Boolean := False;\n   Reserved_6_7 : HAL.UInt2 := 16#0#;\n   DBG_TIM14_STOP : Boolean := False;\n   Reserved_9_9 : HAL.Bit := 16#0#;\n   DBG_RTC_STOP : Boolean := False;\n   DBG_WWDG_STOP : Boolean := False;\n   DBG_IWDG_STOP : Boolean := False;\n   Reserved_13_20 : HAL.UInt8 := 16#0#;\n   DBG_I2C1_SMBUS_TIMEOUT : Boolean := False;\n   Reserved_22_24 : HAL.UInt3 := 16#0#;\n   DBG_CAN_STOP : Boolean := False;\n   Reserved_26_31 : HAL.UInt6 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "APB2_FZ_Register",
       qualified_name: "STM32_SVD.DBGMCU.APB2_FZ_Register",
       signature: "stm32_svd.dbgmcu.apb2_fz_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB2_FZ_Register is record\n   Reserved_0_10 : HAL.UInt11 := 16#0#;\n   DBG_TIM1_STOP : Boolean := False;\n   Reserved_12_15 : HAL.UInt4 := 16#0#;\n   DBG_TIM15_STOP : Boolean := False;\n   DBG_TIM16_STOP : Boolean := False;\n   DBG_TIM17_STOP : Boolean := False;\n   Reserved_19_31 : HAL.UInt13 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.DBGMCU.CR_Register",
       signature: "stm32_svd.dbgmcu.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   Reserved_0_0 : HAL.Bit := 16#0#;\n   DBG_STOP : Boolean := False;\n   DBG_STANDBY : Boolean := False;\n   Reserved_3_31 : HAL.UInt29 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DBGMCU_Peripheral",
       qualified_name: "STM32_SVD.DBGMCU.DBGMCU_Peripheral",
       signature: "stm32_svd.dbgmcu.dbgmcu_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DBGMCU_Peripheral is record\n   IDCODE : aliased IDCODE_Register;\n   CR : aliased CR_Register;\n   APB1_FZ : aliased APB1_FZ_Register;\n   APB2_FZ : aliased APB2_FZ_Register;\nend record with\n   Volatile;",
       }   ,
       {
       name: "IDCODE_Register",
       qualified_name: "STM32_SVD.DBGMCU.IDCODE_Register",
       signature: "stm32_svd.dbgmcu.idcode_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IDCODE_Register is record\n   DEV_ID : IDCODE_DEV_ID_Field;\n   DIV_ID : IDCODE_DIV_ID_Field;\n   REV_ID : IDCODE_REV_ID_Field;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "IDCODE_DEV_ID_Field",
       qualified_name: "STM32_SVD.DBGMCU.IDCODE_DEV_ID_Field",
       signature: "stm32_svd.dbgmcu.idcode_dev_id_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IDCODE_DEV_ID_Field is HAL.UInt12;",
       }   ,
       {
       name: "IDCODE_DIV_ID_Field",
       qualified_name: "STM32_SVD.DBGMCU.IDCODE_DIV_ID_Field",
       signature: "stm32_svd.dbgmcu.idcode_div_id_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IDCODE_DIV_ID_Field is HAL.UInt4;",
       }   ,
       {
       name: "IDCODE_REV_ID_Field",
       qualified_name: "STM32_SVD.DBGMCU.IDCODE_REV_ID_Field",
       signature: "stm32_svd.dbgmcu.idcode_rev_id_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IDCODE_REV_ID_Field is HAL.UInt16;",
       }   ,
   ]
,variables:    [
       {
       name: "DBGMCU_Periph",
       qualified_name: "STM32_SVD.DBGMCU.DBGMCU_Periph",
       signature: "stm32_svd.dbgmcu.dbgmcu_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DBGMCU_Periph : aliased DBGMCU_Peripheral with\n   Import,\n   Address => DBGMCU_Base;",
       }   ,
   ]
,}
---
