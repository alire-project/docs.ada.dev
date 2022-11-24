---
crate: spark_unbound
layout: gnatdoc
gnatdoc: {
name: "Spark_Unbound.Safe_Alloc",
qualified_name: "Spark_Unbound.Safe_Alloc",
signature: "spark_unbound.safe_alloc",
enclosing: "spark_unbound",
is_private: false,
documentation: "- @summary\n- Generic package for safe heap allocation of type `T` whose size is known at compile time. \n-\n- @description\n- Generic package for safe heap allocation of type `T` whose size is known at compile time.\n- Type `T_Acc` is used to access the allocated instance of type `T`.",
documentation_snippet: "",
packages:    [
       {
       name: "Arrays",
       qualified_name: "Spark_Unbound.Safe_Alloc.Arrays",
       signature: "spark_unbound.safe_alloc.arrays",
       enclosing: "spark_unbound.safe_alloc",
       is_private: false,
       documentation: "- Tries to allocate an array of `Element_Type` with range from `First` to `Last` on the heap.\n- @param First Sets the lower bound for the allocated array.\n- @param Last Sets the upper bound for the allocated array.\n- @return `null` if `Storage_Error` was raised.\n\n@formal Element_Type\n@formal Index_Type\n@formal Array_Type\n@formal Array_Type_Acc",
       documentation_snippet: "",
       }   ,
       {
       name: "Definite",
       qualified_name: "Spark_Unbound.Safe_Alloc.Definite",
       signature: "spark_unbound.safe_alloc.definite",
       enclosing: "spark_unbound.safe_alloc",
       is_private: false,
       documentation: "- Tries to allocate type `T` on the heap.\n- @return `null` if `Storage_Error` was raised.\n\n@formal T\n@formal T_Acc",
       documentation_snippet: "",
       }   ,
   ]
,}
---
