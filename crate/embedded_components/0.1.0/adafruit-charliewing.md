---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "AdaFruit.CharlieWing",
qualified_name: "AdaFruit.CharlieWing",
signature: "adafruit.charliewing",
enclosing: "adafruit",
is_private: false,
documentation: "Driver for the AdaFruit Charlie Wing matrix LED board.\nSee the IS31FL3731 package for API documentation.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Device",
       qualified_name: "AdaFruit.CharlieWing.Device",
       signature: "adafruit.charliewing.device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Device\n  (Port : not null HAL.I2C.Any_I2C_Port;\n   AD   : HAL.UInt2)\nis new IS31FL3731.Device\nwith private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "X_Coord",
       qualified_name: "AdaFruit.CharlieWing.X_Coord",
       signature: "adafruit.charliewing.x_coord",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype X_Coord is IS31FL3731.X_Coord range 0 .. 15;",
       }   ,
       {
       name: "Y_Coord",
       qualified_name: "AdaFruit.CharlieWing.Y_Coord",
       signature: "adafruit.charliewing.y_coord",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Y_Coord is IS31FL3731.Y_Coord range 0 .. 6;",
       }   ,
   ]
,}
---
