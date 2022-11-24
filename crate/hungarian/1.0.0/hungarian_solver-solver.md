---
crate: hungarian
layout: gnatdoc
gnatdoc: {
name: "Solver",
qualified_name: "Hungarian_Solver.Solver",
signature: "hungarian_solver.solver",
enclosing: "hungarian_solver",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Job_Sol_Index",
       qualified_name: "Hungarian_Solver.Solver.Job_Sol_Index",
       signature: "hungarian_solver.solver.job_sol_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Job_Sol_Index is new Natural       range 0 .. Jobs;",
       }   ,
       {
       name: "Size",
       qualified_name: "Hungarian_Solver.Solver.Size",
       signature: "hungarian_solver.solver.size",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Size is new Natural range 1 .. Natural'Max (Workers, Jobs);",
       }   ,
       {
       name: "Worker_Index",
       qualified_name: "Hungarian_Solver.Solver.Worker_Index",
       signature: "hungarian_solver.solver.worker_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Worker_Index is new Positive range 1 .. Workers;",
       }   ,
   ]
,array_types:    [
       {
       name: "Cost_Matrix",
       qualified_name: "Hungarian_Solver.Solver.Cost_Matrix",
       signature: "hungarian_solver.solver.cost_matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cost_Matrix is array (Worker_Index'Range,\n                           Job_Index'Range) of Costs;",
       }   ,
       {
       name: "Solution_Array",
       qualified_name: "Hungarian_Solver.Solver.Solution_Array",
       signature: "hungarian_solver.solver.solution_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Solution_Array is array (Worker_Index'Range) of Job_Sol_Index;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Problem",
       qualified_name: "Hungarian_Solver.Solver.Problem",
       signature: "hungarian_solver.solver.problem",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Problem is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Costs",
       qualified_name: "Hungarian_Solver.Solver.Costs",
       signature: "hungarian_solver.solver.costs",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Costs is Hungarian_Solver.Costs;",
       }   ,
       {
       name: "Job_Index",
       qualified_name: "Hungarian_Solver.Solver.Job_Index",
       signature: "hungarian_solver.solver.job_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype  Job_Index is     Job_Sol_Index range 1 .. Job_Sol_Index'Last;",
       }   ,
   ]
,}
---
