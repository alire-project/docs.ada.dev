---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Storage_Elements",
qualified_name: "System.Storage_Elements",
signature: "system.storage_elements",
enclosing: "system",
is_private: false,
documentation: "Note that we take advantage of the implementation permission to make\nthis unit Pure instead of Preelaborable; see RM 13.7.1(15). In Ada 2005,\nthis is Pure in any case (AI-362).",
documentation_snippet: "",
simple_types:    [
       {
       name: "Integer_Address",
       qualified_name: "System.Storage_Elements.Integer_Address",
       signature: "system.storage_elements.integer_address",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Integer_Address is mod Memory_Size;",
       }   ,
       {
       name: "Storage_Element",
       qualified_name: "System.Storage_Elements.Storage_Element",
       signature: "system.storage_elements.storage_element",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Element is mod 2 ** Storage_Unit;",
       }   ,
       {
       name: "Storage_Offset",
       qualified_name: "System.Storage_Elements.Storage_Offset",
       signature: "system.storage_elements.storage_offset",
       enclosing: "",
       is_private: false,
       documentation: "Note: the reason for the Long_Long_Integer qualification here is to\navoid a bogus ambiguity when this unit is analyzed in an rtsfind\ncontext. It may be possible to remove this in the future, but it is\ncertainly harmless in any case ???",
       documentation_snippet: "type Storage_Offset is range\n  -(2 ** (Integer'(Standard'Address_Size) - 1)) ..\n  +(2 ** (Integer'(Standard'Address_Size) - 1)) - Long_Long_Integer'(1);",
       }   ,
   ]
,array_types:    [
       {
       name: "Storage_Array",
       qualified_name: "System.Storage_Elements.Storage_Array",
       signature: "system.storage_elements.storage_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Array is\n  array (Storage_Offset range <>) of aliased Storage_Element;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Storage_Count",
       qualified_name: "System.Storage_Elements.Storage_Count",
       signature: "system.storage_elements.storage_count",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Storage_Count is Storage_Offset range 0 .. Storage_Offset'Last;",
       }   ,
   ]
,}
---
