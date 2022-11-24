---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD",
qualified_name: "RP2040_SVD",
signature: "rp2040_svd",
enclosing: "",
is_private: false,
documentation: "------------------\n Base addresses --\n------------------",
documentation_snippet: "",
constants:    [
       {
       name: "ADC_Base",
       qualified_name: "RP2040_SVD.ADC_Base",
       signature: "rp2040_svd.adc_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ADC_Base : constant System.Address := System'To_Address (16#4004C000#);",
       }   ,
       {
       name: "BUSCTRL_Base",
       qualified_name: "RP2040_SVD.BUSCTRL_Base",
       signature: "rp2040_svd.busctrl_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "BUSCTRL_Base : constant System.Address := System'To_Address (16#40030000#);",
       }   ,
       {
       name: "CLOCKS_Base",
       qualified_name: "RP2040_SVD.CLOCKS_Base",
       signature: "rp2040_svd.clocks_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CLOCKS_Base : constant System.Address := System'To_Address (16#40008000#);",
       }   ,
       {
       name: "DMA_Base",
       qualified_name: "RP2040_SVD.DMA_Base",
       signature: "rp2040_svd.dma_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "DMA_Base : constant System.Address := System'To_Address (16#50000000#);",
       }   ,
       {
       name: "I2C0_Base",
       qualified_name: "RP2040_SVD.I2C0_Base",
       signature: "rp2040_svd.i2c0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "I2C0_Base : constant System.Address := System'To_Address (16#40044000#);",
       }   ,
       {
       name: "I2C1_Base",
       qualified_name: "RP2040_SVD.I2C1_Base",
       signature: "rp2040_svd.i2c1_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "I2C1_Base : constant System.Address := System'To_Address (16#40048000#);",
       }   ,
       {
       name: "IO_BANK0_Base",
       qualified_name: "RP2040_SVD.IO_BANK0_Base",
       signature: "rp2040_svd.io_bank0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "IO_BANK0_Base : constant System.Address := System'To_Address (16#40014000#);",
       }   ,
       {
       name: "IO_QSPI_Base",
       qualified_name: "RP2040_SVD.IO_QSPI_Base",
       signature: "rp2040_svd.io_qspi_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "IO_QSPI_Base : constant System.Address := System'To_Address (16#40018000#);",
       }   ,
       {
       name: "PADS_BANK0_Base",
       qualified_name: "RP2040_SVD.PADS_BANK0_Base",
       signature: "rp2040_svd.pads_bank0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PADS_BANK0_Base : constant System.Address := System'To_Address (16#4001C000#);",
       }   ,
       {
       name: "PADS_QSPI_Base",
       qualified_name: "RP2040_SVD.PADS_QSPI_Base",
       signature: "rp2040_svd.pads_qspi_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PADS_QSPI_Base : constant System.Address := System'To_Address (16#40020000#);",
       }   ,
       {
       name: "PIO0_Base",
       qualified_name: "RP2040_SVD.PIO0_Base",
       signature: "rp2040_svd.pio0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PIO0_Base : constant System.Address := System'To_Address (16#50200000#);",
       }   ,
       {
       name: "PIO1_Base",
       qualified_name: "RP2040_SVD.PIO1_Base",
       signature: "rp2040_svd.pio1_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PIO1_Base : constant System.Address := System'To_Address (16#50300000#);",
       }   ,
       {
       name: "PLL_SYS_Base",
       qualified_name: "RP2040_SVD.PLL_SYS_Base",
       signature: "rp2040_svd.pll_sys_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_SYS_Base : constant System.Address := System'To_Address (16#40028000#);",
       }   ,
       {
       name: "PLL_USB_Base",
       qualified_name: "RP2040_SVD.PLL_USB_Base",
       signature: "rp2040_svd.pll_usb_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PLL_USB_Base : constant System.Address := System'To_Address (16#4002C000#);",
       }   ,
       {
       name: "PPB_Base",
       qualified_name: "RP2040_SVD.PPB_Base",
       signature: "rp2040_svd.ppb_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PPB_Base : constant System.Address := System'To_Address (16#E0000000#);",
       }   ,
       {
       name: "PSM_Base",
       qualified_name: "RP2040_SVD.PSM_Base",
       signature: "rp2040_svd.psm_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PSM_Base : constant System.Address := System'To_Address (16#40010000#);",
       }   ,
       {
       name: "PWM_Base",
       qualified_name: "RP2040_SVD.PWM_Base",
       signature: "rp2040_svd.pwm_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PWM_Base : constant System.Address := System'To_Address (16#40050000#);",
       }   ,
       {
       name: "RESETS_Base",
       qualified_name: "RP2040_SVD.RESETS_Base",
       signature: "rp2040_svd.resets_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RESETS_Base : constant System.Address := System'To_Address (16#4000C000#);",
       }   ,
       {
       name: "ROSC_Base",
       qualified_name: "RP2040_SVD.ROSC_Base",
       signature: "rp2040_svd.rosc_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "ROSC_Base : constant System.Address := System'To_Address (16#40060000#);",
       }   ,
       {
       name: "RTC_Base",
       qualified_name: "RP2040_SVD.RTC_Base",
       signature: "rp2040_svd.rtc_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "RTC_Base : constant System.Address := System'To_Address (16#4005C000#);",
       }   ,
       {
       name: "SIO_Base",
       qualified_name: "RP2040_SVD.SIO_Base",
       signature: "rp2040_svd.sio_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SIO_Base : constant System.Address := System'To_Address (16#D0000000#);",
       }   ,
       {
       name: "SPI0_Base",
       qualified_name: "RP2040_SVD.SPI0_Base",
       signature: "rp2040_svd.spi0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SPI0_Base : constant System.Address := System'To_Address (16#4003C000#);",
       }   ,
       {
       name: "SPI1_Base",
       qualified_name: "RP2040_SVD.SPI1_Base",
       signature: "rp2040_svd.spi1_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SPI1_Base : constant System.Address := System'To_Address (16#40040000#);",
       }   ,
       {
       name: "SYSCFG_Base",
       qualified_name: "RP2040_SVD.SYSCFG_Base",
       signature: "rp2040_svd.syscfg_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SYSCFG_Base : constant System.Address := System'To_Address (16#40004000#);",
       }   ,
       {
       name: "SYSINFO_Base",
       qualified_name: "RP2040_SVD.SYSINFO_Base",
       signature: "rp2040_svd.sysinfo_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SYSINFO_Base : constant System.Address := System'To_Address (16#40000000#);",
       }   ,
       {
       name: "TBMAN_Base",
       qualified_name: "RP2040_SVD.TBMAN_Base",
       signature: "rp2040_svd.tbman_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TBMAN_Base : constant System.Address := System'To_Address (16#4006C000#);",
       }   ,
       {
       name: "TIMER_Base",
       qualified_name: "RP2040_SVD.TIMER_Base",
       signature: "rp2040_svd.timer_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "TIMER_Base : constant System.Address := System'To_Address (16#40054000#);",
       }   ,
       {
       name: "UART0_Base",
       qualified_name: "RP2040_SVD.UART0_Base",
       signature: "rp2040_svd.uart0_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "UART0_Base : constant System.Address := System'To_Address (16#40034000#);",
       }   ,
       {
       name: "UART1_Base",
       qualified_name: "RP2040_SVD.UART1_Base",
       signature: "rp2040_svd.uart1_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "UART1_Base : constant System.Address := System'To_Address (16#40038000#);",
       }   ,
       {
       name: "USBCTRL_DPRAM_Base",
       qualified_name: "RP2040_SVD.USBCTRL_DPRAM_Base",
       signature: "rp2040_svd.usbctrl_dpram_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "USBCTRL_DPRAM_Base : constant System.Address := System'To_Address (16#50100000#);",
       }   ,
       {
       name: "USBCTRL_REGS_Base",
       qualified_name: "RP2040_SVD.USBCTRL_REGS_Base",
       signature: "rp2040_svd.usbctrl_regs_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "USBCTRL_REGS_Base : constant System.Address := System'To_Address (16#50110000#);",
       }   ,
       {
       name: "VREG_AND_CHIP_RESET_Base",
       qualified_name: "RP2040_SVD.VREG_AND_CHIP_RESET_Base",
       signature: "rp2040_svd.vreg_and_chip_reset_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "VREG_AND_CHIP_RESET_Base : constant System.Address := System'To_Address (16#40064000#);",
       }   ,
       {
       name: "WATCHDOG_Base",
       qualified_name: "RP2040_SVD.WATCHDOG_Base",
       signature: "rp2040_svd.watchdog_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "WATCHDOG_Base : constant System.Address := System'To_Address (16#40058000#);",
       }   ,
       {
       name: "XIP_CTRL_Base",
       qualified_name: "RP2040_SVD.XIP_CTRL_Base",
       signature: "rp2040_svd.xip_ctrl_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XIP_CTRL_Base : constant System.Address := System'To_Address (16#14000000#);",
       }   ,
       {
       name: "XIP_SSI_Base",
       qualified_name: "RP2040_SVD.XIP_SSI_Base",
       signature: "rp2040_svd.xip_ssi_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XIP_SSI_Base : constant System.Address := System'To_Address (16#18000000#);",
       }   ,
       {
       name: "XOSC_Base",
       qualified_name: "RP2040_SVD.XOSC_Base",
       signature: "rp2040_svd.xosc_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XOSC_Base : constant System.Address := System'To_Address (16#40024000#);",
       }   ,
   ]
,}
---