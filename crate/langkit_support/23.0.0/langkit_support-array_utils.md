---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Array_Utils",
qualified_name: "Langkit_Support.Array_Utils",
signature: "langkit_support.array_utils",
enclosing: "langkit_support",
is_private: false,
documentation: "This package provides a standardized array type (starting at index 0) along\nwith a host of functional primitives to manipulate instances of this\narray. Functional transformations are a more natural way to express some\ntransformations (filters for example), and, thanks to Ada's secondary stack\nbased arrays, can be much faster than the dynamic vector counterpart.\n\nFor example, given the following imperative code::\n\n   Input  : Vector;\n   Output : Vector;\n\n   for El of Input loop\n      if Predicate (El) then\n         Output.Append (El);\n      end if;\n   end loop;\n\nYou could do the same thing in a functional way with this module, like so::\n\n   Input  : Array_Type;\n   Output : Array_Type := Filter (Input, Predicate'Access)\n\nThe module generally provides two ways to use a higher order primitive:\n\n1. The first is by using the dynamic version of the primitive, that takes\n   an access to the subprogram(s) it is going to need. For filter, it will\n   be the Filter primitive.\n\n2. The second is to use the generic version of the primitive, that will\n   take the subprograms as generic parameters. Those versions end with the\n   _Gen suffix. For filter, it will be Filter_Gen. Those versions are\n   faster, because the front-end is able to inline the parameter\n   subprograms inside the call.\n\n@formal Element_Type\n@formal Index_Type\n@formal Array_Type\n@formal \"=\"",
documentation_snippet: "",
record_types:    [
       {
       name: "Option_Type",
       qualified_name: "Langkit_Support.Array_Utils.Option_Type",
       signature: "langkit_support.array_utils.option_type",
       enclosing: "",
       is_private: false,
       documentation: "Basic option type, that can either contain an element or nothing\n\n@field Has_Element\n@field Element",
       documentation_snippet: "type Option_Type (Has_Element : Boolean) is record\n   case Has_Element is\n   when True =>\n      Element : Element_Type;\n   when False => null;\n   end case;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Extended_Index",
       qualified_name: "Langkit_Support.Array_Utils.Extended_Index",
       signature: "langkit_support.array_utils.extended_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Extended_Index is Index_Type'Base;",
       }   ,
   ]
,constants:    [
       {
       name: "Empty_Array",
       qualified_name: "Langkit_Support.Array_Utils.Empty_Array",
       signature: "langkit_support.array_utils.empty_array",
       enclosing: "",
       is_private: false,
       documentation: "Constant for the empty array",
       documentation_snippet: "Empty_Array : constant Array_Type\n  (Index_Type'Succ (Index_Type'First) .. Index_Type'First)\n    := (others => <>);",
       }   ,
       {
       name: "None",
       qualified_name: "Langkit_Support.Array_Utils.None",
       signature: "langkit_support.array_utils.none",
       enclosing: "",
       is_private: false,
       documentation: "Constant for the empty Option type",
       documentation_snippet: "None : constant Option_Type := (Has_Element => False);",
       }   ,
   ]
,}
---
