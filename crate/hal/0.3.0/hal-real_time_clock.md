---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.Real_Time_Clock",
qualified_name: "HAL.Real_Time_Clock",
signature: "hal.real_time_clock",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                        Copyright (C) 2016, AdaCore                       --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "RTC_Day",
       qualified_name: "HAL.Real_Time_Clock.RTC_Day",
       signature: "hal.real_time_clock.rtc_day",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Day is range 1 .. 31;",
       }   ,
       {
       name: "RTC_Day_Of_Week",
       qualified_name: "HAL.Real_Time_Clock.RTC_Day_Of_Week",
       signature: "hal.real_time_clock.rtc_day_of_week",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Day_Of_Week is (Monday, Tuesday, Wednesday, Thursday, Friday,\n                         Saturday, Sunday);",
       }   ,
       {
       name: "RTC_Hour",
       qualified_name: "HAL.Real_Time_Clock.RTC_Hour",
       signature: "hal.real_time_clock.rtc_hour",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Hour is mod 24;",
       }   ,
       {
       name: "RTC_Minute",
       qualified_name: "HAL.Real_Time_Clock.RTC_Minute",
       signature: "hal.real_time_clock.rtc_minute",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Minute is mod 60;",
       }   ,
       {
       name: "RTC_Month",
       qualified_name: "HAL.Real_Time_Clock.RTC_Month",
       signature: "hal.real_time_clock.rtc_month",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Month is (January, February, March, April, May, June, July, August,\n                   September, October, November, December);",
       }   ,
       {
       name: "RTC_Second",
       qualified_name: "HAL.Real_Time_Clock.RTC_Second",
       signature: "hal.real_time_clock.rtc_second",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Second is mod 60;",
       }   ,
       {
       name: "RTC_Year",
       qualified_name: "HAL.Real_Time_Clock.RTC_Year",
       signature: "hal.real_time_clock.rtc_year",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Year is range 00 .. 99;",
       }   ,
   ]
,record_types:    [
       {
       name: "RTC_Date",
       qualified_name: "HAL.Real_Time_Clock.RTC_Date",
       signature: "hal.real_time_clock.rtc_date",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Date is record\n   Day_Of_Week : RTC_Day_Of_Week;\n   Day         : RTC_Day;\n   Month       : RTC_Month;\n   Year        : RTC_Year;\nend record;",
       }   ,
       {
       name: "RTC_Time",
       qualified_name: "HAL.Real_Time_Clock.RTC_Time",
       signature: "hal.real_time_clock.rtc_time",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Time is record\n   Hour : RTC_Hour;\n   Min  : RTC_Minute;\n   Sec  : RTC_Second;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "RTC_Device",
       qualified_name: "HAL.Real_Time_Clock.RTC_Device",
       signature: "hal.real_time_clock.rtc_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type RTC_Device is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_RTC_Device",
       qualified_name: "HAL.Real_Time_Clock.Any_RTC_Device",
       signature: "hal.real_time_clock.any_rtc_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_RTC_Device is access all RTC_Device'Class;",
       }   ,
   ]
,}
---
