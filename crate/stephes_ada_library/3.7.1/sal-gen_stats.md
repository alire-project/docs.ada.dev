---
crate: stephes_ada_library
layout: gnatdoc
gnatdoc: {
name: "SAL.Gen_Stats",
qualified_name: "SAL.Gen_Stats",
signature: "sal.gen_stats",
enclosing: "sal",
is_private: false,
documentation: "As a special exception under Section 7 of GPL version 3, you are granted\nadditional permissions described in the GCC Runtime Library Exception,\nversion 3.1, as published by the Free Software Foundation.\n\n@formal Real_Type",
documentation_snippet: "",
record_types:    [
       {
       name: "Display_Type",
       qualified_name: "SAL.Gen_Stats.Display_Type",
       signature: "sal.gen_stats.display_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Display_Type is record\n   Count              : Integer;\n   Mean               : Real_Type;\n   Standard_Deviation : Real_Type;\n   Min                : Real_Type;\n   Max                : Real_Type;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Stats_Type",
       qualified_name: "SAL.Gen_Stats.Stats_Type",
       signature: "sal.gen_stats.stats_type",
       enclosing: "",
       is_private: false,
       documentation: "tagged to allow \"object.method\" notation",
       documentation_snippet: "type Stats_Type is tagged private;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Stats",
       qualified_name: "SAL.Gen_Stats.Null_Stats",
       signature: "sal.gen_stats.null_stats",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Stats : constant Stats_Type;",
       }   ,
   ]
,}
---
