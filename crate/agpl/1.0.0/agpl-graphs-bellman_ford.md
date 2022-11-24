---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Graphs.Bellman_Ford",
qualified_name: "Agpl.Graphs.Bellman_Ford",
signature: "agpl.graphs.bellman_ford",
enclosing: "agpl.graphs",
is_private: false,
documentation: "C code taken from en.wikipedia.com\n\n@formal Vertex_Data",
documentation_snippet: "",
simple_types:    [
       {
       name: "Vertex_Index",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Vertex_Index",
       signature: "agpl.graphs.bellman_ford.vertex_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertex_Index is new Positive;",
       }   ,
   ]
,array_types:    [
       {
       name: "Cost_Array",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Cost_Array",
       signature: "agpl.graphs.bellman_ford.cost_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cost_Array  is array  (Vertex_Index range <>) of Integer;",
       }   ,
       {
       name: "Edge_Array",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Edge_Array",
       signature: "agpl.graphs.bellman_ford.edge_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Edge_Array  is array  (Positive range <>) of Edge;",
       }   ,
   ]
,record_types:    [
       {
       name: "Edge",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Edge",
       signature: "agpl.graphs.bellman_ford.edge",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Source\n@field Dest\n@field Weight\n  Can be negative",
       documentation_snippet: "type Edge is record\n   Source,\n   Dest   : Vertex_Index;\n   Weight : Integer;\nend record;",
       }   ,
       {
       name: "Vertex",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Vertex",
       signature: "agpl.graphs.bellman_ford.vertex",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vertex is record\n   Index : Vertex_Index;\n   Data  : Vertex_Data;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Graph",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Graph",
       signature: "agpl.graphs.bellman_ford.graph",
       enclosing: "",
       is_private: false,
       documentation: "Graphs must be continuous: that is, vertices must be consecutively named.",
       documentation_snippet: "type Graph is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Cost_Matrix",
       qualified_name: "Agpl.Graphs.Bellman_Ford.Cost_Matrix",
       signature: "agpl.graphs.bellman_ford.cost_matrix",
       enclosing: "",
       is_private: false,
       documentation: "where the integer is the cost of going from Row to Col vertex,\nas given by the integer weights of the edges",
       documentation_snippet: "subtype Cost_Matrix is Cost_Matrices.Matrix;",
       }   ,
   ]
,}
---
