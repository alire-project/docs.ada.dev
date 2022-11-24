---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Output",
qualified_name: "GPR.Output",
signature: "gpr.output",
enclosing: "gpr",
is_private: false,
documentation: "This package contains low level output routines for writing error messages\nand informational output.",
documentation_snippet: "",
access_types:    [
       {
       name: "Output_Proc",
       qualified_name: "GPR.Output.Output_Proc",
       signature: "gpr.output.output_proc",
       enclosing: "",
       is_private: false,
       documentation: "This type is used for the Set_Special_Output procedure. If Output_Proc\nis called, then instead of lines being written to standard error or\nstandard output, a call is made to the given procedure for each line,\npassing the line with an end of line character (which is a single\nASCII.LF character, even in systems which normally use CR/LF or some\nother sequence for line end).\n\n@param S",
       documentation_snippet: "type Output_Proc is access procedure (S : String);",
       }   ,
   ]
,}
---
