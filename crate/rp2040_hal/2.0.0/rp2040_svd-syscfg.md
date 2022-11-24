---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.SYSCFG",
qualified_name: "RP2040_SVD.SYSCFG",
signature: "rp2040_svd.syscfg",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
array_types:    [
       {
       name: "MEMPOWERDOWN_SRAM_Field_Array",
       qualified_name: "RP2040_SVD.SYSCFG.MEMPOWERDOWN_SRAM_Field_Array",
       signature: "rp2040_svd.syscfg.mempowerdown_sram_field_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MEMPOWERDOWN_SRAM_Field_Array is array (0 .. 5) of Boolean\n  with Component_Size => 1, Size => 6;",
       }   ,
   ]
,record_types:    [
       {
       name: "DBGFORCE_Register",
       qualified_name: "RP2040_SVD.SYSCFG.DBGFORCE_Register",
       signature: "rp2040_svd.syscfg.dbgforce_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DBGFORCE_Register is record\n   PROC0_SWDO    : Boolean := False;\n   PROC0_SWDI    : Boolean := True;\n   PROC0_SWCLK   : Boolean := True;\n   PROC0_ATTACH  : Boolean := False;\n   PROC1_SWDO    : Boolean := False;\n   PROC1_SWDI    : Boolean := True;\n   PROC1_SWCLK   : Boolean := True;\n   PROC1_ATTACH  : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "MEMPOWERDOWN_Register",
       qualified_name: "RP2040_SVD.SYSCFG.MEMPOWERDOWN_Register",
       signature: "rp2040_svd.syscfg.mempowerdown_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MEMPOWERDOWN_Register is record\n   SRAM          : MEMPOWERDOWN_SRAM_Field :=\n                    (As_Array => False, Val => 16#0#);\n   USB           : Boolean := False;\n   ROM           : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "MEMPOWERDOWN_SRAM_Field",
       qualified_name: "RP2040_SVD.SYSCFG.MEMPOWERDOWN_SRAM_Field",
       signature: "rp2040_svd.syscfg.mempowerdown_sram_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MEMPOWERDOWN_SRAM_Field\n  (As_Array : Boolean := False)\nis record\n   case As_Array is\n      when False =>\n         Val : HAL.UInt6;\n      when True =>\n         Arr : MEMPOWERDOWN_SRAM_Field_Array;\n   end case;\nend record\n  with Unchecked_Union, Size => 6;",
       }   ,
       {
       name: "PROC_CONFIG_Register",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_CONFIG_Register",
       signature: "rp2040_svd.syscfg.proc_config_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PROC_CONFIG_Register is record\n   PROC0_HALTED     : Boolean := False;\n   PROC1_HALTED     : Boolean := False;\n   Reserved_2_23    : HAL.UInt22 := 16#0#;\n   PROC0_DAP_INSTID : PROC_CONFIG_PROC0_DAP_INSTID_Field := 16#0#;\n   PROC1_DAP_INSTID : PROC_CONFIG_PROC1_DAP_INSTID_Field := 16#1#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PROC_IN_SYNC_BYPASS_HI_Register",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_IN_SYNC_BYPASS_HI_Register",
       signature: "rp2040_svd.syscfg.proc_in_sync_bypass_hi_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PROC_IN_SYNC_BYPASS_HI_Register is record\n   PROC_IN_SYNC_BYPASS_HI : PROC_IN_SYNC_BYPASS_HI_PROC_IN_SYNC_BYPASS_HI_Field :=\n                             16#0#;\n   Reserved_6_31          : HAL.UInt26 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PROC_IN_SYNC_BYPASS_Register",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_IN_SYNC_BYPASS_Register",
       signature: "rp2040_svd.syscfg.proc_in_sync_bypass_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PROC_IN_SYNC_BYPASS_Register is record\n   PROC_IN_SYNC_BYPASS : PROC_IN_SYNC_BYPASS_PROC_IN_SYNC_BYPASS_Field :=\n                          16#0#;\n   Reserved_30_31      : HAL.UInt2 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SYSCFG_Peripheral",
       qualified_name: "RP2040_SVD.SYSCFG.SYSCFG_Peripheral",
       signature: "rp2040_svd.syscfg.syscfg_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SYSCFG_Peripheral is record\n   PROC0_NMI_MASK         : aliased HAL.UInt32;\n   PROC1_NMI_MASK         : aliased HAL.UInt32;\n   PROC_CONFIG            : aliased PROC_CONFIG_Register;\n   PROC_IN_SYNC_BYPASS    : aliased PROC_IN_SYNC_BYPASS_Register;\n   PROC_IN_SYNC_BYPASS_HI : aliased PROC_IN_SYNC_BYPASS_HI_Register;\n   DBGFORCE               : aliased DBGFORCE_Register;\n   MEMPOWERDOWN           : aliased MEMPOWERDOWN_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "PROC_CONFIG_PROC0_DAP_INSTID_Field",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_CONFIG_PROC0_DAP_INSTID_Field",
       signature: "rp2040_svd.syscfg.proc_config_proc0_dap_instid_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PROC_CONFIG_PROC0_DAP_INSTID_Field is HAL.UInt4;",
       }   ,
       {
       name: "PROC_CONFIG_PROC1_DAP_INSTID_Field",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_CONFIG_PROC1_DAP_INSTID_Field",
       signature: "rp2040_svd.syscfg.proc_config_proc1_dap_instid_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PROC_CONFIG_PROC1_DAP_INSTID_Field is HAL.UInt4;",
       }   ,
       {
       name: "PROC_IN_SYNC_BYPASS_HI_PROC_IN_SYNC_BYPASS_HI_Field",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_IN_SYNC_BYPASS_HI_PROC_IN_SYNC_BYPASS_HI_Field",
       signature: "rp2040_svd.syscfg.proc_in_sync_bypass_hi_proc_in_sync_bypass_hi_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PROC_IN_SYNC_BYPASS_HI_PROC_IN_SYNC_BYPASS_HI_Field is HAL.UInt6;",
       }   ,
       {
       name: "PROC_IN_SYNC_BYPASS_PROC_IN_SYNC_BYPASS_Field",
       qualified_name: "RP2040_SVD.SYSCFG.PROC_IN_SYNC_BYPASS_PROC_IN_SYNC_BYPASS_Field",
       signature: "rp2040_svd.syscfg.proc_in_sync_bypass_proc_in_sync_bypass_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PROC_IN_SYNC_BYPASS_PROC_IN_SYNC_BYPASS_Field is HAL.UInt30;",
       }   ,
   ]
,variables:    [
       {
       name: "SYSCFG_Periph",
       qualified_name: "RP2040_SVD.SYSCFG.SYSCFG_Periph",
       signature: "rp2040_svd.syscfg.syscfg_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SYSCFG_Periph : aliased SYSCFG_Peripheral\n  with Import, Address => SYSCFG_Base;",
       }   ,
   ]
,}
---
