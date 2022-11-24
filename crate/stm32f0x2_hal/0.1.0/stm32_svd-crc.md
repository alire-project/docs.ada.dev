---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.CRC",
qualified_name: "STM32_SVD.CRC",
signature: "stm32_svd.crc",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.CRC.CR_Register",
       signature: "stm32_svd.crc.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   RESET : Boolean := False;\n   Reserved_1_2 : HAL.UInt2 := 16#0#;\n   POLYSIZE : CR_POLYSIZE_Field := 16#0#;\n   REV_IN : CR_REV_IN_Field := 16#0#;\n   REV_OUT : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CRC_Peripheral",
       qualified_name: "STM32_SVD.CRC.CRC_Peripheral",
       signature: "stm32_svd.crc.crc_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CRC_Peripheral is record\n   DR : aliased HAL.UInt32;\n   IDR : aliased IDR_Register;\n   CR : aliased CR_Register;\n   INIT : aliased HAL.UInt32;\nend record with\n   Volatile;",
       }   ,
       {
       name: "IDR_Register",
       qualified_name: "STM32_SVD.CRC.IDR_Register",
       signature: "stm32_svd.crc.idr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IDR_Register is record\n   IDR : IDR_IDR_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CR_POLYSIZE_Field",
       qualified_name: "STM32_SVD.CRC.CR_POLYSIZE_Field",
       signature: "stm32_svd.crc.cr_polysize_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_POLYSIZE_Field is HAL.UInt2;",
       }   ,
       {
       name: "CR_REV_IN_Field",
       qualified_name: "STM32_SVD.CRC.CR_REV_IN_Field",
       signature: "stm32_svd.crc.cr_rev_in_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_REV_IN_Field is HAL.UInt2;",
       }   ,
       {
       name: "IDR_IDR_Field",
       qualified_name: "STM32_SVD.CRC.IDR_IDR_Field",
       signature: "stm32_svd.crc.idr_idr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IDR_IDR_Field is HAL.UInt8;",
       }   ,
   ]
,variables:    [
       {
       name: "CRC_Periph",
       qualified_name: "STM32_SVD.CRC.CRC_Periph",
       signature: "stm32_svd.crc.crc_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CRC_Periph : aliased CRC_Peripheral with\n   Import,\n   Address => CRC_Base;",
       }   ,
   ]
,}
---
