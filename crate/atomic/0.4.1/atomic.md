---
crate: atomic
layout: gnatdoc
gnatdoc: {
name: "Atomic",
qualified_name: "Atomic",
signature: "atomic",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Flag",
       qualified_name: "Atomic.Flag",
       signature: "atomic.flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Flag is limited private;",
       }   ,
       {
       name: "Mem_Order",
       qualified_name: "Atomic.Mem_Order",
       signature: "atomic.mem_order",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Relaxed\n  Implies no inter-thread ordering constraints\n@enum Consume\n  This is currently implemented using the stronger __ATOMIC_ACQUIRE\n  memory order because of a deficiency in C++11's semantics for\n  memory_order_consume.\n@enum Acquire\n  Creates an inter-thread happens-before constraint from the release\n  (or stronger) semantic store to this acquire load. Can prevent\n  hoisting of code to before the operation.\n@enum Release\n  Creates an inter-thread happens-before constraint to acquire (or\n  stronger) semantic loads that read from this release store. Can\n  prevent sinking of code to after the operation.\n@enum Acq_Rel\n  Combines the effects of both Acquire and Release\n@enum Seq_Cst\n  Enforces total ordering with all other Seq_Cst operations",
       documentation_snippet: "type Mem_Order is\n  (Relaxed,\n   Consume,\n   Acquire,\n   Release,\n   Acq_Rel,\n   Seq_Cst);",
       }   ,
   ]
,}
---
