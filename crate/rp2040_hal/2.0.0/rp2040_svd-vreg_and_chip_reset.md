---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.VREG_AND_CHIP_RESET",
qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET",
signature: "rp2040_svd.vreg_and_chip_reset",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "BOD_Register",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.BOD_Register",
       signature: "rp2040_svd.vreg_and_chip_reset.bod_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BOD_Register is record\n   EN            : Boolean := True;\n   Reserved_1_3  : HAL.UInt3 := 16#0#;\n   VSEL          : BOD_VSEL_Field := 16#9#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "CHIP_RESET_Register",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.CHIP_RESET_Register",
       signature: "rp2040_svd.vreg_and_chip_reset.chip_reset_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CHIP_RESET_Register is record\n   Reserved_0_7     : HAL.UInt8 := 16#0#;\n   HAD_POR          : Boolean := False;\n   Reserved_9_15    : HAL.UInt7 := 16#0#;\n   HAD_RUN          : Boolean := False;\n   Reserved_17_19   : HAL.UInt3 := 16#0#;\n   HAD_PSM_RESTART  : Boolean := False;\n   Reserved_21_23   : HAL.UInt3 := 16#0#;\n   PSM_RESTART_FLAG : Boolean := False;\n   Reserved_25_31   : HAL.UInt7 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "VREG_AND_CHIP_RESET_Peripheral",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.VREG_AND_CHIP_RESET_Peripheral",
       signature: "rp2040_svd.vreg_and_chip_reset.vreg_and_chip_reset_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VREG_AND_CHIP_RESET_Peripheral is record\n   VREG       : aliased VREG_Register;\n   BOD        : aliased BOD_Register;\n   CHIP_RESET : aliased CHIP_RESET_Register;\nend record\n  with Volatile;",
       }   ,
       {
       name: "VREG_Register",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.VREG_Register",
       signature: "rp2040_svd.vreg_and_chip_reset.vreg_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VREG_Register is record\n   EN             : Boolean := True;\n   HIZ            : Boolean := False;\n   Reserved_2_3   : HAL.UInt2 := 16#0#;\n   VSEL           : VREG_VSEL_Field := 16#B#;\n   Reserved_8_11  : HAL.UInt4 := 16#0#;\n   ROK            : Boolean := False;\n   Reserved_13_31 : HAL.UInt19 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "BOD_VSEL_Field",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.BOD_VSEL_Field",
       signature: "rp2040_svd.vreg_and_chip_reset.bod_vsel_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BOD_VSEL_Field is HAL.UInt4;",
       }   ,
       {
       name: "VREG_VSEL_Field",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.VREG_VSEL_Field",
       signature: "rp2040_svd.vreg_and_chip_reset.vreg_vsel_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype VREG_VSEL_Field is HAL.UInt4;",
       }   ,
   ]
,variables:    [
       {
       name: "VREG_AND_CHIP_RESET_Periph",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET.VREG_AND_CHIP_RESET_Periph",
       signature: "rp2040_svd.vreg_and_chip_reset.vreg_and_chip_reset_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "VREG_AND_CHIP_RESET_Periph : aliased VREG_AND_CHIP_RESET_Peripheral\n  with Import, Address => VREG_AND_CHIP_RESET_Base;",
       }   ,
   ]
,}
---
