---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Actions.Transform",
qualified_name: "Rx.Actions.Transform",
signature: "rx.actions.transform",
enclosing: "rx.actions",
is_private: false,
documentation: "Plain type transforming functions",
documentation_snippet: "",
interface_types:    [
       {
       name: "TInflater1",
       qualified_name: "Rx.Actions.Transform.TInflater1",
       signature: "rx.actions.transform.tinflater1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TInflater1 is interface;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "HInflater1",
       qualified_name: "Rx.Actions.Transform.HInflater1",
       signature: "rx.actions.transform.hinflater1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type HInflater1 is new TInflater1_Holders.Definite with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Func1",
       qualified_name: "Rx.Actions.Transform.Func1",
       signature: "rx.actions.transform.func1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Func1 is access function (V : From.T) return Into.T;",
       }   ,
       {
       name: "Func2",
       qualified_name: "Rx.Actions.Transform.Func2",
       signature: "rx.actions.transform.func2",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Func2 is access function (F : From.T;\n                               I : Into.T) return Into.T;",
       }   ,
       {
       name: "Inflater1",
       qualified_name: "Rx.Actions.Transform.Inflater1",
       signature: "rx.actions.transform.inflater1",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inflater1 is access function (V : From.T) return Into.Observable'Class;",
       }   ,
   ]
,}
---
