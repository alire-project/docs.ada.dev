---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Adalog.Debug",
qualified_name: "Langkit_Support.Adalog.Debug",
signature: "langkit_support.adalog.debug",
enclosing: "langkit_support.adalog",
is_private: false,
documentation: "This package Contains the debug configuration for Adalog. There are two\nmain ways of configuring the debug mode in Adalog:\n\n- The Debug_Enabled constant will determine at compile time whether\n  debugging is enabled or not. If it is False, no traces will be output,\n  and the Step mode won't be usable.\n- If you set the Debug_Enabled constant to True, you still need to activate\n  a debug mode at runtime via Set_Debug_State.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Debug_State_Type",
       qualified_name: "Langkit_Support.Adalog.Debug.Debug_State_Type",
       signature: "langkit_support.adalog.debug.debug_state_type",
       enclosing: "",
       is_private: false,
       documentation: "Set the debug state for Adalog:\n\n- If Trace, will trace the execution.\n- If Step, will trace and stop at every step of the solve so that you\n  can trace the solve operation step-by-step.\n- If Step_At_First_Unsat, will trace the execution, and set the mode to\n  Step as soon as *any* relation solving returns Unsatisfied.\n\nWARNING: Trace and step mode are not thread safe. It would not make any\nsense to try to use them with solving happening in several threads at\nthe same time.\n\n@enum None\n@enum Trace\n@enum Step\n@enum Step_At_First_Unsat",
       documentation_snippet: "type Debug_State_Type is (None, Trace, Step, Step_At_First_Unsat);",
       }   ,
   ]
,constants:    [
       {
       name: "Debug_Enabled",
       qualified_name: "Langkit_Support.Adalog.Debug.Debug_Enabled",
       signature: "langkit_support.adalog.debug.debug_enabled",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Debug_Enabled : constant Boolean := True;",
       }   ,
   ]
,}
---
