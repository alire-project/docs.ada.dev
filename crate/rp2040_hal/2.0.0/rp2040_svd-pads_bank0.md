---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.PADS_BANK0",
qualified_name: "RP2040_SVD.PADS_BANK0",
signature: "rp2040_svd.pads_bank0",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "GPIO0_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_BANK0.GPIO0_DRIVE_Field",
       signature: "rp2040_svd.pads_bank0.gpio0_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO0_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "SWCLK_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_BANK0.SWCLK_DRIVE_Field",
       signature: "rp2040_svd.pads_bank0.swclk_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWCLK_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "SWD_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_BANK0.SWD_DRIVE_Field",
       signature: "rp2040_svd.pads_bank0.swd_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWD_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "VOLTAGE_SELECT_VOLTAGE_SELECT_Field",
       qualified_name: "RP2040_SVD.PADS_BANK0.VOLTAGE_SELECT_VOLTAGE_SELECT_Field",
       signature: "rp2040_svd.pads_bank0.voltage_select_voltage_select_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Val_3v3\n  Set voltage to 1.8V (DVDD <= 1V8)\n@enum Val_1v8",
       documentation_snippet: "type VOLTAGE_SELECT_VOLTAGE_SELECT_Field is\n   Val_3v3,\n   Val_1v8)\n  with Size => 1;",
       }   ,
   ]
,record_types:    [
       {
       name: "GPIO_Register",
       qualified_name: "RP2040_SVD.PADS_BANK0.GPIO_Register",
       signature: "rp2040_svd.pads_bank0.gpio_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := True;\n   PUE           : Boolean := False;\n   DRIVE         : GPIO0_DRIVE_Field := RP2040_SVD.PADS_BANK0.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PADS_BANK0_Peripheral",
       qualified_name: "RP2040_SVD.PADS_BANK0.PADS_BANK0_Peripheral",
       signature: "rp2040_svd.pads_bank0.pads_bank0_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PADS_BANK0_Peripheral is record\n   VOLTAGE_SELECT : aliased VOLTAGE_SELECT_Register;\n   GPIO0          : aliased GPIO_Register;\n   GPIO1          : aliased GPIO_Register;\n   GPIO2          : aliased GPIO_Register;\n   GPIO3          : aliased GPIO_Register;\n   GPIO4          : aliased GPIO_Register;\n   GPIO5          : aliased GPIO_Register;\n   GPIO6          : aliased GPIO_Register;\n   GPIO7          : aliased GPIO_Register;\n   GPIO8          : aliased GPIO_Register;\n   GPIO9          : aliased GPIO_Register;\n   GPIO10         : aliased GPIO_Register;\n   GPIO11         : aliased GPIO_Register;\n   GPIO12         : aliased GPIO_Register;\n   GPIO13         : aliased GPIO_Register;\n   GPIO14         : aliased GPIO_Register;\n   GPIO15         : aliased GPIO_Register;\n   GPIO16         : aliased GPIO_Register;\n   GPIO17         : aliased GPIO_Register;\n   GPIO18         : aliased GPIO_Register;\n   GPIO19         : aliased GPIO_Register;\n   GPIO20         : aliased GPIO_Register;\n   GPIO21         : aliased GPIO_Register;\n   GPIO22         : aliased GPIO_Register;\n   GPIO23         : aliased GPIO_Register;\n   GPIO24         : aliased GPIO_Register;\n   GPIO25         : aliased GPIO_Register;\n   GPIO26         : aliased GPIO_Register;\n   GPIO27         : aliased GPIO_Register;\n   GPIO28         : aliased GPIO_Register;\n   GPIO29         : aliased GPIO_Register;\n   SWCLK          : aliased SWCLK_Register;\n   SWD            : aliased SWD_Register;\nend record\n  with Volatile;",
       }   ,
       {
       name: "SWCLK_Register",
       qualified_name: "RP2040_SVD.PADS_BANK0.SWCLK_Register",
       signature: "rp2040_svd.pads_bank0.swclk_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWCLK_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := False;\n   PUE           : Boolean := True;\n   DRIVE         : SWCLK_DRIVE_Field := RP2040_SVD.PADS_BANK0.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := True;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SWD_Register",
       qualified_name: "RP2040_SVD.PADS_BANK0.SWD_Register",
       signature: "rp2040_svd.pads_bank0.swd_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SWD_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := False;\n   PUE           : Boolean := True;\n   DRIVE         : SWD_DRIVE_Field := RP2040_SVD.PADS_BANK0.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "VOLTAGE_SELECT_Register",
       qualified_name: "RP2040_SVD.PADS_BANK0.VOLTAGE_SELECT_Register",
       signature: "rp2040_svd.pads_bank0.voltage_select_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VOLTAGE_SELECT_Register is record\n   VOLTAGE_SELECT : VOLTAGE_SELECT_VOLTAGE_SELECT_Field :=\n                     RP2040_SVD.PADS_BANK0.Val_3v3;\n   Reserved_1_31  : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
   ]
,variables:    [
       {
       name: "PADS_BANK0_Periph",
       qualified_name: "RP2040_SVD.PADS_BANK0.PADS_BANK0_Periph",
       signature: "rp2040_svd.pads_bank0.pads_bank0_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PADS_BANK0_Periph : aliased PADS_BANK0_Peripheral\n  with Import, Address => PADS_BANK0_Base;",
       }   ,
   ]
,}
---
