---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "ConjGrad",
qualified_name: "ConjGrad",
signature: "conjgrad",
enclosing: "",
is_private: false,
documentation: "Kind of preconditioner for iterative methods
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
       documentation: "Information on iteration at last failure
       documentation_snippet: "iteration_at_failure: Index;",
       }   ,
   ]
,}
---