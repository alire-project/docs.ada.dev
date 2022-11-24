---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Optimization.Annealing.Solution",
qualified_name: "Agpl.Optimization.Annealing.Solution",
signature: "agpl.optimization.annealing.solution",
enclosing: "agpl.optimization.annealing",
is_private: false,
documentation: "Helper base class that has support for varied probability mutations\nExtend it with missing bits",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Optimization.Annealing.Solution.Object",
       signature: "agpl.optimization.annealing.solution.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is abstract tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Mutation_Doer",
       qualified_name: "Agpl.Optimization.Annealing.Solution.Mutation_Doer",
       signature: "agpl.optimization.annealing.solution.mutation_doer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mutation_Doer   is access procedure (This : in out Object'Class);",
       }   ,
       {
       name: "Mutation_Undoer",
       qualified_name: "Agpl.Optimization.Annealing.Solution.Mutation_Undoer",
       signature: "agpl.optimization.annealing.solution.mutation_undoer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Mutation_Undoer is access procedure (This : in out Object'Class);",
       }   ,
   ]
,}
---
