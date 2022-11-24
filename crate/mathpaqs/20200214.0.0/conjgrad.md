---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "ConjGrad",
qualified_name: "ConjGrad",
signature: "conjgrad",
enclosing: "",
is_private: false,
documentation: "Kind of preconditioner for iterative methods\n\n@formal Real\n@formal Index\n@formal Vector\n@formal Any_matrix\n  NB: 2 syntaxes for instanciating that as unconstrained type :\n  [Ada 95+] type Any_matrix (<>) is private;\n  [Ada 83]  type Any_matrix is private;\n@formal Get\n@formal Rows\n@formal Defined_symmetric\n  ---------------------\n   Vector operations --\n  ---------------------\n@formal Copy\n@formal \"*\"\n@formal Add_scaled\n@formal Scale\n  ----------------------------------\n    Matrix-vector multiplication  --\n  ----------------------------------\n@formal Mult",
documentation_snippet: "",
simple_types:    [
       {
       name: "t_precond",
       qualified_name: "ConjGrad.t_precond",
       signature: "conjgrad.t_precond",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type t_precond is ( none, diag, tridiag );",
       }   ,
   ]
,variables:    [
       {
       name: "iteration_at_failure",
       qualified_name: "ConjGrad.iteration_at_failure",
       signature: "conjgrad.iteration_at_failure",
       enclosing: "",
       is_private: false,
       documentation: "Information on iteration at last failure",
       documentation_snippet: "iteration_at_failure: Index;",
       }   ,
   ]
,}
---
