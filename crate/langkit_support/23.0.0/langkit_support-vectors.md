---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Vectors",
qualified_name: "Langkit_Support.Vectors",
signature: "langkit_support.vectors",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0\n\n@formal Element_Type\n@formal Small_Vector_Capacity",
documentation_snippet: "",
array_types:    [
       {
       name: "Elements_Array",
       qualified_name: "Langkit_Support.Vectors.Elements_Array",
       signature: "langkit_support.vectors.elements_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Elements_Array is array (Index_Type range <>) of Element_Type;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Vector",
       qualified_name: "Langkit_Support.Vectors.Vector",
       signature: "langkit_support.vectors.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector is tagged private\n  with Iterable =>\n    (First       => First_Index,\n     Next        => Next,\n     Has_Element => Has_Element,\n     Element     => Get);",
       }   ,
   ]
,access_types:    [
       {
       name: "Element_Access",
       qualified_name: "Langkit_Support.Vectors.Element_Access",
       signature: "langkit_support.vectors.element_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Access is not null access all Element_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Index_Type",
       qualified_name: "Langkit_Support.Vectors.Index_Type",
       signature: "langkit_support.vectors.index_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Index_Type is Positive;",
       }   ,
       {
       name: "Iteration_Index_Type",
       qualified_name: "Langkit_Support.Vectors.Iteration_Index_Type",
       signature: "langkit_support.vectors.iteration_index_type",
       enclosing: "",
       is_private: false,
       documentation: "Like Index_Type, but also covers zero, which is used to represent a\ndummy last index value for empty vectors.",
       documentation_snippet: "subtype Iteration_Index_Type is Natural;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Vector",
       qualified_name: "Langkit_Support.Vectors.Empty_Vector",
       signature: "langkit_support.vectors.empty_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Vector : constant Vector;",
       }   ,
   ]
,variables:    [
       {
       name: "Empty_Array",
       qualified_name: "Langkit_Support.Vectors.Empty_Array",
       signature: "langkit_support.vectors.empty_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Empty_Array : Elements_Array (1 .. 0) := (others => <>);",
       }   ,
   ]
,}
---
