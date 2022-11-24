---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32_SVD.PWR",
qualified_name: "STM32_SVD.PWR",
signature: "stm32_svd.pwr",
enclosing: "stm32_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "CSR_EWUP_Field_Array",
       qualified_name: "STM32_SVD.PWR.CSR_EWUP_Field_Array",
       signature: "stm32_svd.pwr.csr_ewup_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CSR_EWUP_Field_Array is array (1 .. 8) of Boolean with\n   Component_Size => 1,\n   Size           => 8;",
       }   ,
   ]
,record_types:    [
       {
       name: "CR_Register",
       qualified_name: "STM32_SVD.PWR.CR_Register",
       signature: "stm32_svd.pwr.cr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CR_Register is record\n   LPDS : Boolean := False;\n   PDDS : Boolean := False;\n   CWUF : Boolean := False;\n   CSBF : Boolean := False;\n   PVDE : Boolean := False;\n   PLS : CR_PLS_Field := 16#0#;\n   DBP : Boolean := False;\n   Reserved_9_31 : HAL.UInt23 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "CSR_EWUP_Field",
       qualified_name: "STM32_SVD.PWR.CSR_EWUP_Field",
       signature: "stm32_svd.pwr.csr_ewup_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CSR_EWUP_Field (As_Array : Boolean := False) is record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt8;\n      when True =>\n         Arr : CSR_EWUP_Field_Array;\n   end case;\nend record with\n   Unchecked_Union,\n   Size => 8;",
       }   ,
       {
       name: "CSR_Register",
       qualified_name: "STM32_SVD.PWR.CSR_Register",
       signature: "stm32_svd.pwr.csr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CSR_Register is record\n   WUF : Boolean := False;\n   SBF : Boolean := False;\n   PVDO : Boolean := False;\n   VREFINTRDY : Boolean := False;\n   Reserved_4_7 : HAL.UInt4 := 16#0#;\n   EWUP : CSR_EWUP_Field := (As_Array => False, Val => 16#0#);\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 32,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "PWR_Peripheral",
       qualified_name: "STM32_SVD.PWR.PWR_Peripheral",
       signature: "stm32_svd.pwr.pwr_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWR_Peripheral is record\n   CR : aliased CR_Register;\n   CSR : aliased CSR_Register;\nend record with\n   Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CR_PLS_Field",
       qualified_name: "STM32_SVD.PWR.CR_PLS_Field",
       signature: "stm32_svd.pwr.cr_pls_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CR_PLS_Field is HAL.UInt3;",
       }   ,
   ]
,variables:    [
       {
       name: "PWR_Periph",
       qualified_name: "STM32_SVD.PWR.PWR_Periph",
       signature: "stm32_svd.pwr.pwr_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PWR_Periph : aliased PWR_Peripheral with\n   Import,\n   Address => PWR_Base;",
       }   ,
   ]
,}
---
