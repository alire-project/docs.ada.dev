---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.PIO.WS2812",
qualified_name: "RP.PIO.WS2812",
signature: "rp.pio.ws2812",
enclosing: "rp.pio",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Strip",
       qualified_name: "RP.PIO.WS2812.Strip",
       signature: "rp.pio.ws2812.strip",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Strip\n   (Pin : not null access RP.GPIO.GPIO_Point;\n    PIO : not null access PIO_Device;\n    SM  : PIO_SM;\n    Number_Of_LEDs : Positive)\nis tagged record\n   Data        : HAL.UInt32_Array (1 .. Number_Of_LEDs);\n   Initialized : Boolean := False;\n   DMA_Ready   : Boolean := False;\n   DMA_Chan    : RP.DMA.DMA_Channel_Id;\nend record;",
       }   ,
   ]
,}
---
