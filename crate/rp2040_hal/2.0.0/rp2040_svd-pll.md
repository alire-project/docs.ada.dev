---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.PLL",
qualified_name: "RP2040_SVD.PLL",
signature: "rp2040_svd.pll",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CS_Register",
       qualified_name: "RP2040_SVD.PLL.CS_Register",
       signature: "rp2040_svd.pll.cs_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CS_Register is record\n   REFDIV        : CS_REFDIV_Field := 16#1#;\n   Reserved_6_7  : HAL.UInt2 := 16#0#;\n   BYPASS        : Boolean := False;\n   Reserved_9_30 : HAL.UInt22 := 16#0#;\n   LOCK          : Boolean := False;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "FBDIV_INT_Register",
       qualified_name: "RP2040_SVD.PLL.FBDIV_INT_Register",
       signature: "rp2040_svd.pll.fbdiv_int_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type FBDIV_INT_Register is record\n   FBDIV_INT      : FBDIV_INT_FBDIV_INT_Field := 16#0#;\n   Reserved_12_31 : HAL.UInt20 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PLL_Peripheral",
       qualified_name: "RP2040_SVD.PLL.PLL_Peripheral",
       signature: "rp2040_svd.pll.pll_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PLL_Peripheral is record\n   CS        : aliased CS_Register;\n   PWR       : aliased PWR_Register;\n   FBDIV_INT : aliased FBDIV_INT_Register;\n   PRIM      : aliased PRIM_Register;\nend record\n  with Volatile;",
       }   ,
       {
       name: "PRIM_Register",
       qualified_name: "RP2040_SVD.PLL.PRIM_Register",
       signature: "rp2040_svd.pll.prim_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PRIM_Register is record\n   Reserved_0_11  : HAL.UInt12 := 16#0#;\n   POSTDIV2       : PRIM_POSTDIV2_Field := 16#7#;\n   Reserved_15_15 : HAL.Bit := 16#0#;\n   POSTDIV1       : PRIM_POSTDIV1_Field := 16#7#;\n   Reserved_19_31 : HAL.UInt13 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PWR_Register",
       qualified_name: "RP2040_SVD.PLL.PWR_Register",
       signature: "rp2040_svd.pll.pwr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PWR_Register is record\n   PD            : Boolean := True;\n   Reserved_1_1  : HAL.Bit := 16#0#;\n   DSMPD         : Boolean := True;\n   POSTDIVPD     : Boolean := True;\n   Reserved_4_4  : HAL.Bit := 16#0#;\n   VCOPD         : Boolean := True;\n   Reserved_6_31 : HAL.UInt26 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CS_REFDIV_Field",
       qualified_name: "RP2040_SVD.PLL.CS_REFDIV_Field",
       signature: "rp2040_svd.pll.cs_refdiv_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CS_REFDIV_Field is HAL.UInt6;",
       }   ,
       {
       name: "FBDIV_INT_FBDIV_INT_Field",
       qualified_name: "RP2040_SVD.PLL.FBDIV_INT_FBDIV_INT_Field",
       signature: "rp2040_svd.pll.fbdiv_int_fbdiv_int_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype FBDIV_INT_FBDIV_INT_Field is HAL.UInt12;",
       }   ,
       {
       name: "PRIM_POSTDIV1_Field",
       qualified_name: "RP2040_SVD.PLL.PRIM_POSTDIV1_Field",
       signature: "rp2040_svd.pll.prim_postdiv1_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PRIM_POSTDIV1_Field is HAL.UInt3;",
       }   ,
       {
       name: "PRIM_POSTDIV2_Field",
       qualified_name: "RP2040_SVD.PLL.PRIM_POSTDIV2_Field",
       signature: "rp2040_svd.pll.prim_postdiv2_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype PRIM_POSTDIV2_Field is HAL.UInt3;",
       }   ,
   ]
,variables:    [
       {
       name: "PLL_SYS_Periph",
       qualified_name: "RP2040_SVD.PLL.PLL_SYS_Periph",
       signature: "rp2040_svd.pll.pll_sys_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_SYS_Periph : aliased PLL_Peripheral\n  with Import, Address => PLL_SYS_Base;",
       }   ,
       {
       name: "PLL_USB_Periph",
       qualified_name: "RP2040_SVD.PLL.PLL_USB_Periph",
       signature: "rp2040_svd.pll.pll_usb_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_USB_Periph : aliased PLL_Peripheral\n  with Import, Address => PLL_USB_Base;",
       }   ,
   ]
,}
---
