---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Proc",
qualified_name: "GPR.Proc",
signature: "gpr.proc",
enclosing: "gpr",
is_private: false,
documentation: "This package is used to convert a project file tree (see prj-tree.ads) to\nproject file data structures (see prj.ads), taking into account the\nenvironment (external references).",
documentation_snippet: "",
access_types:    [
       {
       name: "Tree_Loaded_Callback",
       qualified_name: "GPR.Proc.Tree_Loaded_Callback",
       signature: "gpr.proc.tree_loaded_callback",
       enclosing: "",
       is_private: false,
       documentation: "Callback used after the phase 1 of the processing of each aggregated\nproject to get access to project trees of aggregated projects.\n\n@param Node_Tree\n@param Tree\n@param Project_Node\n@param Project",
       documentation_snippet: "type Tree_Loaded_Callback is access procedure\n  (Node_Tree    : Project_Node_Tree_Ref;\n   Tree         : Project_Tree_Ref;\n   Project_Node : Project_Node_Id;\n   Project      : Project_Id);",
       }   ,
   ]
,}
---
