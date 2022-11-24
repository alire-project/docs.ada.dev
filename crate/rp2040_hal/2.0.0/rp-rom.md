---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.ROM",
qualified_name: "RP.ROM",
signature: "rp.rom",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Short_Address",
       qualified_name: "RP.ROM.Short_Address",
       signature: "rp.rom.short_address",
       enclosing: "",
       is_private: false,
       documentation: "Some lookup tables use halfwords",
       documentation_snippet: "type Short_Address is new Unsigned_16;",
       }   ,
       {
       name: "Table_Code",
       qualified_name: "RP.ROM.Table_Code",
       signature: "rp.rom.table_code",
       enclosing: "",
       is_private: false,
       documentation: "Function and Data table entries are indexed by a two-character mnemonic,\nstored in a 32-bit field.  The top two bytes are always zero, presumably\nreserved for future use.",
       documentation_snippet: "type Table_Code is new Unsigned_32;",
       }   ,
   ]
,array_types:    [
       {
       name: "Magic_Field",
       qualified_name: "RP.ROM.Magic_Field",
       signature: "rp.rom.magic_field",
       enclosing: "",
       is_private: false,
       documentation: "Magic should always be ('M', 'u', 1)",
       documentation_snippet: "type Magic_Field is array (1 .. 3) of Unsigned_8;",
       }   ,
   ]
,record_types:    [
       {
       name: "Header_Fields",
       qualified_name: "RP.ROM.Header_Fields",
       signature: "rp.rom.header_fields",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Header_Fields is record\n   Initial_SP        : System.Address;\n   Reset_Handler     : System.Address;\n   NMI_Handler       : System.Address;\n   HardFault_Handler : System.Address;\n   Magic             : Magic_Field;\n   Version           : Unsigned_8;\n   Func_Table        : Short_Address;\n   Data_Table        : Short_Address;\n   Table_Lookup      : Short_Address;\nend record\n   with Size => 208;",
       }   ,
   ]
,constants:    [
       {
       name: "Header",
       qualified_name: "RP.ROM.Header",
       signature: "rp.rom.header",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Header : constant Header_Fields\n   with Import, Address => System'To_Address (16#0000_0000#);",
       }   ,
   ]
,}
---
