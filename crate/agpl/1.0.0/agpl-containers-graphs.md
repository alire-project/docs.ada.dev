---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Containers.Graphs",
qualified_name: "Agpl.Containers.Graphs",
signature: "agpl.containers.graphs",
enclosing: "agpl.containers",
is_private: false,
documentation: "\n@formal Vertex_Type\n@formal No_Vertex\n@formal Edge_Type\n@formal No_Edge\n  Used to signal infinite length or missing\n@formal \"<\"\n@formal Image\n@formal \"<\"\n@formal Image\n  Weight or something, must be true for all E < No_Edge",
documentation_snippet: "",
record_types:    [
       {
       name: "Edge_Cursor",
       qualified_name: "Agpl.Containers.Graphs.Edge_Cursor",
       signature: "agpl.containers.graphs.edge_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Edge_Cursor is abstract tagged null record;",
       }   ,
       {
       name: "Vertex_Cursor",
       qualified_name: "Agpl.Containers.Graphs.Vertex_Cursor",
       signature: "agpl.containers.graphs.vertex_cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertex_Cursor is abstract tagged null record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Edge_Handle",
       qualified_name: "Agpl.Containers.Graphs.Edge_Handle",
       signature: "agpl.containers.graphs.edge_handle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Edge_Handle is new Edge_Handles.Object with null record;",
       }   ,
       {
       name: "Edge_Vector",
       qualified_name: "Agpl.Containers.Graphs.Edge_Vector",
       signature: "agpl.containers.graphs.edge_vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Edge_Vector is new Edge_Vectors.Vector with null record;",
       }   ,
       {
       name: "Graph",
       qualified_name: "Agpl.Containers.Graphs.Graph",
       signature: "agpl.containers.graphs.graph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Graph is abstract tagged private;",
       }   ,
       {
       name: "Vertex_Set",
       qualified_name: "Agpl.Containers.Graphs.Vertex_Set",
       signature: "agpl.containers.graphs.vertex_set",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertex_Set is new Vertex_Sets.Set with null record;",
       }   ,
   ]
,}
---
