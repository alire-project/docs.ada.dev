---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.DMA",
qualified_name: "RP.DMA",
signature: "rp.dma",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Checksum_Algorithm",
       qualified_name: "RP.DMA.Checksum_Algorithm",
       signature: "rp.dma.checksum_algorithm",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum CRC_32\n  CRC-32 (IEEE802.3 polynomial)\n@enum CRC_32R\n  CRC-32 (IEEE802.3 polynomial) with bit reversed data\n@enum CRC_16\n  CRC-16-CCITT\n@enum CRC_16R\n  CRC-16-CCITT with bit reversed data\n@enum EVEN\n  XOR reduction over all data. == 1 if total 1 population count is odd\n@enum SUM\n  Calculate a simple 32-bit checksum (addition with 32 bit accumulator)",
       documentation_snippet: "type Checksum_Algorithm is\n   (CRC_32,\n    CRC_32R,\n    CRC_16,\n    CRC_16R,\n    EVEN,\n    SUM);",
       }   ,
       {
       name: "DMA_Channel_Id",
       qualified_name: "RP.DMA.DMA_Channel_Id",
       signature: "rp.dma.dma_channel_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMA_Channel_Id is range 0 .. 11\n   with Size => 4;",
       }   ,
       {
       name: "DMA_Request_Trigger",
       qualified_name: "RP.DMA.DMA_Request_Trigger",
       signature: "rp.dma.dma_request_trigger",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMA_Request_Trigger is\n   (PIO0_TX0, PIO0_TX1, PIO0_TX2, PIO0_TX3, PIO0_RX0, PIO0_RX1, PIO0_RX2, PIO0_RX3,\n    PIO1_TX0, PIO1_TX1, PIO1_TX2, PIO1_TX3, PIO1_RX0, PIO1_RX1, PIO1_RX2, PIO1_RX3,\n    SPI0_TX, SPI0_RX,\n    SPI1_TX, SPI1_RX,\n    UART0_TX, UART0_RX,\n    UART1_TX, UART1_RX,\n    PWM_WRAP0, PWM_WRAP1, PWM_WRAP2, PWM_WRAP3, PWM_WRAP4, PWM_WRAP5, PWM_WRAP6, PWM_WRAP7,\n    I2C0_TX, I2C0_RX,\n    I2C1_TX, I2C1_RX,\n    ADC,\n    XIP_STREAM, XIP_SSITX, XIP_SSIRX,\n    TIMER0, TIMER1, TIMER2, TIMER3,\n    PERMANENT)\n    with Size => 6;",
       }   ,
       {
       name: "Ring_Wrap_Select",
       qualified_name: "RP.DMA.Ring_Wrap_Select",
       signature: "rp.dma.ring_wrap_select",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ring_Wrap_Select is (Wrap_Read, Wrap_Write)\n   with Size => 1;",
       }   ,
       {
       name: "Transfer_Width",
       qualified_name: "RP.DMA.Transfer_Width",
       signature: "rp.dma.transfer_width",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Transfer_Width is (Transfer_8, Transfer_16, Transfer_32)\n   with Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "DMA_Configuration",
       qualified_name: "RP.DMA.DMA_Configuration",
       signature: "rp.dma.dma_configuration",
       enclosing: "",
       is_private: false,
       documentation: "\n@field High_Priority\n  Schedule this channel before others\n@field Data_Size\n  Bits per transfer (byte, halfword, word)\n@field Increment_Read\n  Increment read address after transfer\n@field Increment_Write\n  Increment write address after transfer\n@field Ring_Size\n  Ring buffer size\n@field Ring_Wrap\n  Read or write buffer is a ring buffer\n@field Chain_To\n  Trigger another channel after transfer.\n@field Trigger\n  Trigger a transfer on this signal\n@field Quiet\n  Disable interrupts\n@field Byte_Swap\n  Reverse byte order\n@field Sniff\n  Send data to sniff checksum",
       documentation_snippet: "type DMA_Configuration is record\n   High_Priority   : Boolean := False;\n   Data_Size       : Transfer_Width := Transfer_8;\n   Increment_Read  : Boolean := False;\n   Increment_Write : Boolean := False;\n   Ring_Size       : HAL.UInt4 := 0;\n   Ring_Wrap       : Ring_Wrap_Select := Wrap_Read;\n   Chain_To        : DMA_Channel_Id := 0;\n   Trigger         : DMA_Request_Trigger := PERMANENT;\n   Quiet           : Boolean := False;\n   Byte_Swap       : Boolean := False;\n   Sniff           : Boolean := False;\nend record;",
       }   ,
       {
       name: "DMA_Status",
       qualified_name: "RP.DMA.DMA_Status",
       signature: "rp.dma.dma_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMA_Status is record\n   Enabled             : Boolean := False;\n   Busy                : Boolean := False;\n   Write_Error         : Boolean := False;\n   Read_Error          : Boolean := False;\n   AHB_Error           : Boolean := False;\n   Transfers_Remaining : Natural := 0;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "DMA_IRQ_Id",
       qualified_name: "RP.DMA.DMA_IRQ_Id",
       signature: "rp.dma.dma_irq_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DMA_IRQ_Id is Natural range 0 .. 1;",
       }   ,
       {
       name: "DMA_Timer_Id",
       qualified_name: "RP.DMA.DMA_Timer_Id",
       signature: "rp.dma.dma_timer_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DMA_Timer_Id is DMA_Request_Trigger range TIMER0 .. TIMER3;",
       }   ,
   ]
,}
---
