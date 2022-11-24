---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Introspection",
qualified_name: "Libadalang.Introspection",
signature: "libadalang.introspection",
enclosing: "libadalang",
is_private: false,
documentation: "--------------\n Node types --\n--------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Any_Enum_Value_Index",
       qualified_name: "Libadalang.Introspection.Any_Enum_Value_Index",
       signature: "libadalang.introspection.any_enum_value_index",
       enclosing: "",
       is_private: false,
       documentation: "Index of an enum value for a given enum type",
       documentation_snippet: "type Any_Enum_Value_Index is new Natural;",
       }   ,
       {
       name: "Any_Value_Type",
       qualified_name: "Libadalang.Introspection.Any_Value_Type",
       signature: "libadalang.introspection.any_value_type",
       enclosing: "",
       is_private: false,
       documentation: "Polymorphic value to contain ``Kind`` values. This type has by-reference\nsemantics, so copying it is cheap.",
       documentation_snippet: "type Any_Value_Type is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Any_Value_Array",
       qualified_name: "Libadalang.Introspection.Any_Value_Array",
       signature: "libadalang.introspection.any_value_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Value_Array is array (Positive range <>) of Any_Value_Type;",
       }   ,
       {
       name: "Value_Array",
       qualified_name: "Libadalang.Introspection.Value_Array",
       signature: "libadalang.introspection.value_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Value_Array is array (Positive range <>) of Value_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Enum_Value_Index",
       qualified_name: "Libadalang.Introspection.Enum_Value_Index",
       signature: "libadalang.introspection.enum_value_index",
       enclosing: "",
       is_private: false,
       documentation: "Index of an enum value for a given enum type",
       documentation_snippet: "subtype Enum_Value_Index is Any_Enum_Value_Index\n   range 0 ..  Any_Enum_Value_Index'Last;",
       }   ,
       {
       name: "Value_Type",
       qualified_name: "Libadalang.Introspection.Value_Type",
       signature: "libadalang.introspection.value_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Value_Type is Any_Value_Type\n   with Dynamic_Predicate => Value_Type /= No_Value;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Enum_Value_Index",
       qualified_name: "Libadalang.Introspection.No_Enum_Value_Index",
       signature: "libadalang.introspection.no_enum_value_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Enum_Value_Index : constant Any_Enum_Value_Index := 0;",
       }   ,
       {
       name: "No_Value",
       qualified_name: "Libadalang.Introspection.No_Value",
       signature: "libadalang.introspection.no_value",
       enclosing: "",
       is_private: false,
       documentation: "Special ``Any_Value_Type`` to mean: no reference to a value",
       documentation_snippet: "No_Value : constant Any_Value_Type;",
       }   ,
   ]
,}
---
