---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Array_Alloc",
qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc",
signature: "langkit_support.generic_bump_ptr.array_alloc",
enclosing: "langkit_support.generic_bump_ptr",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Element_Array",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Element_Array",
       signature: "langkit_support.generic_bump_ptr.array_alloc.element_array",
       enclosing: "",
       is_private: false,
       documentation: "This package handles unsized array types to avoid having to deal with\nfat pointers.",
       documentation_snippet: "type Element_Array is array (Index_Type) of Element_T;",
       }   ,
   ]
,access_types:    [
       {
       name: "Element_Array_Access",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Element_Array_Access",
       signature: "langkit_support.generic_bump_ptr.array_alloc.element_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Array_Access is access all Element_Array;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Array_Access",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Empty_Array_Access",
       signature: "langkit_support.generic_bump_ptr.array_alloc.empty_array_access",
       enclosing: "",
       is_private: false,
       documentation: "Access to an empty array. As accessing its elements is forbidden, but\ndereferencing it to take an empty slice is allowed, it is designed to\npoint to a non-null junk address.",
       documentation_snippet: "Empty_Array_Access : constant Element_Array_Access := To_Pointer\n  (System.Null_Address + 1);",
       }   ,
   ]
,}
---
