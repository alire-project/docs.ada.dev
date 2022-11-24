---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Output",
qualified_name: "Output",
signature: "output",
enclosing: "",
is_private: false,
documentation: "This package contains low level output routines used by the compiler for\nwriting error messages and informational output. It is also used by the\ndebug source file output routines (see Sprint.Print_Debug_Line).",
documentation_snippet: "",
simple_types:    [
       {
       name: "Saved_Output_Buffer",
       qualified_name: "Output.Saved_Output_Buffer",
       signature: "output.saved_output_buffer",
       enclosing: "",
       is_private: false,
       documentation: "Type used for Save/Restore_Buffer",
       documentation_snippet: "type Saved_Output_Buffer is private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Output_Proc",
       qualified_name: "Output.Output_Proc",
       signature: "output.output_proc",
       enclosing: "",
       is_private: false,
       documentation: "This type is used for the Set_Special_Output procedure. If Output_Proc\nis called, then instead of lines being written to standard error or\nstandard output, a call is made to the given procedure for each line,\npassing the line with an end of line character (which is a single\nASCII.LF character, even in systems which normally use CR/LF or some\nother sequence for line end).\n\n@param S",
       documentation_snippet: "type Output_Proc is access procedure (S : String);",
       }   ,
   ]
,constants:    [
       {
       name: "Buffer_Max",
       qualified_name: "Output.Buffer_Max",
       signature: "output.buffer_max",
       enclosing: "",
       is_private: false,
       documentation: "Maximal size of a buffered output line",
       documentation_snippet: "Buffer_Max : constant := Hostparm.Max_Line_Length;",
       }   ,
   ]
,}
---
