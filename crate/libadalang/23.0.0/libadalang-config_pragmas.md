---
crate: libadalang
layout: gnatdoc
gnatdoc: {
name: "Libadalang.Config_Pragmas",
qualified_name: "Libadalang.Config_Pragmas",
signature: "libadalang.config_pragmas",
enclosing: "libadalang",
is_private: false,
documentation: "This package provides helpers to deal with GNAT's configurations pragmas\nfiles.",
documentation_snippet: "",
record_types:    [
       {
       name: "Config_Pragmas_Mapping",
       qualified_name: "Libadalang.Config_Pragmas.Config_Pragmas_Mapping",
       signature: "libadalang.config_pragmas.config_pragmas_mapping",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Local_Pragmas\n  Mappings that associate a local configuration pragmas file (element)\n  to each analysis unit (key) for which it applies.\n@field Global_Pragmas",
       documentation_snippet: "type Config_Pragmas_Mapping is record\n   Local_Pragmas : Unit_Maps.Map;\n   Global_Pragmas : Analysis_Unit;\nend record;",
       }   ,
   ]
,}
---
