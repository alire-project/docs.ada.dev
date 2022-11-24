---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.WWDG",
qualified_name: "STM32_SVD.WWDG",
signature: "stm32_svd.wwdg",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CFR_Register",
       qualified_name: "STM32_SVD.WWDG.CFR_Register",
       signature: "stm32_svd.wwdg.cfr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CFR_Register is record\n   W : CFR_W_Field := 16#7F#;\n   WDGTB : CFR_WDGTB_Field := 16#0#;\n   EWI : Boolean := False;\n   Reserved_10_31 : HAL.UInt22 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.WWDG.CR_Register",
       signature: "stm32_svd.wwdg.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   T : CR_T_Field := 16#7F#;\n   WDGA : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SR_Register",
       qualified_name: "STM32_SVD.WWDG.SR_Register",
       signature: "stm32_svd.wwdg.sr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SR_Register is record\n   EWIF : Boolean := False;\n   Reserved_1_31 : HAL.UInt31 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "WWDG_Peripheral",
       qualified_name: "STM32_SVD.WWDG.WWDG_Peripheral",
       signature: "stm32_svd.wwdg.wwdg_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WWDG_Peripheral is record\n   CR : aliased CR_Register;\n   CFR : aliased CFR_Register;\n   SR : aliased SR_Register;\nend record with\n   Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CFR_W_Field",
       qualified_name: "STM32_SVD.WWDG.CFR_W_Field",
       signature: "stm32_svd.wwdg.cfr_w_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFR_W_Field is HAL.UInt7;",
       }   ,
       {
       name: "CFR_WDGTB_Field",
       qualified_name: "STM32_SVD.WWDG.CFR_WDGTB_Field",
       signature: "stm32_svd.wwdg.cfr_wdgtb_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFR_WDGTB_Field is HAL.UInt2;",
       }   ,
       {
       name: "CR_T_Field",
       qualified_name: "STM32_SVD.WWDG.CR_T_Field",
       signature: "stm32_svd.wwdg.cr_t_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_T_Field is HAL.UInt7;",
       }   ,
   ]
,variables:    [
       {
       name: "WWDG_Periph",
       qualified_name: "STM32_SVD.WWDG.WWDG_Periph",
       signature: "stm32_svd.wwdg.wwdg_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "WWDG_Periph : aliased WWDG_Peripheral with\n   Import,\n   Address => WWDG_Base;",
       }   ,
   ]
,}
---
