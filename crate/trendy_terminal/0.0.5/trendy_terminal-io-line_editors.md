---
crate: trendy_terminal
layout: gnatdoc
gnatdoc: {
name: "Trendy_Terminal.IO.Line_Editors",
qualified_name: "Trendy_Terminal.IO.Line_Editors",
signature: "trendy_terminal.io.line_editors",
enclosing: "trendy_terminal.io",
is_private: false,
documentation: "Updates a line to be a formatted line.",
documentation_snippet: "",
interface_types:    [
       {
       name: "Line_Editor",
       qualified_name: "Trendy_Terminal.IO.Line_Editors.Line_Editor",
       signature: "trendy_terminal.io.line_editors.line_editor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Line_Editor is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Stateless_Line_Editor",
       qualified_name: "Trendy_Terminal.IO.Line_Editors.Stateless_Line_Editor",
       signature: "trendy_terminal.io.line_editors.stateless_line_editor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stateless_Line_Editor is new Line_Editor with record\n    Format_Fn     : Format_Function;\n    Completion_Fn : Completion_Function;\n    Line_History  : Histories.History_Access;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Completion_Function",
       qualified_name: "Trendy_Terminal.IO.Line_Editors.Completion_Function",
       signature: "trendy_terminal.io.line_editors.completion_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Completion_Function is access function (L : Lines.Line)\n    return Lines.Line_Vectors.Vector;",
       }   ,
       {
       name: "Format_Function",
       qualified_name: "Trendy_Terminal.IO.Line_Editors.Format_Function",
       signature: "trendy_terminal.io.line_editors.format_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Format_Function is access function (L : Lines.Line) return Lines.Line;",
       }   ,
   ]
,}
---
