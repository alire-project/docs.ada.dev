---
crate: spark_unbound
layout: gnatdoc_index
gnatdoc: {packages: [
    {
    name: "Spark_Unbound",
    qualified_name: "Spark_Unbound",
    signature: "spark_unbound",
    enclosing: "",
    is_private: false,
    documentation: "",
    documentation_snippet: "",
    },
    {
    name: "Spark_Unbound.Arrays",
    qualified_name: "Spark_Unbound.Arrays",
    signature: "spark_unbound.arrays",
    enclosing: "spark_unbound",
    is_private: false,
    documentation: "needed to use `Self.Arr.all'Old` to prove some contracts\n\n@formal Element_Type\n@formal Index_Type\n  range must be smaller than Natural'Range_Length for overflow prevention (Some kind of compiler restriction would be nice)               \n@formal \"=\"\n  - Function used to compare elements inside `Unbound_Array`s.\n  - @param Left Element that is compared against `Right`.\n  - @param Right Element that is comparef against `Left`.\n  - @return `True` if `Left` and `Right` are equal.",
    documentation_snippet: "",
    },
    {
    name: "Spark_Unbound.Safe_Alloc",
    qualified_name: "Spark_Unbound.Safe_Alloc",
    signature: "spark_unbound.safe_alloc",
    enclosing: "spark_unbound",
    is_private: false,
    documentation: "- @summary\n- Generic package for safe heap allocation of type `T` whose size is known at compile time. \n-\n- @description\n- Generic package for safe heap allocation of type `T` whose size is known at compile time.\n- Type `T_Acc` is used to access the allocated instance of type `T`.",
    documentation_snippet: "",
    },
    {
    name: "Arrays",
    qualified_name: "Spark_Unbound.Safe_Alloc.Arrays",
    signature: "spark_unbound.safe_alloc.arrays",
    enclosing: "spark_unbound.safe_alloc",
    is_private: false,
    documentation: "- Tries to allocate an array of `Element_Type` with range from `First` to `Last` on the heap.\n- @param First Sets the lower bound for the allocated array.\n- @param Last Sets the upper bound for the allocated array.\n- @return `null` if `Storage_Error` was raised.\n\n@formal Element_Type\n@formal Index_Type\n@formal Array_Type\n@formal Array_Type_Acc",
    documentation_snippet: "",
    },
    {
    name: "Definite",
    qualified_name: "Spark_Unbound.Safe_Alloc.Definite",
    signature: "spark_unbound.safe_alloc.definite",
    enclosing: "spark_unbound.safe_alloc",
    is_private: false,
    documentation: "- Tries to allocate type `T` on the heap.\n- @return `null` if `Storage_Error` was raised.\n\n@formal T\n@formal T_Acc",
    documentation_snippet: "",
    },
]
}
---
