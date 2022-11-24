---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.PADS_QSPI",
qualified_name: "RP2040_SVD.PADS_QSPI",
signature: "rp2040_svd.pads_qspi",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "GPIO_QSPI_SCLK_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SCLK_DRIVE_Field",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_sclk_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SCLK_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "GPIO_QSPI_SD0_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SD0_DRIVE_Field",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_sd0_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SD0_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "GPIO_QSPI_SS_DRIVE_Field",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SS_DRIVE_Field",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_ss_drive_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SS_DRIVE_Field is\n  (Val_2mA,\n   Val_4mA,\n   Val_8mA,\n   Val_12mA)\n  with Size => 2;",
       }   ,
       {
       name: "VOLTAGE_SELECT_VOLTAGE_SELECT_Field",
       qualified_name: "RP2040_SVD.PADS_QSPI.VOLTAGE_SELECT_VOLTAGE_SELECT_Field",
       signature: "rp2040_svd.pads_qspi.voltage_select_voltage_select_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Val_3v3\n  Set voltage to 1.8V (DVDD <= 1V8)\n@enum Val_1v8",
       documentation_snippet: "type VOLTAGE_SELECT_VOLTAGE_SELECT_Field is\n   Val_3v3,\n   Val_1v8)\n  with Size => 1;",
       }   ,
   ]
,record_types:    [
       {
       name: "GPIO_QSPI_SCLK_Register",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SCLK_Register",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_sclk_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SCLK_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := True;\n   PUE           : Boolean := False;\n   DRIVE         : GPIO_QSPI_SCLK_DRIVE_Field :=\n                    RP2040_SVD.PADS_QSPI.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "GPIO_QSPI_SD_Register",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SD_Register",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_sd_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SD_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := False;\n   PUE           : Boolean := False;\n   DRIVE         : GPIO_QSPI_SD0_DRIVE_Field :=\n                    RP2040_SVD.PADS_QSPI.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "GPIO_QSPI_SS_Register",
       qualified_name: "RP2040_SVD.PADS_QSPI.GPIO_QSPI_SS_Register",
       signature: "rp2040_svd.pads_qspi.gpio_qspi_ss_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GPIO_QSPI_SS_Register is record\n   SLEWFAST      : Boolean := False;\n   SCHMITT       : Boolean := True;\n   PDE           : Boolean := False;\n   PUE           : Boolean := True;\n   DRIVE         : GPIO_QSPI_SS_DRIVE_Field :=\n                    RP2040_SVD.PADS_QSPI.Val_4mA;\n   IE            : Boolean := True;\n   OD            : Boolean := False;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "PADS_QSPI_Peripheral",
       qualified_name: "RP2040_SVD.PADS_QSPI.PADS_QSPI_Peripheral",
       signature: "rp2040_svd.pads_qspi.pads_qspi_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PADS_QSPI_Peripheral is record\n   VOLTAGE_SELECT : aliased VOLTAGE_SELECT_Register;\n   GPIO_QSPI_SCLK : aliased GPIO_QSPI_SCLK_Register;\n   GPIO_QSPI_SD0  : aliased GPIO_QSPI_SD_Register;\n   GPIO_QSPI_SD1  : aliased GPIO_QSPI_SD_Register;\n   GPIO_QSPI_SD2  : aliased GPIO_QSPI_SD_Register;\n   GPIO_QSPI_SD3  : aliased GPIO_QSPI_SD_Register;\n   GPIO_QSPI_SS   : aliased GPIO_QSPI_SS_Register;\nend record\n  with Volatile;",
       }   ,
       {
       name: "VOLTAGE_SELECT_Register",
       qualified_name: "RP2040_SVD.PADS_QSPI.VOLTAGE_SELECT_Register",
       signature: "rp2040_svd.pads_qspi.voltage_select_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type VOLTAGE_SELECT_Register is record\n   VOLTAGE_SELECT : VOLTAGE_SELECT_VOLTAGE_SELECT_Field :=\n                     RP2040_SVD.PADS_QSPI.Val_3v3;\n   Reserved_1_31  : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
   ]
,variables:    [
       {
       name: "PADS_QSPI_Periph",
       qualified_name: "RP2040_SVD.PADS_QSPI.PADS_QSPI_Periph",
       signature: "rp2040_svd.pads_qspi.pads_qspi_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PADS_QSPI_Periph : aliased PADS_QSPI_Peripheral\n  with Import, Address => PADS_QSPI_Base;",
       }   ,
   ]
,}
---
