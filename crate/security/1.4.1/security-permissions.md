---
crate: security
layout: gnatdoc
gnatdoc: {
name: "Security.Permissions",
qualified_name: "Security.Permissions",
signature: "security.permissions",
enclosing: "security",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Definition",
       qualified_name: "Security.Permissions.Definition",
       signature: "security.permissions.definition",
       enclosing: "security.permissions",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Permission_Index",
       qualified_name: "Security.Permissions.Permission_Index",
       signature: "security.permissions.permission_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permission_Index is new Natural range 0 .. MAX_PERMISSION;",
       }   ,
       {
       name: "Permission_Index_Set",
       qualified_name: "Security.Permissions.Permission_Index_Set",
       signature: "security.permissions.permission_index_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permission_Index_Set is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Permission_Index_Array",
       qualified_name: "Security.Permissions.Permission_Index_Array",
       signature: "security.permissions.permission_index_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permission_Index_Array is array (Positive range <>) of Permission_Index;",
       }   ,
   ]
,record_types:    [
       {
       name: "Permission",
       qualified_name: "Security.Permissions.Permission",
       signature: "security.permissions.permission",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Permission (Id : Permission_Index) is tagged limited null record;",
       }   ,
   ]
,constants:    [
       {
       name: "EMPTY_SET",
       qualified_name: "Security.Permissions.EMPTY_SET",
       signature: "security.permissions.empty_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "EMPTY_SET : constant Permission_Index_Set;",
       }   ,
       {
       name: "MAX_PERMISSION",
       qualified_name: "Security.Permissions.MAX_PERMISSION",
       signature: "security.permissions.max_permission",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_PERMISSION : constant Natural := 255;",
       }   ,
       {
       name: "NONE",
       qualified_name: "Security.Permissions.NONE",
       signature: "security.permissions.none",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "NONE : constant Permission_Index := Permission_Index'First;",
       }   ,
   ]
,}
---
