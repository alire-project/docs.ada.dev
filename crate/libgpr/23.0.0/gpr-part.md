---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Part",
qualified_name: "GPR.Part",
signature: "gpr.part",
enclosing: "gpr",
is_private: false,
documentation: "Implements the parsing of project files into a tree",
documentation_snippet: "",
simple_types:    [
       {
       name: "Errout_Mode",
       qualified_name: "GPR.Part.Errout_Mode",
       signature: "gpr.part.errout_mode",
       enclosing: "",
       is_private: false,
       documentation: "Whether Parse should call Errout.Finalize (which prints the error\nmessages on stdout). When Never_Finalize is used, Errout is not reset\neither at the beginning of Parse.\n\n@enum Always_Finalize\n@enum Finalize_If_Error\n@enum Never_Finalize",
       documentation_snippet: "type Errout_Mode is\n  (Always_Finalize,\n   Finalize_If_Error,\n   Never_Finalize);",
       }   ,
   ]
,}
---
