---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "LIS3DSH.SPI",
qualified_name: "LIS3DSH.SPI",
signature: "lis3dsh.spi",
enclosing: "lis3dsh",
is_private: false,
documentation: "This package provides a SPI-based I/O implementation for the LIS3DSH\naccelerometer.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Three_Axis_Accelerometer_SPI",
       qualified_name: "LIS3DSH.SPI.Three_Axis_Accelerometer_SPI",
       signature: "lis3dsh.spi.three_axis_accelerometer_spi",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Three_Axis_Accelerometer_SPI\n  (Port        : not null Any_SPI_Port;\n   Chip_Select : not null Any_GPIO_Point)\nis new Three_Axis_Accelerometer with private;",
       }   ,
   ]
,}
---
