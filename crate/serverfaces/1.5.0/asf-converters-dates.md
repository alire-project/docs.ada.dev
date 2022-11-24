---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Converters.Dates",
qualified_name: "ASF.Converters.Dates",
signature: "asf.converters.dates",
enclosing: "asf.converters",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Format_Type",
       qualified_name: "ASF.Converters.Dates.Format_Type",
       signature: "asf.converters.dates.format_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Format_Type is (DATE, TIME, BOTH, CONVERTER_PATTERN, COMPONENT_FORMAT);",
       }   ,
       {
       name: "Style_Type",
       qualified_name: "ASF.Converters.Dates.Style_Type",
       signature: "asf.converters.dates.style_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_Type is (DEFAULT, SHORT, MEDIUM, LONG, FULL);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Date_Converter",
       qualified_name: "ASF.Converters.Dates.Date_Converter",
       signature: "asf.converters.dates.date_converter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Date_Converter is new Converter with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Date_Converter_Access",
       qualified_name: "ASF.Converters.Dates.Date_Converter_Access",
       signature: "asf.converters.dates.date_converter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Date_Converter_Access is access all Date_Converter'Class;",
       }   ,
   ]
,}
---
