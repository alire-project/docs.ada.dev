---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.Reset",
qualified_name: "RP.Reset",
signature: "rp.reset",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Reset_Id",
       qualified_name: "RP.Reset.Reset_Id",
       signature: "rp.reset.reset_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reset_Id is\n   (Reset_ADC,\n    Reset_BUSCTRL,\n    Reset_DMA,\n    Reset_I2C0,\n    Reset_I2C1,\n    Reset_IO_BANK0,\n    Reset_QSPI,\n    Reset_JTAG,\n    Reset_PADS_BANK0,\n    Reset_PADS_QSPI,\n    Reset_PIO0,\n    Reset_PIO1,\n    Reset_PLL_SYS,\n    Reset_PLL_USB,\n    Reset_PWM,\n    Reset_RTC,\n    Reset_SPI0,\n    Reset_SPI1,\n    Reset_SYSCFG,\n    Reset_SYSINFO,\n    Reset_TBMAN,\n    Reset_TIMER,\n    Reset_UART0,\n    Reset_UART1,\n    Reset_USBCTRL);",
       }   ,
       {
       name: "Reset_Status",
       qualified_name: "RP.Reset.Reset_Status",
       signature: "rp.reset.reset_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Reset_Status is\n   (Reset_Ok,\n    Reset_Timeout);",
       }   ,
   ]
,}
---
