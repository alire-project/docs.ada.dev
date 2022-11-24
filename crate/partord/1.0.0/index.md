---
crate: partord
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Partial_Order_Sorting",
    qualified_name: "Partial_Order_Sorting",
    signature: "partial_order_sorting",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Partial_Order_Sorting.Array_Sort",
    qualified_name: "Partial_Order_Sorting.Array_Sort",
    signature: "partial_order_sorting.array_sort",
    enclosing: "partial_order_sorting",
    is_private: false,
    documentation: "\nSort the elements in Item in \"decreasing\" order in the sense that\nif Sort'result(I) < Sort'result(j) then it must be I > J.  Yes,\nit looks like a usual ordering, but in this case \"<\" can be partial,\nthat is, it is not necessarily true that if A /= B then it must\nbe A<B or A > B.  Think about, for example, sets ordered by inclusion.\n\n@formal Index_Type\n@formal Element_Type\n@formal Container_Type\n@formal \"<\"\n  with function Image (X : Element_Type) return String;",
    documentation_snippet: "",
    },
]
}
---
