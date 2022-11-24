---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "BNO055_I2C_IO",
qualified_name: "BNO055_I2C_IO",
signature: "bno055_i2c_io",
enclosing: "",
is_private: false,
documentation: "This package provides I/O for communicating with the BNO055 sensor hardware\nin terms of I2C. (USART-based communication is an alternative.)",
documentation_snippet: "",
record_types:    [
       {
       name: "IO_Port",
       qualified_name: "BNO055_I2C_IO.IO_Port",
       signature: "bno055_i2c_io.io_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IO_Port is tagged record\n   Port   : Any_I2C_Port;\n   Device : I2C_Address;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_IO_Port",
       qualified_name: "BNO055_I2C_IO.Any_IO_Port",
       signature: "bno055_i2c_io.any_io_port",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_IO_Port is access all IO_Port'Class;",
       }   ,
   ]
,}
---
