---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Adalog",
qualified_name: "Langkit_Support.Adalog",
signature: "langkit_support.adalog",
enclosing: "langkit_support",
is_private: false,
documentation: "\nCopyright (C) 2014-2022, AdaCore\nSPDX-License-Identifier: Apache-2.0",
documentation_snippet: "",
simple_types:    [
       {
       name: "Solver_Kind",
       qualified_name: "Langkit_Support.Adalog.Solver_Kind",
       signature: "langkit_support.adalog.solver_kind",
       enclosing: "",
       is_private: false,
       documentation: "Different kind of solvers available in Adalog. ``None`` is for no\nsolver.\n\n@enum None\n@enum Symbolic\n@enum State_Machine",
       documentation_snippet: "type Solver_Kind is (None, Symbolic, State_Machine);",
       }   ,
   ]
,record_types:    [
       {
       name: "Solve_Options_Type",
       qualified_name: "Langkit_Support.Adalog.Solve_Options_Type",
       signature: "langkit_support.adalog.solve_options_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Solve_Options_Type is record\n   Cut_Dead_Branches : Boolean := True;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Valid_Solver_Kind",
       qualified_name: "Langkit_Support.Adalog.Valid_Solver_Kind",
       signature: "langkit_support.adalog.valid_solver_kind",
       enclosing: "",
       is_private: false,
       documentation: "Kind subtype for valid solver kinds",
       documentation_snippet: "subtype Valid_Solver_Kind is Solver_Kind range Symbolic .. State_Machine;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Timeout_Ticks_Number",
       qualified_name: "Langkit_Support.Adalog.Default_Timeout_Ticks_Number",
       signature: "langkit_support.adalog.default_timeout_ticks_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Timeout_Ticks_Number : constant := 50_000_000;",
       }   ,
   ]
,variables:    [
       {
       name: "Cst_Folding_Trace",
       qualified_name: "Langkit_Support.Adalog.Cst_Folding_Trace",
       signature: "langkit_support.adalog.cst_folding_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show the result of relation constant folding pass done during\nthe preparation stage in the symbolic solver.",
       documentation_snippet: "Cst_Folding_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.CONSTANT_FOLDING\",\n   Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Default_Options",
       qualified_name: "Langkit_Support.Adalog.Default_Options",
       signature: "langkit_support.adalog.default_options",
       enclosing: "",
       is_private: false,
       documentation: "Mutate this to affect the behavior of all calls to the solver which just\nuse the default options.",
       documentation_snippet: "Default_Options : Solve_Options_Type := (others => <>);",
       }   ,
       {
       name: "Sol_Trace",
       qualified_name: "Langkit_Support.Adalog.Sol_Trace",
       signature: "langkit_support.adalog.sol_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show:\n\n* the number of tried solutions;\n* valid solutions found.",
       documentation_snippet: "Sol_Trace  : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.SOLUTION\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Solv_Trace",
       qualified_name: "Langkit_Support.Adalog.Solv_Trace",
       signature: "langkit_support.adalog.solv_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show:\n\n* the progress of solving a sequence of atoms (both in the symbolic\n  solver's Try_Solution and in the dead branch cut optimization);\n* the progress of solving individual atoms.",
       documentation_snippet: "Solv_Trace  : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.SOLVE\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Solver_Trace",
       qualified_name: "Langkit_Support.Adalog.Solver_Trace",
       signature: "langkit_support.adalog.solver_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace whose only purpose is to show when we start solving an equation,\nand show when solving aborts because of an exception.",
       documentation_snippet: "Solver_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Stats_Trace",
       qualified_name: "Langkit_Support.Adalog.Stats_Trace",
       signature: "langkit_support.adalog.stats_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to output statistics about the equation to solve (number of atoms,\nof Any/All relations).",
       documentation_snippet: "Stats_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.STATS\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Timing_Trace",
       qualified_name: "Langkit_Support.Adalog.Timing_Trace",
       signature: "langkit_support.adalog.timing_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show the time taken by each equation resolution step",
       documentation_snippet: "Timing_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.TIMING\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Trav_Trace",
       qualified_name: "Langkit_Support.Adalog.Trav_Trace",
       signature: "langkit_support.adalog.trav_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show when starting the processing of a compound relation in the\nsymbolic solver.",
       documentation_snippet: "Trav_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.TRAVERSAL\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
       {
       name: "Verbose_Trace",
       qualified_name: "Langkit_Support.Adalog.Verbose_Trace",
       signature: "langkit_support.adalog.verbose_trace",
       enclosing: "",
       is_private: false,
       documentation: "Trace to show when:\n\n* a variable gets assigned a value;\n* a variable gets assigned an Id;\n* a variable gets (un)aliased.",
       documentation_snippet: "Verbose_Trace : GNATCOLL.Traces.Trace_Handle := GNATCOLL.Traces.Create\n  (\"LANGKIT.SOLVER.VERBOSE\", Default => GNATCOLL.Traces.From_Config);",
       }   ,
   ]
,}
---
