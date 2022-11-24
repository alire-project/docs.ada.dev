---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Ragged",
qualified_name: "Ragged",
signature: "ragged",
enclosing: "",
is_private: false,
documentation: "Cell and index should be private but for efficency and for subtle \nproblems that arise when type item is implemeted as a limited private \nin an external package, cell and index are kept visible.\n\n@formal Row_Index\n@formal Col_Index\n@formal Item\n@formal Null_Value",
documentation_snippet: "",
simple_types:    [
       {
       name: "Hidden_Type",
       qualified_name: "Ragged.Hidden_Type",
       signature: "ragged.hidden_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Hidden_Type is limited private;",
       }   ,
   ]
,record_types:    [
       {
       name: "Cell",
       qualified_name: "Ragged.Cell",
       signature: "ragged.cell",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cell is   \n    record \n        Value  : Item; \n        Hidden : Hidden_Type; \n    end record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Index",
       qualified_name: "Ragged.Index",
       signature: "ragged.index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Index       is access Cell;",
       }   ,
   ]
,}
---
