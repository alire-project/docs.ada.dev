---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.RTC",
qualified_name: "RP.RTC",
signature: "rp.rtc",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "RTC_Alarm_Mask",
       qualified_name: "RP.RTC.RTC_Alarm_Mask",
       signature: "rp.rtc.rtc_alarm_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Alarm_Mask is record\n   Year        : Boolean := True;\n   Month       : Boolean := True;\n   Day         : Boolean := True;\n   Day_Of_Week : Boolean := True;\n   Hour        : Boolean := True;\n   Min         : Boolean := True;\n   Sec         : Boolean := True;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "RTC_Device",
       qualified_name: "RP.RTC.RTC_Device",
       signature: "rp.rtc.rtc_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Device is new HAL.Real_Time_Clock.RTC_Device with null record;",
       }   ,
   ]
,}
---
