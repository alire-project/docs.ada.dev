---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.Flash",
qualified_name: "STM32_SVD.Flash",
signature: "stm32_svd.flash",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "OBR_Data_Field_Array",
       qualified_name: "STM32_SVD.Flash.OBR_Data_Field_Array",
       signature: "stm32_svd.flash.obr_data_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OBR_Data_Field_Array is array (0 .. 1) of OBR_Data_Element with\n   Component_Size => 8,\n   Size           => 16;",
       }   ,
       {
       name: "OBR_nBOOT_Field_Array",
       qualified_name: "STM32_SVD.Flash.OBR_nBOOT_Field_Array",
       signature: "stm32_svd.flash.obr_nboot_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OBR_nBOOT_Field_Array is array (0 .. 1) of Boolean with\n   Component_Size => 1,\n   Size           => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "ACR_Register",
       qualified_name: "STM32_SVD.Flash.ACR_Register",
       signature: "stm32_svd.flash.acr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ACR_Register is record\n   LATENCY : ACR_LATENCY_Field := 16#0#;\n   Reserved_3_3 : HAL.Bit := 16#0#;\n   PRFTBE : Boolean := True;\n   PRFTBS : Boolean := True;\n   Reserved_6_31 : HAL.UInt26 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.Flash.CR_Register",
       signature: "stm32_svd.flash.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   PG : Boolean := False;\n   PER : Boolean := False;\n   MER : Boolean := False;\n   Reserved_3_3 : HAL.Bit := 16#0#;\n   OPTPG : Boolean := False;\n   OPTER : Boolean := False;\n   STRT : Boolean := False;\n   LOCK : Boolean := True;\n   Reserved_8_8 : HAL.Bit := 16#0#;\n   OPTWRE : Boolean := False;\n   ERRIE : Boolean := False;\n   Reserved_11_11 : HAL.Bit := 16#0#;\n   EOPIE : Boolean := False;\n   FORCE_OPTLOAD : Boolean := False;\n   Reserved_14_31 : HAL.UInt18 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "Flash_Peripheral",
       qualified_name: "STM32_SVD.Flash.Flash_Peripheral",
       signature: "stm32_svd.flash.flash_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flash_Peripheral is record\n   ACR : aliased ACR_Register;\n   KEYR : aliased HAL.UInt32;\n   OPTKEYR : aliased HAL.UInt32;\n   SR : aliased SR_Register;\n   CR : aliased CR_Register;\n   AR : aliased HAL.UInt32;\n   OBR : aliased OBR_Register;\n   WRPR : aliased HAL.UInt32;\nend record with\n   Volatile;",
       }   ,
       {
       name: "OBR_Data_Field",
       qualified_name: "STM32_SVD.Flash.OBR_Data_Field",
       signature: "stm32_svd.flash.obr_data_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OBR_Data_Field (As_Array : Boolean := False) is record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt16;\n      when True =>\n         Arr : OBR_Data_Field_Array;\n   end case;\nend record with\n   Unchecked_Union,\n   Size => 16;",
       }   ,
       {
       name: "OBR_nBOOT_Field",
       qualified_name: "STM32_SVD.Flash.OBR_nBOOT_Field",
       signature: "stm32_svd.flash.obr_nboot_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OBR_nBOOT_Field (As_Array : Boolean := False) is record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt2;\n      when True =>\n         Arr : OBR_nBOOT_Field_Array;\n   end case;\nend record with\n   Unchecked_Union,\n   Size => 2;",
       }   ,
       {
       name: "OBR_Register",
       qualified_name: "STM32_SVD.Flash.OBR_Register",
       signature: "stm32_svd.flash.obr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OBR_Register is record\n   OPTERR : Boolean;\n   RDPRT : OBR_RDPRT_Field;\n   Reserved_3_7 : HAL.UInt5;\n   WDG_SW : Boolean;\n   nRST_STOP : Boolean;\n   nRST_STDBY : Boolean;\n   nBOOT : OBR_nBOOT_Field;\n   VDDA_MONITOR : Boolean;\n   RAM_PARITY_CHECK : Boolean;\n   BOOT_SEL : Boolean;\n   Data : OBR_Data_Field;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "SR_Register",
       qualified_name: "STM32_SVD.Flash.SR_Register",
       signature: "stm32_svd.flash.sr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SR_Register is record\n   BSY : Boolean := False;\n   Reserved_1_1 : HAL.Bit := 16#0#;\n   PGERR : Boolean := False;\n   Reserved_3_3 : HAL.Bit := 16#0#;\n   WRPRT : Boolean := False;\n   EOP : Boolean := False;\n   Reserved_6_31 : HAL.UInt26 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ACR_LATENCY_Field",
       qualified_name: "STM32_SVD.Flash.ACR_LATENCY_Field",
       signature: "stm32_svd.flash.acr_latency_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ACR_LATENCY_Field is HAL.UInt3;",
       }   ,
       {
       name: "OBR_Data_Element",
       qualified_name: "STM32_SVD.Flash.OBR_Data_Element",
       signature: "stm32_svd.flash.obr_data_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype OBR_Data_Element is HAL.UInt8;",
       }   ,
       {
       name: "OBR_RDPRT_Field",
       qualified_name: "STM32_SVD.Flash.OBR_RDPRT_Field",
       signature: "stm32_svd.flash.obr_rdprt_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype OBR_RDPRT_Field is HAL.UInt2;",
       }   ,
   ]
,variables:    [
       {
       name: "Flash_Periph",
       qualified_name: "STM32_SVD.Flash.Flash_Periph",
       signature: "stm32_svd.flash.flash_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Flash_Periph : aliased Flash_Peripheral with\n   Import,\n   Address => Flash_Base;",
       }   ,
   ]
,}
---
