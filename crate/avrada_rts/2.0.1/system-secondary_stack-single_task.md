---
crate: avrada_rts
layout: gnatdoc
gnatdoc: {
name: "System.Secondary_Stack.Single_Task",
qualified_name: "System.Secondary_Stack.Single_Task",
signature: "system.secondary_stack.single_task",
enclosing: "system.secondary_stack",
is_private: false,
documentation: "This package provides a simple, default implementation of a function that\nreturns a pointer to a secondary stack for use in single-threaded\napplications. It is not suitable for multi-threaded applications.\n\nThe function defined in this package is used when the following two\nconditions are met:\n  1) No user-defined implementation has been provided. That is, the\n     symbol __gnat_get_sec_stack is not exported by the user's code.\n  2) No tasking is used. When tasking is used, __gnat_get_secondary_stack\n     is resolved by libgnarl.a (that contains a thread-safe implementation\n     of the secondary stack), so that the single-threaded version is not\n     included in the final executable.",
documentation_snippet: "",
}
---
