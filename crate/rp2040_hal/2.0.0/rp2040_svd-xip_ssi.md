---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP2040_SVD.XIP_SSI",
qualified_name: "RP2040_SVD.XIP_SSI",
signature: "rp2040_svd.xip_ssi",
enclosing: "rp2040_svd",
is_private: false,
documentation: "-------------\n Registers --\n-------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "CTRLR0_SPI_FRF_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_SPI_FRF_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_spi_frf_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum STD\n  Dual-SPI frame format; two bits per SCK, half-duplex\n@enum DUAL\n  Quad-SPI frame format; four bits per SCK, half-duplex\n@enum QUAD",
       documentation_snippet: "type CTRLR0_SPI_FRF_Field is\n   STD,\n   DUAL,\n   QUAD)\n  with Size => 2;",
       }   ,
       {
       name: "CTRLR0_TMOD_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_TMOD_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_tmod_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum TX_AND_RX\n  Transmit only (not for FRF == 0, standard SPI mode)\n@enum TX_ONLY\n  Receive only (not for FRF == 0, standard SPI mode)\n@enum RX_ONLY\n  EEPROM read mode (TX then RX; RX starts after control data TX'd)\n@enum EEPROM_READ",
       documentation_snippet: "type CTRLR0_TMOD_Field is\n   TX_AND_RX,\n   TX_ONLY,\n   RX_ONLY,\n   EEPROM_READ)\n  with Size => 2;",
       }   ,
       {
       name: "SPI_CTRLR0_INST_L_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_INST_L_Field",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_inst_l_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum NONE\n  4-bit instruction\n@enum Val_4B\n  8-bit instruction\n@enum Val_8B\n  16-bit instruction\n@enum Val_16B",
       documentation_snippet: "type SPI_CTRLR0_INST_L_Field is\n   NONE,\n   Val_4B,\n   Val_8B,\n   Val_16B)\n  with Size => 2;",
       }   ,
       {
       name: "SPI_CTRLR0_TRANS_TYPE_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_TRANS_TYPE_Field",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_trans_type_field",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Val_1C1A\n  Command in standard SPI format, address in format specified by FRF\n@enum Val_1C2A\n  Command and address both in format specified by FRF (e.g. Dual-SPI)\n@enum Val_2C2A",
       documentation_snippet: "type SPI_CTRLR0_TRANS_TYPE_Field is\n   Val_1C1A,\n   Val_1C2A,\n   Val_2C2A)\n  with Size => 2;",
       }   ,
   ]
,record_types:    [
       {
       name: "BAUDR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.BAUDR_Register",
       signature: "rp2040_svd.xip_ssi.baudr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BAUDR_Register is record\n   SCKDV          : BAUDR_SCKDV_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "CTRLR0_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_Register",
       signature: "rp2040_svd.xip_ssi.ctrlr0_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRLR0_Register is record\n   DFS            : CTRLR0_DFS_Field := 16#0#;\n   FRF            : CTRLR0_FRF_Field := 16#0#;\n   SCPH           : Boolean := False;\n   SCPOL          : Boolean := False;\n   TMOD           : CTRLR0_TMOD_Field := RP2040_SVD.XIP_SSI.TX_AND_RX;\n   SLV_OE         : Boolean := False;\n   SRL            : Boolean := False;\n   CFS            : CTRLR0_CFS_Field := 16#0#;\n   DFS_32         : CTRLR0_DFS_32_Field := 16#0#;\n   SPI_FRF        : CTRLR0_SPI_FRF_Field := RP2040_SVD.XIP_SSI.STD;\n   Reserved_23_23 : HAL.Bit := 16#0#;\n   SSTE           : Boolean := False;\n   Reserved_25_31 : HAL.UInt7 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "CTRLR1_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR1_Register",
       signature: "rp2040_svd.xip_ssi.ctrlr1_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRLR1_Register is record\n   NDF            : CTRLR1_NDF_Field := 16#0#;\n   Reserved_16_31 : HAL.UInt16 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "DMACR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.DMACR_Register",
       signature: "rp2040_svd.xip_ssi.dmacr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMACR_Register is record\n   RDMAE         : Boolean := False;\n   TDMAE         : Boolean := False;\n   Reserved_2_31 : HAL.UInt30 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "DMARDLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.DMARDLR_Register",
       signature: "rp2040_svd.xip_ssi.dmardlr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMARDLR_Register is record\n   DMARDL        : DMARDLR_DMARDL_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "DMATDLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.DMATDLR_Register",
       signature: "rp2040_svd.xip_ssi.dmatdlr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type DMATDLR_Register is record\n   DMATDL        : DMATDLR_DMATDL_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "ICR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.ICR_Register",
       signature: "rp2040_svd.xip_ssi.icr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ICR_Register is record\n   ICR           : Boolean;\n   Reserved_1_31 : HAL.UInt31;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "IMR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.IMR_Register",
       signature: "rp2040_svd.xip_ssi.imr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type IMR_Register is record\n   TXEIM         : Boolean := False;\n   TXOIM         : Boolean := False;\n   RXUIM         : Boolean := False;\n   RXOIM         : Boolean := False;\n   RXFIM         : Boolean := False;\n   MSTIM         : Boolean := False;\n   Reserved_6_31 : HAL.UInt26 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "ISR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.ISR_Register",
       signature: "rp2040_svd.xip_ssi.isr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ISR_Register is record\n   TXEIS         : Boolean;\n   TXOIS         : Boolean;\n   RXUIS         : Boolean;\n   RXOIS         : Boolean;\n   RXFIS         : Boolean;\n   MSTIS         : Boolean;\n   Reserved_6_31 : HAL.UInt26;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "MSTICR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.MSTICR_Register",
       signature: "rp2040_svd.xip_ssi.msticr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MSTICR_Register is record\n   MSTICR        : Boolean;\n   Reserved_1_31 : HAL.UInt31;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "MWCR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.MWCR_Register",
       signature: "rp2040_svd.xip_ssi.mwcr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type MWCR_Register is record\n   MWMOD         : Boolean := False;\n   MDD           : Boolean := False;\n   MHS           : Boolean := False;\n   Reserved_3_31 : HAL.UInt29 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RISR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RISR_Register",
       signature: "rp2040_svd.xip_ssi.risr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RISR_Register is record\n   TXEIR         : Boolean;\n   TXOIR         : Boolean;\n   RXUIR         : Boolean;\n   RXOIR         : Boolean;\n   RXFIR         : Boolean;\n   MSTIR         : Boolean;\n   Reserved_6_31 : HAL.UInt26;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RX_SAMPLE_DLY_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RX_SAMPLE_DLY_Register",
       signature: "rp2040_svd.xip_ssi.rx_sample_dly_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RX_SAMPLE_DLY_Register is record\n   RSD           : RX_SAMPLE_DLY_RSD_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RXFLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RXFLR_Register",
       signature: "rp2040_svd.xip_ssi.rxflr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RXFLR_Register is record\n   RXTFL         : RXFLR_RXTFL_Field;\n   Reserved_8_31 : HAL.UInt24;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RXFTLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RXFTLR_Register",
       signature: "rp2040_svd.xip_ssi.rxftlr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RXFTLR_Register is record\n   RFT           : RXFTLR_RFT_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RXOICR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RXOICR_Register",
       signature: "rp2040_svd.xip_ssi.rxoicr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RXOICR_Register is record\n   RXOICR        : Boolean;\n   Reserved_1_31 : HAL.UInt31;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "RXUICR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.RXUICR_Register",
       signature: "rp2040_svd.xip_ssi.rxuicr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RXUICR_Register is record\n   RXUICR        : Boolean;\n   Reserved_1_31 : HAL.UInt31;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SER_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.SER_Register",
       signature: "rp2040_svd.xip_ssi.ser_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SER_Register is record\n   SER           : Boolean := False;\n   Reserved_1_31 : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SPI_CTRLR0_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_Register",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SPI_CTRLR0_Register is record\n   TRANS_TYPE     : SPI_CTRLR0_TRANS_TYPE_Field :=\n                     RP2040_SVD.XIP_SSI.Val_1C1A;\n   ADDR_L         : SPI_CTRLR0_ADDR_L_Field := 16#0#;\n   Reserved_6_7   : HAL.UInt2 := 16#0#;\n   INST_L         : SPI_CTRLR0_INST_L_Field := RP2040_SVD.XIP_SSI.NONE;\n   Reserved_10_10 : HAL.Bit := 16#0#;\n   WAIT_CYCLES    : SPI_CTRLR0_WAIT_CYCLES_Field := 16#0#;\n   SPI_DDR_EN     : Boolean := False;\n   INST_DDR_EN    : Boolean := False;\n   SPI_RXDS_EN    : Boolean := False;\n   Reserved_19_23 : HAL.UInt5 := 16#0#;\n   XIP_CMD        : SPI_CTRLR0_XIP_CMD_Field := 16#3#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.SR_Register",
       signature: "rp2040_svd.xip_ssi.sr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SR_Register is record\n   BUSY          : Boolean;\n   TFNF          : Boolean;\n   TFE           : Boolean;\n   RFNE          : Boolean;\n   RFF           : Boolean;\n   TXE           : Boolean;\n   DCOL          : Boolean;\n   Reserved_7_31 : HAL.UInt25;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "SSIENR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.SSIENR_Register",
       signature: "rp2040_svd.xip_ssi.ssienr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type SSIENR_Register is record\n   SSI_EN        : Boolean := False;\n   Reserved_1_31 : HAL.UInt31 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TXD_DRIVE_EDGE_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.TXD_DRIVE_EDGE_Register",
       signature: "rp2040_svd.xip_ssi.txd_drive_edge_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TXD_DRIVE_EDGE_Register is record\n   TDE           : TXD_DRIVE_EDGE_TDE_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TXFLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.TXFLR_Register",
       signature: "rp2040_svd.xip_ssi.txflr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TXFLR_Register is record\n   TFTFL         : TXFLR_TFTFL_Field;\n   Reserved_8_31 : HAL.UInt24;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TXFTLR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.TXFTLR_Register",
       signature: "rp2040_svd.xip_ssi.txftlr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TXFTLR_Register is record\n   TFT           : TXFTLR_TFT_Field := 16#0#;\n   Reserved_8_31 : HAL.UInt24 := 16#0#;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "TXOICR_Register",
       qualified_name: "RP2040_SVD.XIP_SSI.TXOICR_Register",
       signature: "rp2040_svd.xip_ssi.txoicr_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TXOICR_Register is record\n   TXOICR        : Boolean;\n   Reserved_1_31 : HAL.UInt31;\nend record\n  with Volatile_Full_Access, Object_Size => 32,\n       Bit_Order => System.Low_Order_First;",
       }   ,
       {
       name: "XIP_SSI_Peripheral",
       qualified_name: "RP2040_SVD.XIP_SSI.XIP_SSI_Peripheral",
       signature: "rp2040_svd.xip_ssi.xip_ssi_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type XIP_SSI_Peripheral is record\n   CTRLR0         : aliased CTRLR0_Register;\n   CTRLR1         : aliased CTRLR1_Register;\n   SSIENR         : aliased SSIENR_Register;\n   MWCR           : aliased MWCR_Register;\n   SER            : aliased SER_Register;\n   BAUDR          : aliased BAUDR_Register;\n   TXFTLR         : aliased TXFTLR_Register;\n   RXFTLR         : aliased RXFTLR_Register;\n   TXFLR          : aliased TXFLR_Register;\n   RXFLR          : aliased RXFLR_Register;\n   SR             : aliased SR_Register;\n   IMR            : aliased IMR_Register;\n   ISR            : aliased ISR_Register;\n   RISR           : aliased RISR_Register;\n   TXOICR         : aliased TXOICR_Register;\n   RXOICR         : aliased RXOICR_Register;\n   RXUICR         : aliased RXUICR_Register;\n   MSTICR         : aliased MSTICR_Register;\n   ICR            : aliased ICR_Register;\n   DMACR          : aliased DMACR_Register;\n   DMATDLR        : aliased DMATDLR_Register;\n   DMARDLR        : aliased DMARDLR_Register;\n   IDR            : aliased HAL.UInt32;\n   SSI_VERSION_ID : aliased HAL.UInt32;\n   DR0            : aliased HAL.UInt32;\n   RX_SAMPLE_DLY  : aliased RX_SAMPLE_DLY_Register;\n   SPI_CTRLR0     : aliased SPI_CTRLR0_Register;\n   TXD_DRIVE_EDGE : aliased TXD_DRIVE_EDGE_Register;\nend record\n  with Volatile;",
       }   ,
   ]
,subtypes:    [
       {
       name: "BAUDR_SCKDV_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.BAUDR_SCKDV_Field",
       signature: "rp2040_svd.xip_ssi.baudr_sckdv_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BAUDR_SCKDV_Field is HAL.UInt16;",
       }   ,
       {
       name: "CTRLR0_CFS_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_CFS_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_cfs_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRLR0_CFS_Field is HAL.UInt4;",
       }   ,
       {
       name: "CTRLR0_DFS_32_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_DFS_32_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_dfs_32_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRLR0_DFS_32_Field is HAL.UInt5;",
       }   ,
       {
       name: "CTRLR0_DFS_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_DFS_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_dfs_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRLR0_DFS_Field is HAL.UInt4;",
       }   ,
       {
       name: "CTRLR0_FRF_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR0_FRF_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr0_frf_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRLR0_FRF_Field is HAL.UInt2;",
       }   ,
       {
       name: "CTRLR1_NDF_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.CTRLR1_NDF_Field",
       signature: "rp2040_svd.xip_ssi.ctrlr1_ndf_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype CTRLR1_NDF_Field is HAL.UInt16;",
       }   ,
       {
       name: "DMARDLR_DMARDL_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.DMARDLR_DMARDL_Field",
       signature: "rp2040_svd.xip_ssi.dmardlr_dmardl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DMARDLR_DMARDL_Field is HAL.UInt8;",
       }   ,
       {
       name: "DMATDLR_DMATDL_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.DMATDLR_DMATDL_Field",
       signature: "rp2040_svd.xip_ssi.dmatdlr_dmatdl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype DMATDLR_DMATDL_Field is HAL.UInt8;",
       }   ,
       {
       name: "RX_SAMPLE_DLY_RSD_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.RX_SAMPLE_DLY_RSD_Field",
       signature: "rp2040_svd.xip_ssi.rx_sample_dly_rsd_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype RX_SAMPLE_DLY_RSD_Field is HAL.UInt8;",
       }   ,
       {
       name: "RXFLR_RXTFL_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.RXFLR_RXTFL_Field",
       signature: "rp2040_svd.xip_ssi.rxflr_rxtfl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype RXFLR_RXTFL_Field is HAL.UInt8;",
       }   ,
       {
       name: "RXFTLR_RFT_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.RXFTLR_RFT_Field",
       signature: "rp2040_svd.xip_ssi.rxftlr_rft_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype RXFTLR_RFT_Field is HAL.UInt8;",
       }   ,
       {
       name: "SPI_CTRLR0_ADDR_L_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_ADDR_L_Field",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_addr_l_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SPI_CTRLR0_ADDR_L_Field is HAL.UInt4;",
       }   ,
       {
       name: "SPI_CTRLR0_WAIT_CYCLES_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_WAIT_CYCLES_Field",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_wait_cycles_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SPI_CTRLR0_WAIT_CYCLES_Field is HAL.UInt5;",
       }   ,
       {
       name: "SPI_CTRLR0_XIP_CMD_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.SPI_CTRLR0_XIP_CMD_Field",
       signature: "rp2040_svd.xip_ssi.spi_ctrlr0_xip_cmd_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SPI_CTRLR0_XIP_CMD_Field is HAL.UInt8;",
       }   ,
       {
       name: "TXD_DRIVE_EDGE_TDE_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.TXD_DRIVE_EDGE_TDE_Field",
       signature: "rp2040_svd.xip_ssi.txd_drive_edge_tde_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TXD_DRIVE_EDGE_TDE_Field is HAL.UInt8;",
       }   ,
       {
       name: "TXFLR_TFTFL_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.TXFLR_TFTFL_Field",
       signature: "rp2040_svd.xip_ssi.txflr_tftfl_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TXFLR_TFTFL_Field is HAL.UInt8;",
       }   ,
       {
       name: "TXFTLR_TFT_Field",
       qualified_name: "RP2040_SVD.XIP_SSI.TXFTLR_TFT_Field",
       signature: "rp2040_svd.xip_ssi.txftlr_tft_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype TXFTLR_TFT_Field is HAL.UInt8;",
       }   ,
   ]
,variables:    [
       {
       name: "XIP_SSI_Periph",
       qualified_name: "RP2040_SVD.XIP_SSI.XIP_SSI_Periph",
       signature: "rp2040_svd.xip_ssi.xip_ssi_periph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "XIP_SSI_Periph : aliased XIP_SSI_Peripheral\n  with Import, Address => XIP_SSI_Base;",
       }   ,
   ]
,}
---
