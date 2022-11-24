---
crate: lvgl_ada_simulator
layout: gnatdoc
gnatdoc: {
name: "Lv.Objx.Calendar",
qualified_name: "Lv.Objx.Calendar",
signature: "lv.objx.calendar",
enclosing: "lv.objx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Style_T",
       qualified_name: "Lv.Objx.Calendar.Style_T",
       signature: "lv.objx.calendar.style_t",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Style_BG\n  Also the style of the \"normal\" date numbers\n@enum Style_HEADER\n@enum Style_HEADER_PR\n@enum Style_DAY_NAMES\n@enum Style_HIGHLIGHTED_DAYS\n@enum Style_INACTIVE_DAYS\n@enum Style_WEEK_BOX\n@enum Style_TODAY_BOX",
       documentation_snippet: "type Style_T is\n (Style_BG,\n  Style_HEADER,\n  Style_HEADER_PR,\n  Style_DAY_NAMES,\n  Style_HIGHLIGHTED_DAYS,\n  Style_INACTIVE_DAYS,\n  Style_WEEK_BOX,\n  Style_TODAY_BOX);",
       }   ,
   ]
,array_types:    [
       {
       name: "Date_Array",
       qualified_name: "Lv.Objx.Calendar.Date_Array",
       signature: "lv.objx.calendar.date_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Date_Array is array (Natural range <>) of aliased Date_T\n  with Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Date_T",
       qualified_name: "Lv.Objx.Calendar.Date_T",
       signature: "lv.objx.calendar.date_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Date_T is record\n   Year  : aliased Uint16_T;\n   Month : aliased Int8_T;\n   Day   : aliased Int8_T;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Instance",
       qualified_name: "Lv.Objx.Calendar.Instance",
       signature: "lv.objx.calendar.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Obj_T;",
       }   ,
   ]
,}
---
