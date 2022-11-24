---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.SYSINFO",
qualified_name: "RP2040_SVD.SYSINFO",
signature: "rp2040_svd.sysinfo",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
record_types:    [
       {
       name: "CHIP_ID_Register",
       qualified_name: "RP2040_SVD.SYSINFO.CHIP_ID_Register",
       signature: "rp2040_svd.sysinfo.chip_id_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CHIP_ID_Register is record\n   MANUFACTURER : CHIP_ID_MANUFACTURER_Field;\n   PART         : CHIP_ID_PART_Field;\n   REVISION     : CHIP_ID_REVISION_Field;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PLATFORM_Register",
       qualified_name: "RP2040_SVD.SYSINFO.PLATFORM_Register",
       signature: "rp2040_svd.sysinfo.platform_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PLATFORM_Register is record\n   FPGA          : Boolean;\n   ASIC          : Boolean;\n   Reserved_2_31 : HAL.UInt30;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SYSINFO_Peripheral",
       qualified_name: "RP2040_SVD.SYSINFO.SYSINFO_Peripheral",
       signature: "rp2040_svd.sysinfo.sysinfo_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SYSINFO_Peripheral is record\n   CHIP_ID       : aliased CHIP_ID_Register;\n   PLATFORM      : aliased PLATFORM_Register;\n   GITREF_RP2040 : aliased HAL.UInt32;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "CHIP_ID_MANUFACTURER_Field",
       qualified_name: "RP2040_SVD.SYSINFO.CHIP_ID_MANUFACTURER_Field",
       signature: "rp2040_svd.sysinfo.chip_id_manufacturer_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CHIP_ID_MANUFACTURER_Field is HAL.UInt12;",
       }   ,
       {
       name: "CHIP_ID_PART_Field",
       qualified_name: "RP2040_SVD.SYSINFO.CHIP_ID_PART_Field",
       signature: "rp2040_svd.sysinfo.chip_id_part_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CHIP_ID_PART_Field is HAL.UInt16;",
       }   ,
       {
       name: "CHIP_ID_REVISION_Field",
       qualified_name: "RP2040_SVD.SYSINFO.CHIP_ID_REVISION_Field",
       signature: "rp2040_svd.sysinfo.chip_id_revision_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CHIP_ID_REVISION_Field is HAL.UInt4;",
       }   ,
   ]
,variables:    [
       {
       name: "SYSINFO_Periph",
       qualified_name: "RP2040_SVD.SYSINFO.SYSINFO_Periph",
       signature: "rp2040_svd.sysinfo.sysinfo_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SYSINFO_Periph : aliased SYSINFO_Peripheral\n  with Import, Address => SYSINFO_Base;",
       }   ,
   ]
,}
---
