---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Generic_Bump_Ptr",
qualified_name: "Langkit_Support.Generic_Bump_Ptr",
signature: "langkit_support.generic_bump_ptr",
enclosing: "langkit_support",
is_private: false,
documentation: "-----------------------------------\n  Generic (and fast) ad-hoc pool --\n-----------------------------------\n\n@formal Page_Size\n  This constant has been chosen heuristically to be the lowest value that\n  gives the best performance. Bigger values did not make any difference,\n  and that way we ensure that pools can stay small.",
documentation_snippet: "",
packages:    [
       {
       name: "Alloc",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Alloc",
       signature: "langkit_support.generic_bump_ptr.alloc",
       enclosing: "langkit_support.generic_bump_ptr",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
       {
       name: "Array_Alloc",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc",
       signature: "langkit_support.generic_bump_ptr.array_alloc",
       enclosing: "langkit_support.generic_bump_ptr",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
array_types:           [
              {
              name: "Element_Array",
              qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Element_Array",
              signature: "langkit_support.generic_bump_ptr.array_alloc.element_array",
              enclosing: "",
              is_private: false,
              documentation: "This package handles unsized array types to avoid having to deal with\nfat pointers.",
              documentation_snippet: "type Element_Array is array (Index_Type) of Element_T;",
              }          ,
          ]
,access_types:           [
              {
              name: "Element_Array_Access",
              qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Element_Array_Access",
              signature: "langkit_support.generic_bump_ptr.array_alloc.element_array_access",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Element_Array_Access is access all Element_Array;",
              }          ,
          ]
,constants:           [
              {
              name: "Empty_Array_Access",
              qualified_name: "Langkit_Support.Generic_Bump_Ptr.Array_Alloc.Empty_Array_Access",
              signature: "langkit_support.generic_bump_ptr.array_alloc.empty_array_access",
              enclosing: "",
              is_private: false,
              documentation: "Access to an empty array. As accessing its elements is forbidden, but\ndereferencing it to take an empty slice is allowed, it is designed to\npoint to a non-null junk address.",
              documentation_snippet: "Empty_Array_Access : constant Element_Array_Access := To_Pointer\n  (System.Null_Address + 1);",
              }          ,
          ]
,       }   ,
       {
       name: "Tagged_Alloc",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Tagged_Alloc",
       signature: "langkit_support.generic_bump_ptr.tagged_alloc",
       enclosing: "langkit_support.generic_bump_ptr",
       is_private: false,
       documentation: "",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Bump_Ptr_Pool",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Bump_Ptr_Pool",
       signature: "langkit_support.generic_bump_ptr.bump_ptr_pool",
       enclosing: "",
       is_private: false,
       documentation: "This type is a handle to a subpool. You need to initialize it via a call\nto Create.",
       documentation_snippet: "type Bump_Ptr_Pool is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Ada_Bump_Ptr_Pool",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.Ada_Bump_Ptr_Pool",
       signature: "langkit_support.generic_bump_ptr.ada_bump_ptr_pool",
       enclosing: "",
       is_private: false,
       documentation: "This type is meant to be used as a storage pool. See section 6.4 of the\nAda 2012 rationale for details. Here is a basic example of the use::\n\n   Root_Pool : Ada_Bump_Ptr_Pool;\n   type Int_Access is access all Integer;\n   for Int_Access'Storage_Pool use Root_Pool;\n\n   Subpool   : Pool_Handle := Create_Subpool (Root_Pool);\n\n   A : Int_Access := new (Subpool) Integer'(42);\n\nWhile the performance is still improved when compared to regular\nmalloc/free, it is much slower than the ad-hoc mechanism, so\ncoherent use cases might be:\n\n- When you cannot use the ad-hoc mechanism because of the type of\n  objects you want to allocate.\n\n- When you don't care about the performance but still want the\n  simplified memory management that this kind of pools provide.",
       documentation_snippet: "type Ada_Bump_Ptr_Pool is new Root_Storage_Pool_With_Subpools\nwith null record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Pool",
       qualified_name: "Langkit_Support.Generic_Bump_Ptr.No_Pool",
       signature: "langkit_support.generic_bump_ptr.no_pool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Pool : constant Bump_Ptr_Pool;",
       }   ,
   ]
,}
---
