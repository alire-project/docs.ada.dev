---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Boxes",
qualified_name: "Langkit_Support.Boxes",
signature: "langkit_support.boxes",
enclosing: "langkit_support",
is_private: false,
documentation: "This package provides a simple implementation for boxing types: types that\nare dynamically allocated, handled by reference and with automatic memory\nmanagement thanks to reference counting.\n\nThe main difference with GNATCOLL.Refcount is that here, Element_Type is\nlimited and constrained while in GNATCOLL.Refcount, Element_Type is not\nlimited and unconstrained.\n\n@formal Element_Type\n  The type to be boxed\n@formal Refcount\n  Return Self's reference count\n@formal Set_Refcount\n  Set Self's reference count to Count\n@formal Release\n  Release all resources in Element_Type. This is called when the reference\n  count drops to 0.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Reference",
       qualified_name: "Langkit_Support.Boxes.Reference",
       signature: "langkit_support.boxes.reference",
       enclosing: "",
       is_private: false,
       documentation: "Ref-counted reference to an Element_Type value",
       documentation_snippet: "type Reference is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Element_Access",
       qualified_name: "Langkit_Support.Boxes.Element_Access",
       signature: "langkit_support.boxes.element_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Access is access all Element_Type;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Reference",
       qualified_name: "Langkit_Support.Boxes.No_Reference",
       signature: "langkit_support.boxes.no_reference",
       enclosing: "",
       is_private: false,
       documentation: "Null reference (no element is referenced)",
       documentation_snippet: "No_Reference : constant Reference;",
       }   ,
   ]
,}
---
