---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "Ada.Calendar.Delays",
qualified_name: "Ada.Calendar.Delays",
signature: "ada.calendar.delays",
enclosing: "ada.calendar",
is_private: false,
documentation: "The type declarations here have to match the corresponding type\ndeclarations in AVR.Real_Time.",
documentation_snippet: "",
record_types:    [
       {
       name: "Time",
       qualified_name: "Ada.Calendar.Delays.Time",
       signature: "ada.calendar.delays.time",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Time is record\n   Days : Day_Count;\n   Secs : Duration;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Day_Count",
       qualified_name: "Ada.Calendar.Delays.Day_Count",
       signature: "ada.calendar.delays.day_count",
       enclosing: "",
       is_private: false,
       documentation: "   type Duration is delta 0.001 digits 9 range -24.0 * 3600.0\n.. 48.0 * 3600.0;\n   for Duration'Size use 32;",
       documentation_snippet: "subtype Day_Count is Interfaces.Integer_16;",
       }   ,
   ]
,}
---
