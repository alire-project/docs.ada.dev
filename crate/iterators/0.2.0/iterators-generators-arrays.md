---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Generators.Arrays",
qualified_name: "Iterators.Generators.Arrays",
signature: "iterators.generators.arrays",
enclosing: "iterators.generators",
is_private: false,
documentation: "To avoid duplication of generic profile, and allow use with anonymous\narrays, we require users to cast their arrays to one of the named type\nherein:\n\n@formal Any_Index\n@formal Any_Element",
documentation_snippet: "",
array_types:    [
       {
       name: "Element_Array",
       qualified_name: "Iterators.Generators.Arrays.Element_Array",
       signature: "iterators.generators.arrays.element_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Element_Array is array (Any_Index range <>) of aliased Any_Element;",
       }   ,
   ]
,}
---
