---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.RCC",
qualified_name: "STM32_SVD.RCC",
signature: "stm32_svd.rcc",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "AHBENR_Register",
       qualified_name: "STM32_SVD.RCC.AHBENR_Register",
       signature: "stm32_svd.rcc.ahbenr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type AHBENR_Register is record\n   DMA1EN : Boolean := False;\n   Reserved_1_1 : HAL.Bit := 16#0#;\n   SRAMEN : Boolean := True;\n   Reserved_3_3 : HAL.Bit := 16#0#;\n   FLITFEN : Boolean := True;\n   Reserved_5_5 : HAL.Bit := 16#0#;\n   CRCEN : Boolean := False;\n   Reserved_7_16 : HAL.UInt10 := 16#0#;\n   IOPAEN : Boolean := False;\n   IOPBEN : Boolean := False;\n   IOPCEN : Boolean := False;\n   IOPDEN : Boolean := False;\n   Reserved_21_21 : HAL.Bit := 16#0#;\n   IOPFEN : Boolean := False;\n   Reserved_23_23 : HAL.Bit := 16#0#;\n   TSCEN : Boolean := False;\n   Reserved_25_31 : HAL.UInt7 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "AHBRSTR_Register",
       qualified_name: "STM32_SVD.RCC.AHBRSTR_Register",
       signature: "stm32_svd.rcc.ahbrstr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type AHBRSTR_Register is record\n   Reserved_0_16 : HAL.UInt17 := 16#0#;\n   IOPARST : Boolean := False;\n   IOPBRST : Boolean := False;\n   IOPCRST : Boolean := False;\n   IOPDRST : Boolean := False;\n   Reserved_21_21 : HAL.Bit := 16#0#;\n   IOPFRST : Boolean := False;\n   Reserved_23_23 : HAL.Bit := 16#0#;\n   TSCRST : Boolean := False;\n   Reserved_25_31 : HAL.UInt7 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "APB1ENR_Register",
       qualified_name: "STM32_SVD.RCC.APB1ENR_Register",
       signature: "stm32_svd.rcc.apb1enr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB1ENR_Register is record\n   TIM2EN : Boolean := False;\n   TIM3EN : Boolean := False;\n   Reserved_2_3 : HAL.UInt2 := 16#0#;\n   TIM6EN : Boolean := False;\n   TIM7EN : Boolean := False;\n   Reserved_6_7 : HAL.UInt2 := 16#0#;\n   TIM14EN : Boolean := False;\n   Reserved_9_10 : HAL.UInt2 := 16#0#;\n   WWDGEN : Boolean := False;\n   Reserved_12_13 : HAL.UInt2 := 16#0#;\n   SPI2EN : Boolean := False;\n   Reserved_15_16 : HAL.UInt2 := 16#0#;\n   USART2EN : Boolean := False;\n   USART3EN : Boolean := False;\n   USART4EN : Boolean := False;\n   Reserved_20_20 : HAL.Bit := 16#0#;\n   I2C1EN : Boolean := False;\n   I2C2EN : Boolean := False;\n   USBRST : Boolean := False;\n   Reserved_24_24 : HAL.Bit := 16#0#;\n   CANEN : Boolean := False;\n   Reserved_26_26 : HAL.Bit := 16#0#;\n   CRSEN : Boolean := False;\n   PWREN : Boolean := False;\n   DACEN : Boolean := False;\n   CECEN : Boolean := False;\n   Reserved_31_31 : HAL.Bit := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "APB1RSTR_Register",
       qualified_name: "STM32_SVD.RCC.APB1RSTR_Register",
       signature: "stm32_svd.rcc.apb1rstr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB1RSTR_Register is record\n   TIM2RST : Boolean := False;\n   TIM3RST : Boolean := False;\n   Reserved_2_3 : HAL.UInt2 := 16#0#;\n   TIM6RST : Boolean := False;\n   TIM7RST : Boolean := False;\n   Reserved_6_7 : HAL.UInt2 := 16#0#;\n   TIM14RST : Boolean := False;\n   Reserved_9_10 : HAL.UInt2 := 16#0#;\n   WWDGRST : Boolean := False;\n   Reserved_12_13 : HAL.UInt2 := 16#0#;\n   SPI2RST : Boolean := False;\n   Reserved_15_16 : HAL.UInt2 := 16#0#;\n   USART2RST : Boolean := False;\n   USART3RST : Boolean := False;\n   USART4RST : Boolean := False;\n   Reserved_20_20 : HAL.Bit := 16#0#;\n   I2C1RST : Boolean := False;\n   I2C2RST : Boolean := False;\n   USBRST : Boolean := False;\n   Reserved_24_24 : HAL.Bit := 16#0#;\n   CANRST : Boolean := False;\n   Reserved_26_26 : HAL.Bit := 16#0#;\n   CRSRST : Boolean := False;\n   PWRRST : Boolean := False;\n   DACRST : Boolean := False;\n   CECRST : Boolean := False;\n   Reserved_31_31 : HAL.Bit := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "APB2ENR_Register",
       qualified_name: "STM32_SVD.RCC.APB2ENR_Register",
       signature: "stm32_svd.rcc.apb2enr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB2ENR_Register is record\n   SYSCFGEN : Boolean := False;\n   Reserved_1_8 : HAL.UInt8 := 16#0#;\n   ADCEN : Boolean := False;\n   Reserved_10_10 : HAL.Bit := 16#0#;\n   TIM1EN : Boolean := False;\n   SPI1EN : Boolean := False;\n   Reserved_13_13 : HAL.Bit := 16#0#;\n   USART1EN : Boolean := False;\n   Reserved_15_15 : HAL.Bit := 16#0#;\n   TIM15EN : Boolean := False;\n   TIM16EN : Boolean := False;\n   TIM17EN : Boolean := False;\n   Reserved_19_21 : HAL.UInt3 := 16#0#;\n   DBGMCUEN : Boolean := False;\n   Reserved_23_31 : HAL.UInt9 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "APB2RSTR_Register",
       qualified_name: "STM32_SVD.RCC.APB2RSTR_Register",
       signature: "stm32_svd.rcc.apb2rstr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type APB2RSTR_Register is record\n   SYSCFGRST : Boolean := False;\n   Reserved_1_8 : HAL.UInt8 := 16#0#;\n   ADCRST : Boolean := False;\n   Reserved_10_10 : HAL.Bit := 16#0#;\n   TIM1RST : Boolean := False;\n   SPI1RST : Boolean := False;\n   Reserved_13_13 : HAL.Bit := 16#0#;\n   USART1RST : Boolean := False;\n   Reserved_15_15 : HAL.Bit := 16#0#;\n   TIM15RST : Boolean := False;\n   TIM16RST : Boolean := False;\n   TIM17RST : Boolean := False;\n   Reserved_19_21 : HAL.UInt3 := 16#0#;\n   DBGMCURST : Boolean := False;\n   Reserved_23_31 : HAL.UInt9 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "BDCR_Register",
       qualified_name: "STM32_SVD.RCC.BDCR_Register",
       signature: "stm32_svd.rcc.bdcr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BDCR_Register is record\n   LSEON : Boolean := False;\n   LSERDY : Boolean := False;\n   LSEBYP : Boolean := False;\n   LSEDRV : BDCR_LSEDRV_Field := 16#0#;\n   Reserved_5_7 : HAL.UInt3 := 16#0#;\n   RTCSEL : BDCR_RTCSEL_Field := 16#0#;\n   Reserved_10_14 : HAL.UInt5 := 16#0#;\n   RTCEN : Boolean := False;\n   BDRST : Boolean := False;\n   Reserved_17_31 : HAL.UInt15 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CFGR2_Register",
       qualified_name: "STM32_SVD.RCC.CFGR2_Register",
       signature: "stm32_svd.rcc.cfgr2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CFGR2_Register is record\n   PREDIV : CFGR2_PREDIV_Field := 16#0#;\n   Reserved_4_31 : HAL.UInt28 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CFGR3_Register",
       qualified_name: "STM32_SVD.RCC.CFGR3_Register",
       signature: "stm32_svd.rcc.cfgr3_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CFGR3_Register is record\n   USART1SW : CFGR3_USART1SW_Field := 16#0#;\n   Reserved_2_3 : HAL.UInt2 := 16#0#;\n   I2C1SW : Boolean := False;\n   Reserved_5_5 : HAL.Bit := 16#0#;\n   CECSW : Boolean := False;\n   USBSW : Boolean := False;\n   ADCSW : Boolean := False;\n   Reserved_9_15 : HAL.UInt7 := 16#0#;\n   USART2SW : CFGR3_USART2SW_Field := 16#0#;\n   Reserved_18_31 : HAL.UInt14 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CFGR_Register",
       qualified_name: "STM32_SVD.RCC.CFGR_Register",
       signature: "stm32_svd.rcc.cfgr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CFGR_Register is record\n   SW : CFGR_SW_Field := 16#0#;\n   SWS : CFGR_SWS_Field := 16#0#;\n   HPRE : CFGR_HPRE_Field := 16#0#;\n   PPRE : CFGR_PPRE_Field := 16#0#;\n   Reserved_11_13 : HAL.UInt3 := 16#0#;\n   ADCPRE : Boolean := False;\n   PLLSRC : CFGR_PLLSRC_Field := 16#0#;\n   PLLXTPRE : Boolean := False;\n   PLLMUL : CFGR_PLLMUL_Field := 16#0#;\n   Reserved_22_23 : HAL.UInt2 := 16#0#;\n   MCO : CFGR_MCO_Field := 16#0#;\n   Reserved_27_27 : HAL.Bit := 16#0#;\n   MCOPRE : CFGR_MCOPRE_Field := 16#0#;\n   PLLNODIV : Boolean := False;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CIR_Register",
       qualified_name: "STM32_SVD.RCC.CIR_Register",
       signature: "stm32_svd.rcc.cir_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CIR_Register is record\n   LSIRDYF : Boolean := False;\n   LSERDYF : Boolean := False;\n   HSIRDYF : Boolean := False;\n   HSERDYF : Boolean := False;\n   PLLRDYF : Boolean := False;\n   HSI14RDYF : Boolean := False;\n   HSI48RDYF : Boolean := False;\n   CSSF : Boolean := False;\n   LSIRDYIE : Boolean := False;\n   LSERDYIE : Boolean := False;\n   HSIRDYIE : Boolean := False;\n   HSERDYIE : Boolean := False;\n   PLLRDYIE : Boolean := False;\n   HSI14RDYE : Boolean := False;\n   HSI48RDYIE : Boolean := False;\n   Reserved_15_15 : HAL.Bit := 16#0#;\n   LSIRDYC : Boolean := False;\n   LSERDYC : Boolean := False;\n   HSIRDYC : Boolean := False;\n   HSERDYC : Boolean := False;\n   PLLRDYC : Boolean := False;\n   HSI14RDYC : Boolean := False;\n   HSI48RDYC : Boolean := False;\n   CSSC : Boolean := False;\n   Reserved_24_31 : HAL.UInt8 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CR2_Register",
       qualified_name: "STM32_SVD.RCC.CR2_Register",
       signature: "stm32_svd.rcc.cr2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR2_Register is record\n   HSI14ON : Boolean := False;\n   HSI14RDY : Boolean := False;\n   HSI14DIS : Boolean := False;\n   HSI14TRIM : CR2_HSI14TRIM_Field := 16#10#;\n   HSI14CAL : CR2_HSI14CAL_Field := 16#0#;\n   HSI48ON : Boolean := False;\n   HSI48RDY : Boolean := False;\n   Reserved_18_23 : HAL.UInt6 := 16#0#;\n   HSI48CAL : Boolean := False;\n   Reserved_25_31 : HAL.UInt7 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.RCC.CR_Register",
       signature: "stm32_svd.rcc.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   HSION : Boolean := True;\n   HSIRDY : Boolean := True;\n   Reserved_2_2 : HAL.Bit := 16#0#;\n   HSITRIM : CR_HSITRIM_Field := 16#10#;\n   HSICAL : CR_HSICAL_Field := 16#0#;\n   HSEON : Boolean := False;\n   HSERDY : Boolean := False;\n   HSEBYP : Boolean := False;\n   CSSON : Boolean := False;\n   Reserved_20_23 : HAL.UInt4 := 16#0#;\n   PLLON : Boolean := False;\n   PLLRDY : Boolean := False;\n   Reserved_26_31 : HAL.UInt6 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CSR_Register",
       qualified_name: "STM32_SVD.RCC.CSR_Register",
       signature: "stm32_svd.rcc.csr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CSR_Register is record\n   LSION : Boolean := False;\n   LSIRDY : Boolean := False;\n   Reserved_2_23 : HAL.UInt22 := 16#0#;\n   RMVF : Boolean := False;\n   OBLRSTF : Boolean := False;\n   PINRSTF : Boolean := True;\n   PORRSTF : Boolean := True;\n   SFTRSTF : Boolean := False;\n   IWDGRSTF : Boolean := False;\n   WWDGRSTF : Boolean := False;\n   LPWRRSTF : Boolean := False;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "RCC_Peripheral",
       qualified_name: "STM32_SVD.RCC.RCC_Peripheral",
       signature: "stm32_svd.rcc.rcc_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RCC_Peripheral is record\n   CR : aliased CR_Register;\n   CFGR : aliased CFGR_Register;\n   CIR : aliased CIR_Register;\n   APB2RSTR : aliased APB2RSTR_Register;\n   APB1RSTR : aliased APB1RSTR_Register;\n   AHBENR : aliased AHBENR_Register;\n   APB2ENR : aliased APB2ENR_Register;\n   APB1ENR : aliased APB1ENR_Register;\n   BDCR : aliased BDCR_Register;\n   CSR : aliased CSR_Register;\n   AHBRSTR : aliased AHBRSTR_Register;\n   CFGR2 : aliased CFGR2_Register;\n   CFGR3 : aliased CFGR3_Register;\n   CR2 : aliased CR2_Register;\nend record with\n   Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "BDCR_LSEDRV_Field",
       qualified_name: "STM32_SVD.RCC.BDCR_LSEDRV_Field",
       signature: "stm32_svd.rcc.bdcr_lsedrv_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BDCR_LSEDRV_Field is HAL.UInt2;",
       }   ,
       {
       name: "BDCR_RTCSEL_Field",
       qualified_name: "STM32_SVD.RCC.BDCR_RTCSEL_Field",
       signature: "stm32_svd.rcc.bdcr_rtcsel_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BDCR_RTCSEL_Field is HAL.UInt2;",
       }   ,
       {
       name: "CFGR2_PREDIV_Field",
       qualified_name: "STM32_SVD.RCC.CFGR2_PREDIV_Field",
       signature: "stm32_svd.rcc.cfgr2_prediv_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR2_PREDIV_Field is HAL.UInt4;",
       }   ,
       {
       name: "CFGR3_USART1SW_Field",
       qualified_name: "STM32_SVD.RCC.CFGR3_USART1SW_Field",
       signature: "stm32_svd.rcc.cfgr3_usart1sw_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR3_USART1SW_Field is HAL.UInt2;",
       }   ,
       {
       name: "CFGR3_USART2SW_Field",
       qualified_name: "STM32_SVD.RCC.CFGR3_USART2SW_Field",
       signature: "stm32_svd.rcc.cfgr3_usart2sw_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR3_USART2SW_Field is HAL.UInt2;",
       }   ,
       {
       name: "CFGR_HPRE_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_HPRE_Field",
       signature: "stm32_svd.rcc.cfgr_hpre_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_HPRE_Field is HAL.UInt4;",
       }   ,
       {
       name: "CFGR_MCO_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_MCO_Field",
       signature: "stm32_svd.rcc.cfgr_mco_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_MCO_Field is HAL.UInt3;",
       }   ,
       {
       name: "CFGR_MCOPRE_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_MCOPRE_Field",
       signature: "stm32_svd.rcc.cfgr_mcopre_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_MCOPRE_Field is HAL.UInt3;",
       }   ,
       {
       name: "CFGR_PLLMUL_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_PLLMUL_Field",
       signature: "stm32_svd.rcc.cfgr_pllmul_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_PLLMUL_Field is HAL.UInt4;",
       }   ,
       {
       name: "CFGR_PLLSRC_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_PLLSRC_Field",
       signature: "stm32_svd.rcc.cfgr_pllsrc_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_PLLSRC_Field is HAL.UInt2;",
       }   ,
       {
       name: "CFGR_PPRE_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_PPRE_Field",
       signature: "stm32_svd.rcc.cfgr_ppre_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_PPRE_Field is HAL.UInt3;",
       }   ,
       {
       name: "CFGR_SW_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_SW_Field",
       signature: "stm32_svd.rcc.cfgr_sw_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_SW_Field is HAL.UInt2;",
       }   ,
       {
       name: "CFGR_SWS_Field",
       qualified_name: "STM32_SVD.RCC.CFGR_SWS_Field",
       signature: "stm32_svd.rcc.cfgr_sws_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CFGR_SWS_Field is HAL.UInt2;",
       }   ,
       {
       name: "CR2_HSI14CAL_Field",
       qualified_name: "STM32_SVD.RCC.CR2_HSI14CAL_Field",
       signature: "stm32_svd.rcc.cr2_hsi14cal_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR2_HSI14CAL_Field is HAL.UInt8;",
       }   ,
       {
       name: "CR2_HSI14TRIM_Field",
       qualified_name: "STM32_SVD.RCC.CR2_HSI14TRIM_Field",
       signature: "stm32_svd.rcc.cr2_hsi14trim_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR2_HSI14TRIM_Field is HAL.UInt5;",
       }   ,
       {
       name: "CR_HSICAL_Field",
       qualified_name: "STM32_SVD.RCC.CR_HSICAL_Field",
       signature: "stm32_svd.rcc.cr_hsical_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_HSICAL_Field is HAL.UInt8;",
       }   ,
       {
       name: "CR_HSITRIM_Field",
       qualified_name: "STM32_SVD.RCC.CR_HSITRIM_Field",
       signature: "stm32_svd.rcc.cr_hsitrim_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_HSITRIM_Field is HAL.UInt5;",
       }   ,
   ]
,variables:    [
       {
       name: "RCC_Periph",
       qualified_name: "STM32_SVD.RCC.RCC_Periph",
       signature: "stm32_svd.rcc.rcc_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RCC_Periph : aliased RCC_Peripheral with\n   Import,\n   Address => RCC_Base;",
       }   ,
   ]
,}
---