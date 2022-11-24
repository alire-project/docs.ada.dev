---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Optimization.Annealing.Solver",
qualified_name: "Agpl.Optimization.Annealing.Solver",
signature: "agpl.optimization.annealing.solver",
enclosing: "agpl.optimization.annealing",
is_private: false,
documentation: "pragma Elaborate_Body;\n\n@formal Solution\n  An opaque type containing a solution.\n@formal Evaluate\n  Says how good is a solution.\n@formal Mutate\n  Mutates a solution.\n@formal Normalize\n  Say the probability of keeping a new solution, given the change in\n  costs and current temperature.\n  Will be compared against U[0..1]\n@formal Last_Mutation\n  Informative, to know mutations working well\n  Just returns a description of what was done.\n  Should be unique for the mutation class, since it is used to\n  aggregate stats.\n@formal Undo\n  Must undo the last mutation. Only one level of undo is required.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Optimization.Annealing.Solver.Object",
       signature: "agpl.optimization.annealing.solver.object",
       enclosing: "",
       is_private: false,
       documentation: "The object used to perform the annealing",
       documentation_snippet: "type Object is tagged limited private;",
       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Optimization.Annealing.Solver.Log_Section",
       signature: "agpl.optimization.annealing.solver.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.optimization.annealing.solver\";",
       }   ,
   ]
,}
---
