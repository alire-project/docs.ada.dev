---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Actions",
qualified_name: "Rx.Actions",
signature: "rx.actions",
enclosing: "rx",
is_private: false,
documentation: "Procedures/Actions that do not require a type",
documentation_snippet: "",
interface_types:    [
       {
       name: "TFilter0",
       qualified_name: "Rx.Actions.TFilter0",
       signature: "rx.actions.tfilter0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TFilter0 is interface;",
       }   ,
       {
       name: "TProc0",
       qualified_name: "Rx.Actions.TProc0",
       signature: "rx.actions.tproc0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TProc0 is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "HTFilter0",
       qualified_name: "Rx.Actions.HTFilter0",
       signature: "rx.actions.htfilter0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type HTFilter0 is new Filter0_Holders.Definite with null record;",
       }   ,
       {
       name: "HTProc0",
       qualified_name: "Rx.Actions.HTProc0",
       signature: "rx.actions.htproc0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type HTProc0 is new Proc0_Holders.Definite with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Filter0",
       qualified_name: "Rx.Actions.Filter0",
       signature: "rx.actions.filter0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter0 is access function return Boolean;",
       }   ,
       {
       name: "Inspector",
       qualified_name: "Rx.Actions.Inspector",
       signature: "rx.actions.inspector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inspector is access\n  procedure (Event_Kind         : Rx_Event_Kinds;\n             Since_Previous     : Duration;\n             Since_Subscription : Duration);",
       }   ,
       {
       name: "Proc0",
       qualified_name: "Rx.Actions.Proc0",
       signature: "rx.actions.proc0",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proc0      is access procedure;",
       }   ,
       {
       name: "Proc_Error",
       qualified_name: "Rx.Actions.Proc_Error",
       signature: "rx.actions.proc_error",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Proc_Error is access procedure (E : Errors.Occurrence);",
       }   ,
   ]
,}
---
