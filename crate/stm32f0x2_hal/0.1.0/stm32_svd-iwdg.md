---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.IWDG",
qualified_name: "STM32_SVD.IWDG",
signature: "stm32_svd.iwdg",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "IWDG_Peripheral",
       qualified_name: "STM32_SVD.IWDG.IWDG_Peripheral",
       signature: "stm32_svd.iwdg.iwdg_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IWDG_Peripheral is record\n   KR : aliased KR_Register;\n   PR : aliased PR_Register;\n   RLR : aliased RLR_Register;\n   SR : aliased SR_Register;\n   WINR : aliased WINR_Register;\nend record with\n   Volatile;",
       }   ,
       {
       name: "KR_Register",
       qualified_name: "STM32_SVD.IWDG.KR_Register",
       signature: "stm32_svd.iwdg.kr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type KR_Register is record\n   KEY : KR_KEY_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "PR_Register",
       qualified_name: "STM32_SVD.IWDG.PR_Register",
       signature: "stm32_svd.iwdg.pr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PR_Register is record\n   PR : PR_PR_Field := 16#0#;\n   Reserved_3_31 : HAL.UInt29 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "RLR_Register",
       qualified_name: "STM32_SVD.IWDG.RLR_Register",
       signature: "stm32_svd.iwdg.rlr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RLR_Register is record\n   RL : RLR_RL_Field := 16#FFF#;\n   Reserved_12_31 : HAL.UInt20 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SR_Register",
       qualified_name: "STM32_SVD.IWDG.SR_Register",
       signature: "stm32_svd.iwdg.sr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SR_Register is record\n   PVU : Boolean;\n   RVU : Boolean;\n   WVU : Boolean;\n   Reserved_3_31 : HAL.UInt29;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "WINR_Register",
       qualified_name: "STM32_SVD.IWDG.WINR_Register",
       signature: "stm32_svd.iwdg.winr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type WINR_Register is record\n   WIN : WINR_WIN_Field := 16#FFF#;\n   Reserved_12_31 : HAL.UInt20 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "KR_KEY_Field",
       qualified_name: "STM32_SVD.IWDG.KR_KEY_Field",
       signature: "stm32_svd.iwdg.kr_key_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype KR_KEY_Field is HAL.UInt16;",
       }   ,
       {
       name: "PR_PR_Field",
       qualified_name: "STM32_SVD.IWDG.PR_PR_Field",
       signature: "stm32_svd.iwdg.pr_pr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PR_PR_Field is HAL.UInt3;",
       }   ,
       {
       name: "RLR_RL_Field",
       qualified_name: "STM32_SVD.IWDG.RLR_RL_Field",
       signature: "stm32_svd.iwdg.rlr_rl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype RLR_RL_Field is HAL.UInt12;",
       }   ,
       {
       name: "WINR_WIN_Field",
       qualified_name: "STM32_SVD.IWDG.WINR_WIN_Field",
       signature: "stm32_svd.iwdg.winr_win_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype WINR_WIN_Field is HAL.UInt12;",
       }   ,
   ]
,variables:    [
       {
       name: "IWDG_Periph",
       qualified_name: "STM32_SVD.IWDG.IWDG_Periph",
       signature: "stm32_svd.iwdg.iwdg_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "IWDG_Periph : aliased IWDG_Peripheral with\n   Import,\n   Address => IWDG_Base;",
       }   ,
   ]
,}
---
