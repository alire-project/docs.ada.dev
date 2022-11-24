---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Diagnostics.Output",
qualified_name: "Langkit_Support.Diagnostics.Output",
signature: "langkit_support.diagnostics.output",
enclosing: "langkit_support.diagnostics",
is_private: false,
documentation: "This package supports outputting\n:ada:ref:`Langkit_Support.Diagnostics.Diagnostic` for a source buffer, in a\npretty colorized format akin to GCC's verbose diagnostic format.\n\n.. note:: For the moment, this package has a few limitations, namely:\n\n    - Only source buffers with ``LF`` line endings are handled.\n\n    - Only error messages spanning one line are gracefully handled.\n      eventually we want to have something more powerful that has a syntax\n      for error spanning multiple lines.\n\n.. todo:\n\n    For the moment this is only used in the ``lkt_toolbox`` executable.\n    Eventually, this should be exposed to generated library users in some\n    fashion.",
documentation_snippet: "",
record_types:    [
       {
       name: "Diagnostic_Style",
       qualified_name: "Langkit_Support.Diagnostics.Output.Diagnostic_Style",
       signature: "langkit_support.diagnostics.output.diagnostic_style",
       enclosing: "",
       is_private: false,
       documentation: "Style for a diagnostic\n\n@field Label\n  Label for the diagnostic\n@field Color",
       documentation_snippet: "type Diagnostic_Style is record\n   Label : Unbounded_Text_Type;\n   Color : ANSI_Color;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Diagnostic_Style",
       qualified_name: "Langkit_Support.Diagnostics.Output.Default_Diagnostic_Style",
       signature: "langkit_support.diagnostics.output.default_diagnostic_style",
       enclosing: "",
       is_private: false,
       documentation: "Default style",
       documentation_snippet: "Default_Diagnostic_Style : constant Diagnostic_Style :=\n  (To_Unbounded_Text (\"error\"), Red);",
       }   ,
   ]
,}
---
