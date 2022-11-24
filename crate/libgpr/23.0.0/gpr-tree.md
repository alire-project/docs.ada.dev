---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Tree",
qualified_name: "GPR.Tree",
signature: "gpr.tree",
enclosing: "gpr",
is_private: false,
documentation: "This package defines the structure of the Project File tree",
documentation_snippet: "",
simple_types:    [
       {
       name: "Comment_Location",
       qualified_name: "GPR.Tree.Comment_Location",
       signature: "gpr.tree.comment_location",
       enclosing: "",
       is_private: false,
       documentation: "Used in call to Add_Comments below\n\n@enum Before\n@enum After\n@enum Before_End\n@enum After_End\n@enum End_Of_Line",
       documentation_snippet: "type Comment_Location is\n  (Before, After, Before_End, After_End, End_Of_Line);",
       }   ,
       {
       name: "Comment_State",
       qualified_name: "GPR.Tree.Comment_State",
       signature: "gpr.tree.comment_state",
       enclosing: "",
       is_private: false,
       documentation: "A type to store the values of several global variables related to\ncomments.",
       documentation_snippet: "type Comment_State is private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Comment_Data",
       qualified_name: "GPR.Tree.Comment_Data",
       signature: "gpr.tree.comment_data",
       enclosing: "",
       is_private: false,
       documentation: "Component type for Comments Table below\n\n@field Value\n@field Follows_Empty_Line\n@field Is_Followed_By_Empty_Line",
       documentation_snippet: "type Comment_Data is record\n   Value                     : Name_Id := No_Name;\n   Follows_Empty_Line        : Boolean := False;\n   Is_Followed_By_Empty_Line : Boolean := False;\nend record;",
       }   ,
       {
       name: "Environment",
       qualified_name: "GPR.Tree.Environment",
       signature: "gpr.tree.environment",
       enclosing: "",
       is_private: false,
       documentation: "\n@field External\n  External references are stored in this hash table (and manipulated\n  through subprograms in prj-ext.ads). External references are\n  project-tree specific so that one can load the same tree twice but\n  have two views of it, for instance.\n@field Project_Path\n  The project path is tree specific, since we might want to load\n  simultaneously multiple projects, each with its own search path, in\n  particular when using different compilers with different default\n  search directories.\n@field Flags",
       documentation_snippet: "type Environment is record\n   External : GPR.Ext.External_References;\n   Project_Path : aliased GPR.Env.Project_Search_Path;\n   Flags : Processing_Flags;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Project_Node_Tree_Ref",
       qualified_name: "GPR.Tree.Project_Node_Tree_Ref",
       signature: "gpr.tree.project_node_tree_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Project_Node_Tree_Ref is GPR.Project_Node_Tree_Ref;",
       }   ,
   ]
,}
---
