---
crate: spark_unbound
layout: gnatdoc
gnatdoc: {
name: "Spark_Unbound.Arrays",
qualified_name: "Spark_Unbound.Arrays",
signature: "spark_unbound.arrays",
enclosing: "spark_unbound",
is_private: false,
documentation: "needed to use `Self.Arr.all'Old` to prove some contracts\n\n@formal Element_Type\n@formal Index_Type\n  range must be smaller than Natural'Range_Length for overflow prevention (Some kind of compiler restriction would be nice)               \n@formal \"=\"\n  - Function used to compare elements inside `Unbound_Array`s.\n  - @param Left Element that is compared against `Right`.\n  - @param Right Element that is comparef against `Left`.\n  - @return `True` if `Left` and `Right` are equal.",
documentation_snippet: "",
array_types:    [
       {
       name: "Array_Type",
       qualified_name: "Spark_Unbound.Arrays.Array_Type",
       signature: "spark_unbound.arrays.array_type",
       enclosing: "",
       is_private: false,
       documentation: "- Note: Type should be treated as private.",
       documentation_snippet: "type Array_Type is array(Index_Type range <>) of Element_Type;",
       }   ,
   ]
,record_types:    [
       {
       name: "Unbound_Array",
       qualified_name: "Spark_Unbound.Arrays.Unbound_Array",
       signature: "spark_unbound.arrays.unbound_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unbound_Array is record\n   Last : Extended_Index := No_Index;\n   Arr : Array_Acc := null;\nend record\n  with Dynamic_Predicate => (if Arr = null then\n                               Last = No_Index\n                               else \n                                 (Arr.all'First = Index_Type'First \n                                  and then Arr.all'First <= Arr.all'Last\n                                  and then (if Arr.all'Length <= 0 then Last = No_Index else Last <= Arr.all'Last)));",
       }   ,
   ]
,access_types:    [
       {
       name: "Array_Acc",
       qualified_name: "Spark_Unbound.Arrays.Array_Acc",
       signature: "spark_unbound.arrays.array_acc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Array_Acc is access Array_Type;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Extended_Index",
       qualified_name: "Spark_Unbound.Arrays.Extended_Index",
       signature: "spark_unbound.arrays.extended_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Extended_Index is\n  Index_Type'Base range \n    Index_Type'First-1 .. Index_Type'Min (Index_Type'Base'Last - 1, Index_Type'Last) + 1;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Index",
       qualified_name: "Spark_Unbound.Arrays.No_Index",
       signature: "spark_unbound.arrays.no_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Index : constant Extended_Index := Extended_Index'First;",
       }   ,
   ]
,}
---
