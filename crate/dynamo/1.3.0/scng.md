---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Scng",
qualified_name: "Scng",
signature: "scng",
enclosing: "",
is_private: false,
documentation: "This package contains a generic lexical analyzer. This is used for scanning\nAda source files or text files with an Ada-like syntax, such as project\nfiles. It is instantiated in Scn and Prj.Err.\n\n@formal Post_Scan\n  Procedure called by Scan for the following tokens: Tok_Char_Literal,\n  Tok_Identifier, Tok_Real_Literal, Tok_Real_Literal, Tok_Integer_Literal,\n  Tok_String_Literal, Tok_Operator_Symbol, and Tok_Vertical_Bar. Used to\n  build Token_Node and also check for obsolescent features.\n@formal Error_Msg\n  Output a message at specified location\n@formal Error_Msg_S\n  Output a message at current scan pointer location\n@formal Error_Msg_SC\n  Output a message at the start of the current token\n@formal Error_Msg_SP\n  Output a message at the start of the previous token",
documentation_snippet: "",
}
---
