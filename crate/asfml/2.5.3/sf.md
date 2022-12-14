---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf",
qualified_name: "Sf",
signature: "sf",
enclosing: "",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n // Define the CSFML version\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
simple_types:    [
       {
       name: "sfBool",
       qualified_name: "Sf.sfBool",
       signature: "sf.sfbool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfBool is new Boolean;",
       }   ,
       {
       name: "sfInt16",
       qualified_name: "Sf.sfInt16",
       signature: "sf.sfint16",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt16 is new Interfaces.Integer_16;",
       }   ,
       {
       name: "sfInt32",
       qualified_name: "Sf.sfInt32",
       signature: "sf.sfint32",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt32 is new Integer;",
       }   ,
       {
       name: "sfInt64",
       qualified_name: "Sf.sfInt64",
       signature: "sf.sfint64",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt64 is new Interfaces.Integer_64;",
       }   ,
       {
       name: "sfInt8",
       qualified_name: "Sf.sfInt8",
       signature: "sf.sfint8",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt8 is range -128 .. 127;",
       }   ,
       {
       name: "sfSize_t",
       qualified_name: "Sf.sfSize_t",
       signature: "sf.sfsize_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSize_t is mod 2 ** Standard'ADDRESS_SIZE;",
       }   ,
       {
       name: "sfUint16",
       qualified_name: "Sf.sfUint16",
       signature: "sf.sfuint16",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint16 is mod 2 ** sfInt16'SIZE;",
       }   ,
       {
       name: "sfUint32",
       qualified_name: "Sf.sfUint32",
       signature: "sf.sfuint32",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint32 is mod 2 ** sfInt32'SIZE;",
       }   ,
       {
       name: "sfUint64",
       qualified_name: "Sf.sfUint64",
       signature: "sf.sfuint64",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint64 is new Interfaces.Unsigned_64;",
       }   ,
       {
       name: "sfUint8",
       qualified_name: "Sf.sfUint8",
       signature: "sf.sfuint8",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint8 is mod 256;",
       }   ,
   ]
,array_types:    [
       {
       name: "sfArrayOfStrings",
       qualified_name: "Sf.sfArrayOfStrings",
       signature: "sf.sfarrayofstrings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfArrayOfStrings is array (sfSize_t range <>) of\n  Ada.Strings.Unbounded.Unbounded_String;",
       }   ,
   ]
,access_types:    [
       {
       name: "sfInt16_Ptr",
       qualified_name: "Sf.sfInt16_Ptr",
       signature: "sf.sfint16_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt16_Ptr is access all sfInt16;",
       }   ,
       {
       name: "sfInt32_Ptr",
       qualified_name: "Sf.sfInt32_Ptr",
       signature: "sf.sfint32_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt32_Ptr is access all sfInt32;",
       }   ,
       {
       name: "sfInt64_Ptr",
       qualified_name: "Sf.sfInt64_Ptr",
       signature: "sf.sfint64_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt64_Ptr is access all sfInt64;",
       }   ,
       {
       name: "sfInt8_Ptr",
       qualified_name: "Sf.sfInt8_Ptr",
       signature: "sf.sfint8_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfInt8_Ptr is access all sfInt8;",
       }   ,
       {
       name: "sfSize_t_Ptr",
       qualified_name: "Sf.sfSize_t_Ptr",
       signature: "sf.sfsize_t_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfSize_t_Ptr is access all sfSize_t;",
       }   ,
       {
       name: "sfUint16_Ptr",
       qualified_name: "Sf.sfUint16_Ptr",
       signature: "sf.sfuint16_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint16_Ptr is access all sfUint16;",
       }   ,
       {
       name: "sfUint32_Ptr",
       qualified_name: "Sf.sfUint32_Ptr",
       signature: "sf.sfuint32_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint32_Ptr is access all sfUint32;",
       }   ,
       {
       name: "sfUint64_Ptr",
       qualified_name: "Sf.sfUint64_Ptr",
       signature: "sf.sfuint64_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint64_Ptr is access all sfUint64;",
       }   ,
       {
       name: "sfUint8_Ptr",
       qualified_name: "Sf.sfUint8_Ptr",
       signature: "sf.sfuint8_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfUint8_Ptr is access all sfUint8;",
       }   ,
   ]
,constants:    [
       {
       name: "Version_Major",
       qualified_name: "Sf.Version_Major",
       signature: "sf.version_major",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Version_Major : constant := 2;",
       }   ,
       {
       name: "Version_Minor",
       qualified_name: "Sf.Version_Minor",
       signature: "sf.version_minor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Version_Minor : constant := 5;",
       }   ,
       {
       name: "Version_Patch",
       qualified_name: "Sf.Version_Patch",
       signature: "sf.version_patch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Version_Patch : constant := 3;",
       }   ,
   ]
,variables:    [
       {
       name: "sfFalse",
       qualified_name: "Sf.sfFalse",
       signature: "sf.sffalse",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfFalse : sfBool renames False;",
       }   ,
       {
       name: "sfTrue",
       qualified_name: "Sf.sfTrue",
       signature: "sf.sftrue",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfTrue  : sfBool renames True;",
       }   ,
   ]
,}
---
