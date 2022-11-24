---
crate: adl_middleware
layout: gnatdoc
gnatdoc: {
name: "Bluetooth_Low_Energy",
qualified_name: "Bluetooth_Low_Energy",
signature: "bluetooth_low_energy",
enclosing: "",
is_private: false,
documentation: "------------\n Channels --\n------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "BLE_Channel_Number",
       qualified_name: "Bluetooth_Low_Energy.BLE_Channel_Number",
       signature: "bluetooth_low_energy.ble_channel_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BLE_Channel_Number is range 0 .. 39;",
       }   ,
       {
       name: "BLE_Frequency_MHz",
       qualified_name: "Bluetooth_Low_Energy.BLE_Frequency_MHz",
       signature: "bluetooth_low_energy.ble_frequency_mhz",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BLE_Frequency_MHz is range 2402 .. 2480;",
       }   ,
       {
       name: "BLE_UUID_Kind",
       qualified_name: "Bluetooth_Low_Energy.BLE_UUID_Kind",
       signature: "bluetooth_low_energy.ble_uuid_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BLE_UUID_Kind is (UUID_16bits, UUID_32bits, UUID_16UInt8s);",
       }   ,
   ]
,record_types:    [
       {
       name: "BLE_UUID",
       qualified_name: "Bluetooth_Low_Energy.BLE_UUID",
       signature: "bluetooth_low_energy.ble_uuid",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type BLE_UUID (Kind : BLE_UUID_Kind) is record\n   case Kind is\n      when UUID_16bits =>\n         UUID_16 : UInt16;\n      when UUID_32bits =>\n         UUID_32 : UInt32;\n      when UUID_16UInt8s =>\n         UUID_16_UInt8s : BLE_16UInt8s_UUID;\n   end case;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "BLE_16UInt8s_UUID",
       qualified_name: "Bluetooth_Low_Energy.BLE_16UInt8s_UUID",
       signature: "bluetooth_low_energy.ble_16uint8s_uuid",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BLE_16UInt8s_UUID is UInt8_Array (1 .. 16);",
       }   ,
       {
       name: "BLE_Advertising_Channel_Number",
       qualified_name: "Bluetooth_Low_Energy.BLE_Advertising_Channel_Number",
       signature: "bluetooth_low_energy.ble_advertising_channel_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BLE_Advertising_Channel_Number is BLE_Channel_Number range 37 .. 39;",
       }   ,
       {
       name: "BLE_Data_Channel_Number",
       qualified_name: "Bluetooth_Low_Energy.BLE_Data_Channel_Number",
       signature: "bluetooth_low_energy.ble_data_channel_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype BLE_Data_Channel_Number is BLE_Channel_Number range 0 .. 36;",
       }   ,
   ]
,variables:    [
       {
       name: "Channel_Frequency",
       qualified_name: "Bluetooth_Low_Energy.Channel_Frequency",
       signature: "bluetooth_low_energy.channel_frequency",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Channel_Frequency : array (BLE_Channel_Number) of BLE_Frequency_MHz :=\n  (0 => 2404,  1 => 2406,  2 => 2408,  3 => 2410,  4 => 2412,\n   5 => 2414,  6 => 2416,  7 => 2418,  8 => 2420,  9 => 2422,\n  10 => 2424, 11 => 2428, 12 => 2430, 13 => 2432, 14 => 2434,\n  15 => 2436, 16 => 2438, 17 => 2440, 18 => 2442, 19 => 2444,\n  20 => 2446, 21 => 2448, 22 => 2450, 23 => 2452, 24 => 2454,\n  25 => 2456, 26 => 2458, 27 => 2460, 28 => 2462, 29 => 2464,\n  30 => 2466, 31 => 2468, 32 => 2470, 33 => 2472, 34 => 2474,\n  35 => 2476, 36 => 2478, 37 => 2402, 38 => 2426, 39 => 2480);",
       }   ,
   ]
,}
---
