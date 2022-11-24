---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.I2C_Master",
qualified_name: "RP.I2C_Master",
signature: "rp.i2c_master",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "I2C_Address_Size",
       qualified_name: "RP.I2C_Master.I2C_Address_Size",
       signature: "rp.i2c_master.i2c_address_size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Address_Size is (Address_Size_7b, Address_Size_10b);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "I2C_Master_Port",
       qualified_name: "RP.I2C_Master.I2C_Master_Port",
       signature: "rp.i2c_master.i2c_master_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type I2C_Master_Port\n   (Num    : I2C_Number;\n    Periph : not null access RP2040_SVD.I2C.I2C_Peripheral)\nis new HAL.I2C.I2C_Port with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "I2C_Number",
       qualified_name: "RP.I2C_Master.I2C_Number",
       signature: "rp.i2c_master.i2c_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype I2C_Number is Natural range 0 .. 1;",
       }   ,
   ]
,}
---
