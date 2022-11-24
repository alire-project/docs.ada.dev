---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.TBMAN",
qualified_name: "RP2040_SVD.TBMAN",
signature: "rp2040_svd.tbman",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "PLATFORM_Register",
       qualified_name: "RP2040_SVD.TBMAN.PLATFORM_Register",
       signature: "rp2040_svd.tbman.platform_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PLATFORM_Register is record\n   ASIC          : Boolean;\n   FPGA          : Boolean;\n   Reserved_2_31 : HAL.UInt30;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TBMAN_Peripheral",
       qualified_name: "RP2040_SVD.TBMAN.TBMAN_Peripheral",
       signature: "rp2040_svd.tbman.tbman_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TBMAN_Peripheral is record\n   PLATFORM : aliased PLATFORM_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,variables:    [
       {
       name: "TBMAN_Periph",
       qualified_name: "RP2040_SVD.TBMAN.TBMAN_Periph",
       signature: "rp2040_svd.tbman.tbman_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TBMAN_Periph : aliased TBMAN_Peripheral\n  with Import, Address => TBMAN_Base;",
       }   ,
   ]
,}
---
