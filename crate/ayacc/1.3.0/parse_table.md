---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Parse_Table",
qualified_name: "Parse_Table",
signature: "parse_table",
enclosing: "",
is_private: false,
documentation: "This package build the shift reduce table and the goto table and\nwrites it to the shift_reduce_file, and goto_file. If the verbose option\nis set, the states generated and their coresponding actions are written\nto the verobose_file.\nThe parse table produced is an LALR(1) parse table.\nThe number of conflicts resulting from the grammar\ncan be determinied by calling the funciton REDUCE_REDUCE_CONFLICTS and\nSHIFT_REDUCE_CONFLICTS, after calling MAKE_PARSE_TABLE.",
documentation_snippet: "",
}
---
