---
crate: stm32f0x2_hal
layout: gnatdoc
gnatdoc: {
name: "STM32.USB_Btable",
qualified_name: "STM32.USB_Btable",
signature: "stm32.usb_btable",
enclosing: "stm32",
is_private: false,
documentation: "TX",
documentation_snippet: "",
array_types:    [
       {
       name: "Btable_Type",
       qualified_name: "STM32.USB_Btable.Btable_Type",
       signature: "stm32.usb_btable.btable_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Btable_Type is array (UInt4) of EP_Group with\n   Volatile;",
       }   ,
   ]
,record_types:    [
       {
       name: "EP_Group",
       qualified_name: "STM32.USB_Btable.EP_Group",
       signature: "stm32.usb_btable.ep_group",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type EP_Group is record\n   ADDR_TX  : USB_ADDRN_TX_Register;\n   COUNT_TX : USB_COUNTN_TX_Register;\n   ADDR_RX  : USB_ADDRN_RX_Register;\n   COUNT_RX : USB_COUNTN_RX_Register;\nend record with\n   Volatile,\n   Object_Size => 64,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "USB_ADDRN_RX_Register",
       qualified_name: "STM32.USB_Btable.USB_ADDRN_RX_Register",
       signature: "stm32.usb_btable.usb_addrn_rx_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_ADDRN_RX_Register is record\n   ADDRN_RX : ADDRN_RX_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 16,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "USB_ADDRN_TX_Register",
       qualified_name: "STM32.USB_Btable.USB_ADDRN_TX_Register",
       signature: "stm32.usb_btable.usb_addrn_tx_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_ADDRN_TX_Register is record\n   ADDRN_TX : ADDRN_TX_Field := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 16,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "USB_COUNTN_RX_Register",
       qualified_name: "STM32.USB_Btable.USB_COUNTN_RX_Register",
       signature: "stm32.usb_btable.usb_countn_rx_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_COUNTN_RX_Register is record\n   COUNTN_RX : COUNTN_RX_Field := 16#0#;\n   NUM_BLOCK : HAL.UInt5       := 16#0#;\n   BL_SIZE   : HAL.Bit         := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 16,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
       {
       name: "USB_COUNTN_TX_Register",
       qualified_name: "STM32.USB_Btable.USB_COUNTN_TX_Register",
       signature: "stm32.usb_btable.usb_countn_tx_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type USB_COUNTN_TX_Register is record\n   COUNTN_TX  : COUNTN_TX_Field := 16#0#;\n   Reserved_0 : HAL.UInt6       := 16#0#;\nend record with\n   Volatile_Full_Access,\n   Object_Size => 16,\n   Bit_Order   => System.Low_Order_First;",
       }   ,
   ]
,subtypes:    [
       {
       name: "ADDRN_RX_Field",
       qualified_name: "STM32.USB_Btable.ADDRN_RX_Field",
       signature: "stm32.usb_btable.addrn_rx_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ADDRN_RX_Field is HAL.UInt16;",
       }   ,
       {
       name: "ADDRN_TX_Field",
       qualified_name: "STM32.USB_Btable.ADDRN_TX_Field",
       signature: "stm32.usb_btable.addrn_tx_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype ADDRN_TX_Field is HAL.UInt16;",
       }   ,
       {
       name: "COUNTN_RX_Field",
       qualified_name: "STM32.USB_Btable.COUNTN_RX_Field",
       signature: "stm32.usb_btable.countn_rx_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype COUNTN_RX_Field is HAL.UInt10;",
       }   ,
       {
       name: "COUNTN_TX_Field",
       qualified_name: "STM32.USB_Btable.COUNTN_TX_Field",
       signature: "stm32.usb_btable.countn_tx_field",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype COUNTN_TX_Field is HAL.UInt10;",
       }   ,
   ]
,constants:    [
       {
       name: "Btable_Base",
       qualified_name: "STM32.USB_Btable.Btable_Base",
       signature: "stm32.usb_btable.btable_base",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btable_Base : constant System.Address := System'To_Address (16#4000_6000#);",
       }   ,
   ]
,variables:    [
       {
       name: "Btable",
       qualified_name: "STM32.USB_Btable.Btable",
       signature: "stm32.usb_btable.btable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btable : aliased Btable_Type with\n   Import,\n   Address => Btable_Base;",
       }   ,
   ]
,}
---
