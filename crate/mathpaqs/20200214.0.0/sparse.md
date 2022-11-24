---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Sparse",
qualified_name: "Sparse",
signature: "sparse",
enclosing: "",
is_private: false,
documentation: "----------------------------------------------------------------------------
documentation_snippet: "",
array_types:    [
       {
       name: "Index_array",
       qualified_name: "Sparse.Index_array",
       signature: "sparse.index_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Index_array is array(Index range <>) of Index;",
       }   ,
   ]
,record_types:    [
       {
       name: "CRS_matrix",
       qualified_name: "Sparse.CRS_matrix",
       signature: "sparse.crs_matrix",
       enclosing: "",
       is_private: false,
       documentation: "\n@field rows_max_p1\n@field nnz_max\n@field val\n@field col_ind\n@field row_ptr\n  p1 means +1 -> extra row ptr
       documentation_snippet: "type CRS_matrix( rows_max_p1, nnz_max: Index ) is record\n  val       : Vector(1..nnz_max);\n  col_ind   : Index_array(1..nnz_max);\n  row_ptr   : Index_array(1..rows_max_p1);\n  symmetric : Boolean;\n  rows      : Index:= rows_max_p1-1;\n  nnz       : Index:= nnz_max;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "p_CRS_matrix",
       qualified_name: "Sparse.p_CRS_matrix",
       signature: "sparse.p_crs_matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type p_CRS_matrix is access CRS_matrix;",
       }   ,
   ]
,}
---