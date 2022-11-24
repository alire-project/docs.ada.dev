---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.STK",
qualified_name: "STM32_SVD.STK",
signature: "stm32_svd.stk",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CALIB_Register",
       qualified_name: "STM32_SVD.STK.CALIB_Register",
       signature: "stm32_svd.stk.calib_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CALIB_Register is record\n   TENMS : CALIB_TENMS_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   SKEW : Boolean := False;\n   NOREF : Boolean := False;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CSR_Register",
       qualified_name: "STM32_SVD.STK.CSR_Register",
       signature: "stm32_svd.stk.csr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CSR_Register is record\n   ENABLE : Boolean := False;\n   TICKINT : Boolean := False;\n   CLKSOURCE : Boolean := False;\n   Reserved_3_15 : HAL.UInt13 := 16#0#;\n   COUNTFLAG : Boolean := False;\n   Reserved_17_31 : HAL.UInt15 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CVR_Register",
       qualified_name: "STM32_SVD.STK.CVR_Register",
       signature: "stm32_svd.stk.cvr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CVR_Register is record\n   CURRENT : CVR_CURRENT_Field := 16#0#;\n   Reserved_24_31 : HAL.UInt8 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "RVR_Register",
       qualified_name: "STM32_SVD.STK.RVR_Register",
       signature: "stm32_svd.stk.rvr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RVR_Register is record\n   RELOAD : RVR_RELOAD_Field := 16#0#;\n   Reserved_24_31 : HAL.UInt8 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "STK_Peripheral",
       qualified_name: "STM32_SVD.STK.STK_Peripheral",
       signature: "stm32_svd.stk.stk_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type STK_Peripheral is record\n   CSR : aliased CSR_Register;\n   RVR : aliased RVR_Register;\n   CVR : aliased CVR_Register;\n   CALIB : aliased CALIB_Register;\nend record with\n   Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CALIB_TENMS_Field",
       qualified_name: "STM32_SVD.STK.CALIB_TENMS_Field",
       signature: "stm32_svd.stk.calib_tenms_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CALIB_TENMS_Field is HAL.UInt24;",
       }   ,
       {
       name: "CVR_CURRENT_Field",
       qualified_name: "STM32_SVD.STK.CVR_CURRENT_Field",
       signature: "stm32_svd.stk.cvr_current_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CVR_CURRENT_Field is HAL.UInt24;",
       }   ,
       {
       name: "RVR_RELOAD_Field",
       qualified_name: "STM32_SVD.STK.RVR_RELOAD_Field",
       signature: "stm32_svd.stk.rvr_reload_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype RVR_RELOAD_Field is HAL.UInt24;",
       }   ,
   ]
,variables:    [
       {
       name: "STK_Periph",
       qualified_name: "STM32_SVD.STK.STK_Periph",
       signature: "stm32_svd.stk.stk_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "STK_Periph : aliased STK_Peripheral with\n   Import,\n   Address => STK_Base;",
       }   ,
   ]
,}
---
