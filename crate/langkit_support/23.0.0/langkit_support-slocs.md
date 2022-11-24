---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Slocs",
qualified_name: "Langkit_Support.Slocs",
signature: "langkit_support.slocs",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Column_Number",
       qualified_name: "Langkit_Support.Slocs.Column_Number",
       signature: "langkit_support.slocs.column_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Column_Number is mod 2 ** 16;",
       }   ,
       {
       name: "Line_Number",
       qualified_name: "Langkit_Support.Slocs.Line_Number",
       signature: "langkit_support.slocs.line_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line_Number is mod 2 ** 32;",
       }   ,
       {
       name: "Relative_Position",
       qualified_name: "Langkit_Support.Slocs.Relative_Position",
       signature: "langkit_support.slocs.relative_position",
       enclosing: "",
       is_private: false,
       documentation: "Where some source location is with respect to another/a source location\nrange.\n\n@enum Before\n@enum Inside\n@enum After",
       documentation_snippet: "type Relative_Position is (Before, Inside, After);",
       }   ,
   ]
,record_types:    [
       {
       name: "Source_Location",
       qualified_name: "Langkit_Support.Slocs.Source_Location",
       signature: "langkit_support.slocs.source_location",
       enclosing: "",
       is_private: false,
       documentation: "Type representing a location in the source\n\n@field Line\n  Line for this source location\n@field Column",
       documentation_snippet: "type Source_Location is record\n   Line   : Line_Number;\n   Column : Column_Number;\nend record;",
       }   ,
       {
       name: "Source_Location_Range",
       qualified_name: "Langkit_Support.Slocs.Source_Location_Range",
       signature: "langkit_support.slocs.source_location_range",
       enclosing: "",
       is_private: false,
       documentation: "Type representing a range in the source\n\n@field Start_Line\n  Start and end lines for this source location\n@field End_Line\n  Start and end lines for this source location\n@field Start_Column\n@field End_Column",
       documentation_snippet: "type Source_Location_Range is record\n   Start_Line, End_Line     : Line_Number;\n   Start_Column, End_Column : Column_Number;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Tab_Stop",
       qualified_name: "Langkit_Support.Slocs.Default_Tab_Stop",
       signature: "langkit_support.slocs.default_tab_stop",
       enclosing: "",
       is_private: false,
       documentation: "Value that will be used for the default tab stop if none is passed\nduring the initialization of a ``Token_Data_Handler``.",
       documentation_snippet: "Default_Tab_Stop : constant Positive := 8;",
       }   ,
       {
       name: "No_Source_Location",
       qualified_name: "Langkit_Support.Slocs.No_Source_Location",
       signature: "langkit_support.slocs.no_source_location",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Source_Location       : constant Source_Location       := (0, 0);",
       }   ,
       {
       name: "No_Source_Location_Range",
       qualified_name: "Langkit_Support.Slocs.No_Source_Location_Range",
       signature: "langkit_support.slocs.no_source_location_range",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Source_Location_Range : constant Source_Location_Range := (0, 0, 0, 0);",
       }   ,
   ]
,}
---
