---
crate: edc_client
layout: gnatdoc
gnatdoc: {
name: "Edc_Client",
qualified_name: "Edc_Client",
signature: "edc_client",
enclosing: "",
is_private: false,
documentation: "------------------------------------------------------------------------\n  This is the baud rate for the UART serial interface",
documentation_snippet: "",
access_types:    [
       {
       name: "Transmit_Procedure",
       qualified_name: "Edc_Client.Transmit_Procedure",
       signature: "edc_client.transmit_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Transmit_Procedure is\n  not null access procedure (Control : String);",
       }   ,
   ]
,constants:    [
       {
       name: "SERIAL_BAUD_RATE",
       qualified_name: "Edc_Client.SERIAL_BAUD_RATE",
       signature: "edc_client.serial_baud_rate",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "SERIAL_BAUD_RATE : constant Natural := 115_200;",
       }   ,
   ]
,}
---
