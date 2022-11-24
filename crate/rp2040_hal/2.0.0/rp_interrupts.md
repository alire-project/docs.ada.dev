---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP_Interrupts",
qualified_name: "RP_Interrupts",
signature: "rp_interrupts",
enclosing: "",
is_private: false,
documentation: "This is a minimal version of the System.BB.Interrupts interface\navailable in Ravenscar. Close enough that these packages can be used\ninterchangably for the purposes of the RP drivers.",
documentation_snippet: "",
access_types:    [
       {
       name: "Interrupt_Handler",
       qualified_name: "RP_Interrupts.Interrupt_Handler",
       signature: "rp_interrupts.interrupt_handler",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Interrupt_Handler     is access procedure;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Interrupt_ID",
       qualified_name: "RP_Interrupts.Interrupt_ID",
       signature: "rp_interrupts.interrupt_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Interrupt_ID       is Cortex_M.NVIC.Interrupt_ID;",
       }   ,
       {
       name: "Interrupt_Priority",
       qualified_name: "RP_Interrupts.Interrupt_Priority",
       signature: "rp_interrupts.interrupt_priority",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Interrupt_Priority is System.Interrupt_Priority;",
       }   ,
   ]
,}
---
