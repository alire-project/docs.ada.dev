---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.NVIC",
qualified_name: "STM32_SVD.NVIC",
signature: "stm32_svd.nvic",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "IPR0_Register",
       qualified_name: "STM32_SVD.NVIC.IPR0_Register",
       signature: "stm32_svd.nvic.ipr0_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR0_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_00 : IPR0_PRI_00_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_01 : IPR0_PRI_01_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_02 : IPR0_PRI_02_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_03 : IPR0_PRI_03_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR1_Register",
       qualified_name: "STM32_SVD.NVIC.IPR1_Register",
       signature: "stm32_svd.nvic.ipr1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR1_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_40 : IPR1_PRI_40_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_41 : IPR1_PRI_41_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_42 : IPR1_PRI_42_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_43 : IPR1_PRI_43_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR2_Register",
       qualified_name: "STM32_SVD.NVIC.IPR2_Register",
       signature: "stm32_svd.nvic.ipr2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR2_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_80 : IPR2_PRI_80_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_81 : IPR2_PRI_81_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_82 : IPR2_PRI_82_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_83 : IPR2_PRI_83_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR3_Register",
       qualified_name: "STM32_SVD.NVIC.IPR3_Register",
       signature: "stm32_svd.nvic.ipr3_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR3_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_120 : IPR3_PRI_120_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_121 : IPR3_PRI_121_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_122 : IPR3_PRI_122_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_123 : IPR3_PRI_123_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR4_Register",
       qualified_name: "STM32_SVD.NVIC.IPR4_Register",
       signature: "stm32_svd.nvic.ipr4_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR4_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_160 : IPR4_PRI_160_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_161 : IPR4_PRI_161_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_162 : IPR4_PRI_162_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_163 : IPR4_PRI_163_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR5_Register",
       qualified_name: "STM32_SVD.NVIC.IPR5_Register",
       signature: "stm32_svd.nvic.ipr5_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR5_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_200 : IPR5_PRI_200_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_201 : IPR5_PRI_201_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_202 : IPR5_PRI_202_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_203 : IPR5_PRI_203_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR6_Register",
       qualified_name: "STM32_SVD.NVIC.IPR6_Register",
       signature: "stm32_svd.nvic.ipr6_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR6_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_240 : IPR6_PRI_240_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_241 : IPR6_PRI_241_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_242 : IPR6_PRI_242_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_243 : IPR6_PRI_243_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "IPR7_Register",
       qualified_name: "STM32_SVD.NVIC.IPR7_Register",
       signature: "stm32_svd.nvic.ipr7_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IPR7_Register is record\n   Reserved_0_5 : HAL.UInt6 := 16#0#;\n   PRI_280 : IPR7_PRI_280_Field := 16#0#;\n   Reserved_8_13 : HAL.UInt6 := 16#0#;\n   PRI_281 : IPR7_PRI_281_Field := 16#0#;\n   Reserved_16_21 : HAL.UInt6 := 16#0#;\n   PRI_282 : IPR7_PRI_282_Field := 16#0#;\n   Reserved_24_29 : HAL.UInt6 := 16#0#;\n   PRI_283 : IPR7_PRI_283_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "NVIC_Peripheral",
       qualified_name: "STM32_SVD.NVIC.NVIC_Peripheral",
       signature: "stm32_svd.nvic.nvic_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type NVIC_Peripheral is record\n   ISER : aliased HAL.UInt32;\n   ICER : aliased HAL.UInt32;\n   ISPR : aliased HAL.UInt32;\n   ICPR : aliased HAL.UInt32;\n   IPR0 : aliased IPR0_Register;\n   IPR1 : aliased IPR1_Register;\n   IPR2 : aliased IPR2_Register;\n   IPR3 : aliased IPR3_Register;\n   IPR4 : aliased IPR4_Register;\n   IPR5 : aliased IPR5_Register;\n   IPR6 : aliased IPR6_Register;\n   IPR7 : aliased IPR7_Register;\nend record with\n   Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "IPR0_PRI_00_Field",
       qualified_name: "STM32_SVD.NVIC.IPR0_PRI_00_Field",
       signature: "stm32_svd.nvic.ipr0_pri_00_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR0_PRI_00_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR0_PRI_01_Field",
       qualified_name: "STM32_SVD.NVIC.IPR0_PRI_01_Field",
       signature: "stm32_svd.nvic.ipr0_pri_01_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR0_PRI_01_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR0_PRI_02_Field",
       qualified_name: "STM32_SVD.NVIC.IPR0_PRI_02_Field",
       signature: "stm32_svd.nvic.ipr0_pri_02_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR0_PRI_02_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR0_PRI_03_Field",
       qualified_name: "STM32_SVD.NVIC.IPR0_PRI_03_Field",
       signature: "stm32_svd.nvic.ipr0_pri_03_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR0_PRI_03_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR1_PRI_40_Field",
       qualified_name: "STM32_SVD.NVIC.IPR1_PRI_40_Field",
       signature: "stm32_svd.nvic.ipr1_pri_40_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR1_PRI_40_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR1_PRI_41_Field",
       qualified_name: "STM32_SVD.NVIC.IPR1_PRI_41_Field",
       signature: "stm32_svd.nvic.ipr1_pri_41_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR1_PRI_41_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR1_PRI_42_Field",
       qualified_name: "STM32_SVD.NVIC.IPR1_PRI_42_Field",
       signature: "stm32_svd.nvic.ipr1_pri_42_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR1_PRI_42_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR1_PRI_43_Field",
       qualified_name: "STM32_SVD.NVIC.IPR1_PRI_43_Field",
       signature: "stm32_svd.nvic.ipr1_pri_43_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR1_PRI_43_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR2_PRI_80_Field",
       qualified_name: "STM32_SVD.NVIC.IPR2_PRI_80_Field",
       signature: "stm32_svd.nvic.ipr2_pri_80_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR2_PRI_80_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR2_PRI_81_Field",
       qualified_name: "STM32_SVD.NVIC.IPR2_PRI_81_Field",
       signature: "stm32_svd.nvic.ipr2_pri_81_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR2_PRI_81_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR2_PRI_82_Field",
       qualified_name: "STM32_SVD.NVIC.IPR2_PRI_82_Field",
       signature: "stm32_svd.nvic.ipr2_pri_82_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR2_PRI_82_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR2_PRI_83_Field",
       qualified_name: "STM32_SVD.NVIC.IPR2_PRI_83_Field",
       signature: "stm32_svd.nvic.ipr2_pri_83_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR2_PRI_83_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR3_PRI_120_Field",
       qualified_name: "STM32_SVD.NVIC.IPR3_PRI_120_Field",
       signature: "stm32_svd.nvic.ipr3_pri_120_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR3_PRI_120_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR3_PRI_121_Field",
       qualified_name: "STM32_SVD.NVIC.IPR3_PRI_121_Field",
       signature: "stm32_svd.nvic.ipr3_pri_121_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR3_PRI_121_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR3_PRI_122_Field",
       qualified_name: "STM32_SVD.NVIC.IPR3_PRI_122_Field",
       signature: "stm32_svd.nvic.ipr3_pri_122_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR3_PRI_122_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR3_PRI_123_Field",
       qualified_name: "STM32_SVD.NVIC.IPR3_PRI_123_Field",
       signature: "stm32_svd.nvic.ipr3_pri_123_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR3_PRI_123_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR4_PRI_160_Field",
       qualified_name: "STM32_SVD.NVIC.IPR4_PRI_160_Field",
       signature: "stm32_svd.nvic.ipr4_pri_160_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR4_PRI_160_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR4_PRI_161_Field",
       qualified_name: "STM32_SVD.NVIC.IPR4_PRI_161_Field",
       signature: "stm32_svd.nvic.ipr4_pri_161_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR4_PRI_161_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR4_PRI_162_Field",
       qualified_name: "STM32_SVD.NVIC.IPR4_PRI_162_Field",
       signature: "stm32_svd.nvic.ipr4_pri_162_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR4_PRI_162_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR4_PRI_163_Field",
       qualified_name: "STM32_SVD.NVIC.IPR4_PRI_163_Field",
       signature: "stm32_svd.nvic.ipr4_pri_163_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR4_PRI_163_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR5_PRI_200_Field",
       qualified_name: "STM32_SVD.NVIC.IPR5_PRI_200_Field",
       signature: "stm32_svd.nvic.ipr5_pri_200_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR5_PRI_200_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR5_PRI_201_Field",
       qualified_name: "STM32_SVD.NVIC.IPR5_PRI_201_Field",
       signature: "stm32_svd.nvic.ipr5_pri_201_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR5_PRI_201_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR5_PRI_202_Field",
       qualified_name: "STM32_SVD.NVIC.IPR5_PRI_202_Field",
       signature: "stm32_svd.nvic.ipr5_pri_202_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR5_PRI_202_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR5_PRI_203_Field",
       qualified_name: "STM32_SVD.NVIC.IPR5_PRI_203_Field",
       signature: "stm32_svd.nvic.ipr5_pri_203_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR5_PRI_203_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR6_PRI_240_Field",
       qualified_name: "STM32_SVD.NVIC.IPR6_PRI_240_Field",
       signature: "stm32_svd.nvic.ipr6_pri_240_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR6_PRI_240_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR6_PRI_241_Field",
       qualified_name: "STM32_SVD.NVIC.IPR6_PRI_241_Field",
       signature: "stm32_svd.nvic.ipr6_pri_241_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR6_PRI_241_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR6_PRI_242_Field",
       qualified_name: "STM32_SVD.NVIC.IPR6_PRI_242_Field",
       signature: "stm32_svd.nvic.ipr6_pri_242_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR6_PRI_242_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR6_PRI_243_Field",
       qualified_name: "STM32_SVD.NVIC.IPR6_PRI_243_Field",
       signature: "stm32_svd.nvic.ipr6_pri_243_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR6_PRI_243_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR7_PRI_280_Field",
       qualified_name: "STM32_SVD.NVIC.IPR7_PRI_280_Field",
       signature: "stm32_svd.nvic.ipr7_pri_280_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR7_PRI_280_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR7_PRI_281_Field",
       qualified_name: "STM32_SVD.NVIC.IPR7_PRI_281_Field",
       signature: "stm32_svd.nvic.ipr7_pri_281_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR7_PRI_281_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR7_PRI_282_Field",
       qualified_name: "STM32_SVD.NVIC.IPR7_PRI_282_Field",
       signature: "stm32_svd.nvic.ipr7_pri_282_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR7_PRI_282_Field is HAL.UInt2;",
       }   ,
       {
       name: "IPR7_PRI_283_Field",
       qualified_name: "STM32_SVD.NVIC.IPR7_PRI_283_Field",
       signature: "stm32_svd.nvic.ipr7_pri_283_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IPR7_PRI_283_Field is HAL.UInt2;",
       }   ,
   ]
,variables:    [
       {
       name: "NVIC_Periph",
       qualified_name: "STM32_SVD.NVIC.NVIC_Periph",
       signature: "stm32_svd.nvic.nvic_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NVIC_Periph : aliased NVIC_Peripheral with\n   Import,\n   Address => NVIC_Base;",
       }   ,
   ]
,}
---