---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Bump_Ptr_Vectors",
qualified_name: "Langkit_Support.Bump_Ptr_Vectors",
signature: "langkit_support.bump_ptr_vectors",
enclosing: "langkit_support",
is_private: false,
documentation: "Beware though, random access is still on the average of 100x slower than in\norder iteration, so *never* use Get_At_Index to iterate over the vector!\n\n@formal Element_Type",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "Langkit_Support.Bump_Ptr_Vectors.Cursor",
       signature: "langkit_support.bump_ptr_vectors.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Vector",
       qualified_name: "Langkit_Support.Bump_Ptr_Vectors.Vector",
       signature: "langkit_support.bump_ptr_vectors.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector is private\n   with Iterable => (First       => First,\n                     Next        => Next,\n                     Has_Element => Has_Element,\n                     Element     => Get);",
       }   ,
   ]
,access_types:    [
       {
       name: "Element_Access",
       qualified_name: "Langkit_Support.Bump_Ptr_Vectors.Element_Access",
       signature: "langkit_support.bump_ptr_vectors.element_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Access is not null access all Element_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Index_Type",
       qualified_name: "Langkit_Support.Bump_Ptr_Vectors.Index_Type",
       signature: "langkit_support.bump_ptr_vectors.index_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Type is Positive;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Cursor",
       qualified_name: "Langkit_Support.Bump_Ptr_Vectors.Empty_Cursor",
       signature: "langkit_support.bump_ptr_vectors.empty_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Cursor : constant Cursor;",
       }   ,
   ]
,}
---
