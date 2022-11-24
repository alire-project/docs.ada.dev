---
crate: eeprom_i2c
layout: gnatdoc
gnatdoc: {
name: "EEPROM_I2C.MC24XX02",
qualified_name: "EEPROM_I2C.MC24XX02",
signature: "eeprom_i2c.mc24xx02",
enclosing: "eeprom_i2c",
is_private: false,
documentation: "---------------------------------------------------------------------------\n  This is the default I2C address of the EEPROM.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "EEPROM_Memory_MC24XX02",
       qualified_name: "EEPROM_I2C.MC24XX02.EEPROM_Memory_MC24XX02",
       signature: "eeprom_i2c.mc24xx02.eeprom_memory_mc24xx02",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type EEPROM_Memory_MC24XX02 (\n                             C_Delay_Callback : Proc_Delay_Callback_MS;\n                             I2C_Addr : HAL.I2C.I2C_Address;\n                             I2C_Port : not null HAL.I2C.Any_I2C_Port\n                            )\nis new EEPROM_Memory (\n                      C_Type_of_Chip => EEC_MC24XX02,\n                      C_Memory_Address_Size => HAL.I2C.Memory_Size_8b,\n                      C_Size_In_Bytes => 256,\n                      C_Size_In_Bits => 2048,\n                      C_Number_Of_Blocks => 1,\n                      C_Bytes_Per_Block => 256,\n                      C_Number_Of_Pages => 32,\n                      C_Bytes_Per_Page => 8,\n                      C_Max_Byte_Address => 16#FF#,\n                      C_Write_Delay_MS => 5,\n                      C_Delay_Callback => C_Delay_Callback,\n                      I2C_Addr => I2C_Addr,\n                      I2C_Port => I2C_Port\n                     ) with null record;",
       }   ,
   ]
,constants:    [
       {
       name: "I2C_DEFAULT_ADDRESS",
       qualified_name: "EEPROM_I2C.MC24XX02.I2C_DEFAULT_ADDRESS",
       signature: "eeprom_i2c.mc24xx02.i2c_default_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "I2C_DEFAULT_ADDRESS : constant HAL.I2C.I2C_Address := 2#1010_0000#;",
       }   ,
   ]
,}
---
