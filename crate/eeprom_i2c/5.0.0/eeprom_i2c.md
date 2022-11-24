---
crate: eeprom_i2c
layout: gnatdoc
gnatdoc: {
name: "EEPROM_I2C",
qualified_name: "EEPROM_I2C",
signature: "eeprom_i2c",
enclosing: "",
is_private: false,
documentation: "---------------------------------------------------------------------------\n  List of all implemented/supported chips\n  The data sheets will be added into this repository",
documentation_snippet: "",
simple_types:    [
       {
       name: "EEPROM_Chip",
       qualified_name: "EEPROM_I2C.EEPROM_Chip",
       signature: "eeprom_i2c.eeprom_chip",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum EEC_MC24XX01\n  MicroChip 24XX01/24LC01B\n@enum EEC_MC24XX02\n  MicroChip 24XX02/24LC02B\n@enum EEC_MC24XX16\n  MicroChip 24LC16B\n@enum EEC_MC24XX64\n  MicroChip 24XX64\n@enum EEC_MC24XX512\n  MicroChip 24XX512",
       documentation_snippet: "type EEPROM_Chip is (EEC_MC24XX01,\n                     EEC_MC24XX02,\n                     EEC_MC24XX16,\n                     EEC_MC24XX64,\n                     EEC_MC24XX512\n                    );",
       }   ,
       {
       name: "EEPROM_Status",
       qualified_name: "EEPROM_I2C.EEPROM_Status",
       signature: "eeprom_i2c.eeprom_status",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Ok\n  returned, if the requested memory address of\n  the EEPROM is out of range:\n  Mem_Addr > Mem_Addr_Size\n  In this case, no I2C operation is started\n@enum Address_Out_Of_Range\n  returned, if the requested data to write is\n  too big.\n  This means, that the relation:\n     Mem_Addr + Data'Size > Size_In_Bytes\n@enum Data_Too_Big\n  Is set,\n  if anything is not OK with the I2C operation\n@enum I2C_Not_Ok",
       documentation_snippet: "type EEPROM_Status is (\n                       Ok,\n                       Address_Out_Of_Range,\n                       Data_Too_Big,\n                       I2C_Not_Ok\n                      );",
       }   ,
   ]
,record_types:    [
       {
       name: "EEPROM_Effective_Address",
       qualified_name: "EEPROM_I2C.EEPROM_Effective_Address",
       signature: "eeprom_i2c.eeprom_effective_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type EEPROM_Effective_Address is record\n   I2C_Address : HAL.I2C.I2C_Address;\n   Mem_Addr    : HAL.UInt16;\nend record;",
       }   ,
       {
       name: "EEPROM_Operation_Result",
       qualified_name: "EEPROM_I2C.EEPROM_Operation_Result",
       signature: "eeprom_i2c.eeprom_operation_result",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type EEPROM_Operation_Result is record\n   E_Status   : EEPROM_Status;\n   I2C_Status : HAL.I2C.I2C_Status;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "EEPROM",
       qualified_name: "EEPROM_I2C.EEPROM",
       signature: "eeprom_i2c.eeprom",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type EEPROM is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "EEPROM_Memory",
       qualified_name: "EEPROM_I2C.EEPROM_Memory",
       signature: "eeprom_i2c.eeprom_memory",
       enclosing: "",
       is_private: false,
       documentation: "\n@field C_Type_of_Chip\n  the size of addressing the EEPROM\n@field C_Memory_Address_Size\n@field C_Size_In_Bytes\n@field C_Size_In_Bits\n@field C_Number_Of_Blocks\n@field C_Bytes_Per_Block\n@field C_Number_Of_Pages\n@field C_Bytes_Per_Page\n@field C_Max_Byte_Address\n@field C_Write_Delay_MS\n@field C_Delay_Callback\n  the address of the EEPROM on the bus\n@field I2C_Addr\n  the port where the EEPROM is connected to\n@field I2C_Port",
       documentation_snippet: "type EEPROM_Memory (\n                    C_Type_of_Chip        : EEPROM_Chip;\n                    C_Memory_Address_Size : HAL.I2C.I2C_Memory_Address_Size;\n                    C_Size_In_Bytes       : HAL.UInt32;\n                    C_Size_In_Bits        : HAL.UInt32;\n                    C_Number_Of_Blocks    : HAL.UInt16;\n                    C_Bytes_Per_Block     : HAL.UInt32;\n                    C_Number_Of_Pages     : HAL.UInt16;\n                    C_Bytes_Per_Page      : HAL.UInt16;\n                    C_Max_Byte_Address    : HAL.UInt32;\n                    C_Write_Delay_MS      : Integer;\n                    C_Delay_Callback      : Proc_Delay_Callback_MS;\n                    I2C_Addr            : HAL.I2C.I2C_Address;\n                    I2C_Port            : not null HAL.I2C.Any_I2C_Port\n                   )\nis new EEPROM with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_EEPROM",
       qualified_name: "EEPROM_I2C.Any_EEPROM",
       signature: "eeprom_i2c.any_eeprom",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_EEPROM is access all EEPROM'Class;",
       }   ,
       {
       name: "Any_EEPROM_Memory",
       qualified_name: "EEPROM_I2C.Any_EEPROM_Memory",
       signature: "eeprom_i2c.any_eeprom_memory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_EEPROM_Memory is access all EEPROM_Memory'Class;",
       }   ,
       {
       name: "Proc_Delay_Callback_MS",
       qualified_name: "EEPROM_I2C.Proc_Delay_Callback_MS",
       signature: "eeprom_i2c.proc_delay_callback_ms",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proc_Delay_Callback_MS is not null access procedure (MS : Integer);",
       }   ,
   ]
,}
---
