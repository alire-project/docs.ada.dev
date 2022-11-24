---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Graphs",
qualified_name: "SAL.Gen_Graphs",
signature: "sal.gen_graphs",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Edge_Data\n@formal Default_Edge_Data\n@formal Vertex_Index\n@formal Invalid_Vertex\n@formal Path_Index\n@formal Edge_Image",
documentation_snippet: "",
simple_types:    [
       {
       name: "Base_Edge_ID",
       qualified_name: "SAL.Gen_Graphs.Base_Edge_ID",
       signature: "sal.gen_graphs.base_edge_id",
       enclosing: "",
       is_private: false,
       documentation: "Edge ids are unique graph-wide, assigned by Add_Edge.",
       documentation_snippet: "type Base_Edge_ID is range 0 .. Integer'Last;",
       }   ,
   ]
,array_types:    [
       {
       name: "Path",
       qualified_name: "SAL.Gen_Graphs.Path",
       signature: "sal.gen_graphs.path",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Path is array (Positive range <>) of Path_Item;",
       }   ,
   ]
,record_types:    [
       {
       name: "Edge_Item",
       qualified_name: "SAL.Gen_Graphs.Edge_Item",
       signature: "sal.gen_graphs.edge_item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Edge_Item is record\n   ID   : Base_Edge_ID := Invalid_Edge_ID;\n   Data : Edge_Data    := Default_Edge_Data;\nend record;",
       }   ,
       {
       name: "Path_Item",
       qualified_name: "SAL.Gen_Graphs.Path_Item",
       signature: "sal.gen_graphs.path_item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Path_Item is record\n   Vertex : Vertex_Index'Base := Invalid_Vertex;\n   Edges  : Edge_Lists.List;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Graph",
       qualified_name: "SAL.Gen_Graphs.Graph",
       signature: "sal.gen_graphs.graph",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Graph is tagged private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Edge_ID",
       qualified_name: "SAL.Gen_Graphs.Edge_ID",
       signature: "sal.gen_graphs.edge_id",
       enclosing: "",
       is_private: false,
       documentation: "Edge ids are unique graph-wide, assigned by Add_Edge.",
       documentation_snippet: "subtype Edge_ID is Base_Edge_ID range 1 .. Base_Edge_ID'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Invalid_Edge_ID",
       qualified_name: "SAL.Gen_Graphs.Invalid_Edge_ID",
       signature: "sal.gen_graphs.invalid_edge_id",
       enclosing: "",
       is_private: false,
       documentation: "Edge ids are unique graph-wide, assigned by Add_Edge.",
       documentation_snippet: "Invalid_Edge_ID : constant Base_Edge_ID := 0;",
       }   ,
   ]
,variables:    [
       {
       name: "Trace",
       qualified_name: "SAL.Gen_Graphs.Trace",
       signature: "sal.gen_graphs.trace",
       enclosing: "",
       is_private: false,
       documentation: "Some bodies output debug info to Text_IO.Current_Output for\nnon-zero values of Trace.",
       documentation_snippet: "Trace : Integer := 0;",
       }   ,
   ]
,}
---
