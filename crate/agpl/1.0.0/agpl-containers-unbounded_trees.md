---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Unbounded_Trees",
qualified_name: "Agpl.Containers.Unbounded_Trees",
signature: "agpl.containers.unbounded_trees",
enclosing: "agpl.containers",
is_private: false,
documentation: "\n@formal Node_Data\n@formal Child_Index\n@formal \"<\"\n  Must be non-modular; it is internally used for sets of children",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Cursor",
       qualified_name: "Agpl.Containers.Unbounded_Trees.Cursor",
       signature: "agpl.containers.unbounded_trees.cursor",
       enclosing: "",
       is_private: false,
       documentation: "Used to navigate a tree. Basically a pointer to node.",
       documentation_snippet: "type Cursor is tagged private;",
       }   ,
       {
       name: "Tree",
       qualified_name: "Agpl.Containers.Unbounded_Trees.Tree",
       signature: "agpl.containers.unbounded_trees.tree",
       enclosing: "",
       is_private: false,
       documentation: "Because I haven't had the time to implement copying, but can be done",
       documentation_snippet: "type Tree is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Log_Section",
       qualified_name: "Agpl.Containers.Unbounded_Trees.Log_Section",
       signature: "agpl.containers.unbounded_trees.log_section",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Log_Section : constant String := \"agpl.containers.unbounded_trees\";",
       }   ,
   ]
,}
---
