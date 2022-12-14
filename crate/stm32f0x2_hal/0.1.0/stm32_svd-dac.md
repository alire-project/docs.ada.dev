---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.DAC",
qualified_name: "STM32_SVD.DAC",
signature: "stm32_svd.dac",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "SWTRIGR_SWTRIG_Field_Array",
       qualified_name: "STM32_SVD.DAC.SWTRIGR_SWTRIG_Field_Array",
       signature: "stm32_svd.dac.swtrigr_swtrig_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWTRIGR_SWTRIG_Field_Array is array (1 .. 2) of Boolean with\n   Component_Size => 1,\n   Size           => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.DAC.CR_Register",
       signature: "stm32_svd.dac.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   EN1 : Boolean := False;\n   BOFF1 : Boolean := False;\n   TEN1 : Boolean := False;\n   TSEL1 : CR_TSEL1_Field := 16#0#;\n   WAVE1 : CR_WAVE1_Field := 16#0#;\n   MAMP1 : CR_MAMP1_Field := 16#0#;\n   DMAEN1 : Boolean := False;\n   DMAUDRIE1 : Boolean := False;\n   Reserved_14_15 : HAL.UInt2 := 16#0#;\n   EN2 : Boolean := False;\n   BOFF2 : Boolean := False;\n   TEN2 : Boolean := False;\n   TSEL2 : CR_TSEL2_Field := 16#0#;\n   WAVE2 : CR_WAVE2_Field := 16#0#;\n   MAMP2 : CR_MAMP2_Field := 16#0#;\n   DMAEN2 : Boolean := False;\n   DMAUDRIE2 : Boolean := False;\n   Reserved_30_31 : HAL.UInt2 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DAC_Peripheral",
       qualified_name: "STM32_SVD.DAC.DAC_Peripheral",
       signature: "stm32_svd.dac.dac_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DAC_Peripheral is record\n   CR : aliased CR_Register;\n   SWTRIGR : aliased SWTRIGR_Register;\n   DHR12R1 : aliased DHR12R1_Register;\n   DHR12L1 : aliased DHR12L1_Register;\n   DHR8R1 : aliased DHR8R1_Register;\n   DHR12R2 : aliased DHR12R2_Register;\n   DHR12L2 : aliased DHR12L2_Register;\n   DHR8R2 : aliased DHR8R2_Register;\n   DHR12RD : aliased DHR12RD_Register;\n   DHR12LD : aliased DHR12LD_Register;\n   DHR8RD : aliased DHR8RD_Register;\n   DOR1 : aliased DOR1_Register;\n   DOR2 : aliased DOR2_Register;\n   SR : aliased SR_Register;\nend record with\n   Volatile;",
       }   ,
       {
       name: "DHR12L1_Register",
       qualified_name: "STM32_SVD.DAC.DHR12L1_Register",
       signature: "stm32_svd.dac.dhr12l1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12L1_Register is record\n   Reserved_0_3 : HAL.UInt4 := 16#0#;\n   DACC1DHR : DHR12L1_DACC1DHR_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR12L2_Register",
       qualified_name: "STM32_SVD.DAC.DHR12L2_Register",
       signature: "stm32_svd.dac.dhr12l2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12L2_Register is record\n   Reserved_0_3 : HAL.UInt4 := 16#0#;\n   DACC2DHR : DHR12L2_DACC2DHR_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR12LD_Register",
       qualified_name: "STM32_SVD.DAC.DHR12LD_Register",
       signature: "stm32_svd.dac.dhr12ld_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12LD_Register is record\n   Reserved_0_3 : HAL.UInt4 := 16#0#;\n   DACC1DHR : DHR12LD_DACC1DHR_Field := 16#0#;\n   Reserved_16_19 : HAL.UInt4 := 16#0#;\n   DACC2DHR : DHR12LD_DACC2DHR_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR12R1_Register",
       qualified_name: "STM32_SVD.DAC.DHR12R1_Register",
       signature: "stm32_svd.dac.dhr12r1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12R1_Register is record\n   DACC1DHR : DHR12R1_DACC1DHR_Field := 16#0#;\n   Reserved_12_31 : HAL.UInt20 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR12R2_Register",
       qualified_name: "STM32_SVD.DAC.DHR12R2_Register",
       signature: "stm32_svd.dac.dhr12r2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12R2_Register is record\n   DACC2DHR : DHR12R2_DACC2DHR_Field := 16#0#;\n   Reserved_12_31 : HAL.UInt20 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR12RD_Register",
       qualified_name: "STM32_SVD.DAC.DHR12RD_Register",
       signature: "stm32_svd.dac.dhr12rd_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR12RD_Register is record\n   DACC1DHR : DHR12RD_DACC1DHR_Field := 16#0#;\n   Reserved_12_15 : HAL.UInt4 := 16#0#;\n   DACC2DHR : DHR12RD_DACC2DHR_Field := 16#0#;\n   Reserved_28_31 : HAL.UInt4 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR8R1_Register",
       qualified_name: "STM32_SVD.DAC.DHR8R1_Register",
       signature: "stm32_svd.dac.dhr8r1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR8R1_Register is record\n   DACC1DHR : DHR8R1_DACC1DHR_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR8R2_Register",
       qualified_name: "STM32_SVD.DAC.DHR8R2_Register",
       signature: "stm32_svd.dac.dhr8r2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR8R2_Register is record\n   DACC2DHR : DHR8R2_DACC2DHR_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DHR8RD_Register",
       qualified_name: "STM32_SVD.DAC.DHR8RD_Register",
       signature: "stm32_svd.dac.dhr8rd_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DHR8RD_Register is record\n   DACC1DHR : DHR8RD_DACC1DHR_Field := 16#0#;\n   DACC2DHR : DHR8RD_DACC2DHR_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DOR1_Register",
       qualified_name: "STM32_SVD.DAC.DOR1_Register",
       signature: "stm32_svd.dac.dor1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DOR1_Register is record\n   DACC1DOR : DOR1_DACC1DOR_Field;\n   Reserved_12_31 : HAL.UInt20;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DOR2_Register",
       qualified_name: "STM32_SVD.DAC.DOR2_Register",
       signature: "stm32_svd.dac.dor2_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DOR2_Register is record\n   DACC2DOR : DOR2_DACC2DOR_Field;\n   Reserved_12_31 : HAL.UInt20;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SR_Register",
       qualified_name: "STM32_SVD.DAC.SR_Register",
       signature: "stm32_svd.dac.sr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SR_Register is record\n   Reserved_0_12 : HAL.UInt13 := 16#0#;\n   DMAUDR1 : Boolean := False;\n   Reserved_14_28 : HAL.UInt15 := 16#0#;\n   DMAUDR2 : Boolean := False;\n   Reserved_30_31 : HAL.UInt2 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SWTRIGR_Register",
       qualified_name: "STM32_SVD.DAC.SWTRIGR_Register",
       signature: "stm32_svd.dac.swtrigr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWTRIGR_Register is record\n   SWTRIG : SWTRIGR_SWTRIG_Field := (As_Array => False, Val => 16#0#);\n   Reserved_2_31 : HAL.UInt30 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SWTRIGR_SWTRIG_Field",
       qualified_name: "STM32_SVD.DAC.SWTRIGR_SWTRIG_Field",
       signature: "stm32_svd.dac.swtrigr_swtrig_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWTRIGR_SWTRIG_Field (As_Array : Boolean := False) is record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt2;\n      when True =>\n         Arr : SWTRIGR_SWTRIG_Field_Array;\n   end case;\nend record with\n   Unchecked_Union,\n   Size => 2;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CR_MAMP1_Field",
       qualified_name: "STM32_SVD.DAC.CR_MAMP1_Field",
       signature: "stm32_svd.dac.cr_mamp1_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_MAMP1_Field is HAL.UInt4;",
       }   ,
       {
       name: "CR_MAMP2_Field",
       qualified_name: "STM32_SVD.DAC.CR_MAMP2_Field",
       signature: "stm32_svd.dac.cr_mamp2_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_MAMP2_Field is HAL.UInt4;",
       }   ,
       {
       name: "CR_TSEL1_Field",
       qualified_name: "STM32_SVD.DAC.CR_TSEL1_Field",
       signature: "stm32_svd.dac.cr_tsel1_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_TSEL1_Field is HAL.UInt3;",
       }   ,
       {
       name: "CR_TSEL2_Field",
       qualified_name: "STM32_SVD.DAC.CR_TSEL2_Field",
       signature: "stm32_svd.dac.cr_tsel2_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_TSEL2_Field is HAL.UInt3;",
       }   ,
       {
       name: "CR_WAVE1_Field",
       qualified_name: "STM32_SVD.DAC.CR_WAVE1_Field",
       signature: "stm32_svd.dac.cr_wave1_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_WAVE1_Field is HAL.UInt2;",
       }   ,
       {
       name: "CR_WAVE2_Field",
       qualified_name: "STM32_SVD.DAC.CR_WAVE2_Field",
       signature: "stm32_svd.dac.cr_wave2_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_WAVE2_Field is HAL.UInt2;",
       }   ,
       {
       name: "DHR12L1_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12L1_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr12l1_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12L1_DACC1DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12L2_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12L2_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr12l2_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12L2_DACC2DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12LD_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12LD_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr12ld_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12LD_DACC1DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12LD_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12LD_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr12ld_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12LD_DACC2DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12R1_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12R1_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr12r1_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12R1_DACC1DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12R2_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12R2_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr12r2_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12R2_DACC2DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12RD_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12RD_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr12rd_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12RD_DACC1DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR12RD_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR12RD_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr12rd_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR12RD_DACC2DHR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DHR8R1_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR8R1_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr8r1_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR8R1_DACC1DHR_Field is HAL.UInt8;",
       }   ,
       {
       name: "DHR8R2_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR8R2_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr8r2_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR8R2_DACC2DHR_Field is HAL.UInt8;",
       }   ,
       {
       name: "DHR8RD_DACC1DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR8RD_DACC1DHR_Field",
       signature: "stm32_svd.dac.dhr8rd_dacc1dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR8RD_DACC1DHR_Field is HAL.UInt8;",
       }   ,
       {
       name: "DHR8RD_DACC2DHR_Field",
       qualified_name: "STM32_SVD.DAC.DHR8RD_DACC2DHR_Field",
       signature: "stm32_svd.dac.dhr8rd_dacc2dhr_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DHR8RD_DACC2DHR_Field is HAL.UInt8;",
       }   ,
       {
       name: "DOR1_DACC1DOR_Field",
       qualified_name: "STM32_SVD.DAC.DOR1_DACC1DOR_Field",
       signature: "stm32_svd.dac.dor1_dacc1dor_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DOR1_DACC1DOR_Field is HAL.UInt12;",
       }   ,
       {
       name: "DOR2_DACC2DOR_Field",
       qualified_name: "STM32_SVD.DAC.DOR2_DACC2DOR_Field",
       signature: "stm32_svd.dac.dor2_dacc2dor_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DOR2_DACC2DOR_Field is HAL.UInt12;",
       }   ,
   ]
,variables:    [
       {
       name: "DAC_Periph",
       qualified_name: "STM32_SVD.DAC.DAC_Periph",
       signature: "stm32_svd.dac.dac_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DAC_Periph : aliased DAC_Peripheral with\n   Import,\n   Address => DAC_Base;",
       }   ,
   ]
,}
---
