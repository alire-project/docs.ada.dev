---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.DMA",
qualified_name: "STM32_SVD.DMA",
signature: "stm32_svd.dma",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CCR_Register",
       qualified_name: "STM32_SVD.DMA.CCR_Register",
       signature: "stm32_svd.dma.ccr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CCR_Register is record\n   EN : Boolean := False;\n   TCIE : Boolean := False;\n   HTIE : Boolean := False;\n   TEIE : Boolean := False;\n   DIR : Boolean := False;\n   CIRC : Boolean := False;\n   PINC : Boolean := False;\n   MINC : Boolean := False;\n   PSIZE : CCR_PSIZE_Field := 16#0#;\n   MSIZE : CCR_MSIZE_Field := 16#0#;\n   PL : CCR_PL_Field := 16#0#;\n   MEM2MEM : Boolean := False;\n   Reserved_15_31 : HAL.UInt17 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CNDTR_Register",
       qualified_name: "STM32_SVD.DMA.CNDTR_Register",
       signature: "stm32_svd.dma.cndtr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CNDTR_Register is record\n   NDT : CNDTR_NDT_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "DMA1_Peripheral",
       qualified_name: "STM32_SVD.DMA.DMA1_Peripheral",
       signature: "stm32_svd.dma.dma1_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMA1_Peripheral is record\n   ISR : aliased ISR_Register;\n   IFCR : aliased IFCR_Register;\n   CCR1 : aliased CCR_Register;\n   CNDTR1 : aliased CNDTR_Register;\n   CPAR1 : aliased HAL.UInt32;\n   CMAR1 : aliased HAL.UInt32;\n   CCR2 : aliased CCR_Register;\n   CNDTR2 : aliased CNDTR_Register;\n   CPAR2 : aliased HAL.UInt32;\n   CMAR2 : aliased HAL.UInt32;\n   CCR3 : aliased CCR_Register;\n   CNDTR3 : aliased CNDTR_Register;\n   CPAR3 : aliased HAL.UInt32;\n   CMAR3 : aliased HAL.UInt32;\n   CCR4 : aliased CCR_Register;\n   CNDTR4 : aliased CNDTR_Register;\n   CPAR4 : aliased HAL.UInt32;\n   CMAR4 : aliased HAL.UInt32;\n   CCR5 : aliased CCR_Register;\n   CNDTR5 : aliased CNDTR_Register;\n   CPAR5 : aliased HAL.UInt32;\n   CMAR5 : aliased HAL.UInt32;\n   CCR6 : aliased CCR_Register;\n   CNDTR6 : aliased CNDTR_Register;\n   CPAR6 : aliased HAL.UInt32;\n   CMAR6 : aliased HAL.UInt32;\n   CCR7 : aliased CCR_Register;\n   CNDTR7 : aliased CNDTR_Register;\n   CPAR7 : aliased HAL.UInt32;\n   CMAR7 : aliased HAL.UInt32;\nend record with\n   Volatile;",
       }   ,
       {
       name: "IFCR_Register",
       qualified_name: "STM32_SVD.DMA.IFCR_Register",
       signature: "stm32_svd.dma.ifcr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IFCR_Register is record\n   CGIF1 : Boolean := False;\n   CTCIF1 : Boolean := False;\n   CHTIF1 : Boolean := False;\n   CTEIF1 : Boolean := False;\n   CGIF2 : Boolean := False;\n   CTCIF2 : Boolean := False;\n   CHTIF2 : Boolean := False;\n   CTEIF2 : Boolean := False;\n   CGIF3 : Boolean := False;\n   CTCIF3 : Boolean := False;\n   CHTIF3 : Boolean := False;\n   CTEIF3 : Boolean := False;\n   CGIF4 : Boolean := False;\n   CTCIF4 : Boolean := False;\n   CHTIF4 : Boolean := False;\n   CTEIF4 : Boolean := False;\n   CGIF5 : Boolean := False;\n   CTCIF5 : Boolean := False;\n   CHTIF5 : Boolean := False;\n   CTEIF5 : Boolean := False;\n   CGIF6 : Boolean := False;\n   CTCIF6 : Boolean := False;\n   CHTIF6 : Boolean := False;\n   CTEIF6 : Boolean := False;\n   CGIF7 : Boolean := False;\n   CTCIF7 : Boolean := False;\n   CHTIF7 : Boolean := False;\n   CTEIF7 : Boolean := False;\n   Reserved_28_31 : HAL.UInt4 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "ISR_Register",
       qualified_name: "STM32_SVD.DMA.ISR_Register",
       signature: "stm32_svd.dma.isr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ISR_Register is record\n   GIF1 : Boolean;\n   TCIF1 : Boolean;\n   HTIF1 : Boolean;\n   TEIF1 : Boolean;\n   GIF2 : Boolean;\n   TCIF2 : Boolean;\n   HTIF2 : Boolean;\n   TEIF2 : Boolean;\n   GIF3 : Boolean;\n   TCIF3 : Boolean;\n   HTIF3 : Boolean;\n   TEIF3 : Boolean;\n   GIF4 : Boolean;\n   TCIF4 : Boolean;\n   HTIF4 : Boolean;\n   TEIF4 : Boolean;\n   GIF5 : Boolean;\n   TCIF5 : Boolean;\n   HTIF5 : Boolean;\n   TEIF5 : Boolean;\n   GIF6 : Boolean;\n   TCIF6 : Boolean;\n   HTIF6 : Boolean;\n   TEIF6 : Boolean;\n   GIF7 : Boolean;\n   TCIF7 : Boolean;\n   HTIF7 : Boolean;\n   TEIF7 : Boolean;\n   Reserved_28_31 : HAL.UInt4;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CCR_MSIZE_Field",
       qualified_name: "STM32_SVD.DMA.CCR_MSIZE_Field",
       signature: "stm32_svd.dma.ccr_msize_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CCR_MSIZE_Field is HAL.UInt2;",
       }   ,
       {
       name: "CCR_PL_Field",
       qualified_name: "STM32_SVD.DMA.CCR_PL_Field",
       signature: "stm32_svd.dma.ccr_pl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CCR_PL_Field is HAL.UInt2;",
       }   ,
       {
       name: "CCR_PSIZE_Field",
       qualified_name: "STM32_SVD.DMA.CCR_PSIZE_Field",
       signature: "stm32_svd.dma.ccr_psize_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CCR_PSIZE_Field is HAL.UInt2;",
       }   ,
       {
       name: "CNDTR_NDT_Field",
       qualified_name: "STM32_SVD.DMA.CNDTR_NDT_Field",
       signature: "stm32_svd.dma.cndtr_ndt_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CNDTR_NDT_Field is HAL.UInt16;",
       }   ,
   ]
,variables:    [
       {
       name: "DMA1_Periph",
       qualified_name: "STM32_SVD.DMA.DMA1_Periph",
       signature: "stm32_svd.dma.dma1_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DMA1_Periph : aliased DMA1_Peripheral with\n   Import,\n   Address => DMA1_Base;",
       }   ,
   ]
,}
---
