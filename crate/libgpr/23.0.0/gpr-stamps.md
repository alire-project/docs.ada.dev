---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "Stamps",
qualified_name: "GPR.Stamps",
signature: "gpr.stamps",
enclosing: "gpr",
is_private: false,
documentation: "---------------------------------\n Representation of Time Stamps --\n---------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Time_Stamp_Type",
       qualified_name: "GPR.Stamps.Time_Stamp_Type",
       signature: "gpr.stamps.time_stamp_type",
       enclosing: "",
       is_private: false,
       documentation: "Type used to represent time stamp",
       documentation_snippet: "type Time_Stamp_Type is new String (Time_Stamp_Index);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Time_Stamp_Index",
       qualified_name: "GPR.Stamps.Time_Stamp_Index",
       signature: "gpr.stamps.time_stamp_index",
       enclosing: "",
       is_private: false,
       documentation: "Type used to represent time stamp",
       documentation_snippet: "subtype Time_Stamp_Index is Natural range 1 .. Time_Stamp_Length;",
       }   ,
   ]
,constants:    [
       {
       name: "Dummy_Time_Stamp",
       qualified_name: "GPR.Stamps.Dummy_Time_Stamp",
       signature: "gpr.stamps.dummy_time_stamp",
       enclosing: "",
       is_private: false,
       documentation: "This is used for dummy time stamp values used in the D lines for\nnon-existent files, and is intended to be an impossible value.",
       documentation_snippet: "Dummy_Time_Stamp : constant Time_Stamp_Type := (others => '0');",
       }   ,
       {
       name: "Empty_Time_Stamp",
       qualified_name: "GPR.Stamps.Empty_Time_Stamp",
       signature: "gpr.stamps.empty_time_stamp",
       enclosing: "",
       is_private: false,
       documentation: "Value representing an empty or missing time stamp. Looks less than\nany real time stamp if two time stamps are compared. Note that\nalthough this is not private, clients should not rely on the exact\nway in which this string is represented, and instead should use the\nsubprograms below.\nNote : the Empty_Time_Stamp value less than any non-empty time stamp\nvalue.",
       documentation_snippet: "Empty_Time_Stamp : constant Time_Stamp_Type := (others => ' ');",
       }   ,
       {
       name: "Time_Stamp_Length",
       qualified_name: "GPR.Stamps.Time_Stamp_Length",
       signature: "gpr.stamps.time_stamp_length",
       enclosing: "",
       is_private: false,
       documentation: "Length of time stamp value",
       documentation_snippet: "Time_Stamp_Length : constant := 14;",
       }   ,
   ]
,}
---
