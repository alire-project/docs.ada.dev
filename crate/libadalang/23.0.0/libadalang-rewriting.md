---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Rewriting",
qualified_name: "Libadalang.Rewriting",
signature: "libadalang.rewriting",
enclosing: "libadalang",
is_private: false,
documentation: "This package provides support for tree-based source code rewriting.\n\n.. ATTENTION:: This is an experimental feature, so even if it is exposed to\nallow experiments, it is totally unsupported and the API is very likely to\nchange in the future.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Node_Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.Node_Rewriting_Handle",
       signature: "libadalang.rewriting.node_rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "Handle for the process of rewriting an AST node. Such handles are owned\nby a Rewriting_Handle instance.",
       documentation_snippet: "type Node_Rewriting_Handle is private;",
       }   ,
       {
       name: "Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.Rewriting_Handle",
       signature: "libadalang.rewriting.rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "Handle for an analysis context rewriting session",
       documentation_snippet: "type Rewriting_Handle is private;",
       }   ,
       {
       name: "Unit_Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.Unit_Rewriting_Handle",
       signature: "libadalang.rewriting.unit_rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "Handle for the process of rewriting an analysis unit. Such handles are\nowned by a Rewriting_Handle instance.",
       documentation_snippet: "type Unit_Rewriting_Handle is private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Node_Rewriting_Handle_Array",
       qualified_name: "Libadalang.Rewriting.Node_Rewriting_Handle_Array",
       signature: "libadalang.rewriting.node_rewriting_handle_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Node_Rewriting_Handle_Array is\n   array (Positive range <>) of Node_Rewriting_Handle;",
       }   ,
       {
       name: "Unit_Rewriting_Handle_Array",
       qualified_name: "Libadalang.Rewriting.Unit_Rewriting_Handle_Array",
       signature: "libadalang.rewriting.unit_rewriting_handle_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Unit_Rewriting_Handle_Array is\n   array (Positive range <>) of Unit_Rewriting_Handle;",
       }   ,
   ]
,record_types:    [
       {
       name: "Apply_Result",
       qualified_name: "Libadalang.Rewriting.Apply_Result",
       signature: "libadalang.rewriting.apply_result",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Success\n@field Unit\n  Reference to the analysis unit that was being processed when\n  the error occurred.\n@field Diagnostics\n  Corresponding list of error messages",
       documentation_snippet: "type Apply_Result (Success : Boolean := True) is record\n   case Success is\n      when False =>\n         Unit : Analysis_Unit;\n         Diagnostics : Diagnostics_Vectors.Vector;\n      when True => null;\n   end case;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Node_Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.No_Node_Rewriting_Handle",
       signature: "libadalang.rewriting.no_node_rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Node_Rewriting_Handle : constant Node_Rewriting_Handle;",
       }   ,
       {
       name: "No_Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.No_Rewriting_Handle",
       signature: "libadalang.rewriting.no_rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Rewriting_Handle      : constant Rewriting_Handle;",
       }   ,
       {
       name: "No_Unit_Rewriting_Handle",
       qualified_name: "Libadalang.Rewriting.No_Unit_Rewriting_Handle",
       signature: "libadalang.rewriting.no_unit_rewriting_handle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Unit_Rewriting_Handle : constant Unit_Rewriting_Handle;",
       }   ,
   ]
,}
---
