---
crate: libgpr
layout: gnatdoc
gnatdoc: {
name: "GPR.Compilation.Sync",
qualified_name: "GPR.Compilation.Sync",
signature: "gpr.compilation.sync",
enclosing: "gpr.compilation",
is_private: false,
documentation: "Synchronize data to/from the slave. The usage is:\n\n  On one side:\n     1. call Send_Files for every slave to be synchronized\n     2. call Wait to wait for the synchronization to be terminated\n\n  On the other side:\n     1. call Receive_Files",
documentation_snippet: "",
simple_types:    [
       {
       name: "Direction",
       qualified_name: "GPR.Compilation.Sync.Direction",
       signature: "gpr.compilation.sync.direction",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Direction is (To_Slave, To_Master);",
       }   ,
   ]
,}
---
