---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Graph.Cubic_curves",
qualified_name: "Graph.Cubic_curves",
signature: "graph.cubic_curves",
enclosing: "graph",
is_private: false,
documentation: "* Coordinates of cubic curves in math plane",
documentation_snippet: "",
record_types:    [
       {
       name: "Cubic_curve_type",
       qualified_name: "Graph.Cubic_curves.Cubic_curve_type",
       signature: "graph.cubic_curves.cubic_curve_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@field n_seg\n@field end_pt\n  end points\n@field c1\n  control points, can be the same\n@field c2\n  control points, can be the same",
       documentation_snippet: "type Cubic_curve_type(n_seg: positive) is record\n  end_pt: math_polygon_type(0..n_seg);\n  c1,c2:  math_polygon_type(1..n_seg);\nend record;",
       }   ,
   ]
,}
---
