---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Styleg",
qualified_name: "Styleg",
signature: "styleg",
enclosing: "",
is_private: false,
documentation: "This generic package collects the routines used for style checking, as\nactivated by the relevant command line option. These are gathered in\na separate package so that they can more easily be customized. Calls\nto these subprograms are only made if Opt.Style_Check is set True.\nStyleg does not depends on the GNAT tree (Atree, Sinfo, ...).\n\n@formal Error_Msg\n  Output a message at specified location\n@formal Error_Msg_S\n  Output a message at current scan pointer location\n@formal Error_Msg_SC\n  Output a message at the start of the current token\n@formal Error_Msg_SP\n  Output a message at the start of the previous token",
documentation_snippet: "",
}
---
