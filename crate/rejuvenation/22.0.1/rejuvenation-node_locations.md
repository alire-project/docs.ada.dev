---
crate: rejuvenation
layout: gnatdoc
gnatdoc: {
name: "Rejuvenation.Node_Locations",
qualified_name: "Rejuvenation.Node_Locations",
signature: "rejuvenation.node_locations",
enclosing: "rejuvenation",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Node_Location",
       qualified_name: "Rejuvenation.Node_Locations.Node_Location",
       signature: "rejuvenation.node_locations.node_location",
       enclosing: "",
       is_private: false,
       documentation: "Between two adjacent nodes in the AST, trivia\n(i.e. white space and comment) can occur.\nThis raises the question: Where does a Node start / end?\nNo_Trivia           : Trivia before / after the node is\n                      not considered part of that node\nTrivia_On_Same_Line : Trivia before / after the node\n                      on the same line is considered part\n                      of that node\nAll_Trivia          : Trivia before / after the node is\n                      considered part of that node\n\n@enum No_Trivia\n@enum Trivia_On_Same_Line\n@enum All_Trivia",
       documentation_snippet: "type Node_Location is (No_Trivia, Trivia_On_Same_Line, All_Trivia);",
       }   ,
   ]
,}
---
