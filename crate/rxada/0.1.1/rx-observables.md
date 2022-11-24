---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Observables",
qualified_name: "Rx.Observables",
signature: "rx.observables",
enclosing: "rx",
is_private: false,
documentation: "",
documentation_snippet: "",
packages:    [
       {
       name: "Linkers",
       qualified_name: "Rx.Observables.Linkers",
       signature: "rx.observables.linkers",
       enclosing: "rx.observables",
       is_private: false,
       documentation: "This package can be used instead of using the Rx.Observables one to make the \"&\" visible",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Policies",
       qualified_name: "Rx.Observables.Policies",
       signature: "rx.observables.policies",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Policies is (Keep_First, Keep_Last);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Definite_Observable",
       qualified_name: "Rx.Observables.Definite_Observable",
       signature: "rx.observables.definite_observable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Definite_Observable is Typed.Definite_Observables.Observable;",
       }   ,
       {
       name: "From_List_Transformer",
       qualified_name: "Rx.Observables.From_List_Transformer",
       signature: "rx.observables.from_list_transformer",
       enclosing: "",
       is_private: false,
       documentation: "subtype Obs_Transformer        is Obs_Transformers.Operator'Class;",
       documentation_snippet: "subtype From_List_Transformer  is From_List_Transformers.Operator'Class;",
       }   ,
       {
       name: "Into_List_Transformer",
       qualified_name: "Rx.Observables.Into_List_Transformer",
       signature: "rx.observables.into_list_transformer",
       enclosing: "",
       is_private: false,
       documentation: "subtype Obs_Transformer        is Obs_Transformers.Operator'Class;",
       documentation_snippet: "subtype Into_List_Transformer  is Into_List_Transformers.Operator'Class;",
       }   ,
       {
       name: "List_Preserver",
       qualified_name: "Rx.Observables.List_Preserver",
       signature: "rx.observables.list_preserver",
       enclosing: "",
       is_private: false,
       documentation: "subtype Obs_Transformer        is Obs_Transformers.Operator'Class;",
       documentation_snippet: "subtype List_Preserver         is List_Preservers.Operator'Class;",
       }   ,
       {
       name: "Observable",
       qualified_name: "Rx.Observables.Observable",
       signature: "rx.observables.observable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Observable  is Typed.Contracts.Observable'Class;",
       }   ,
       {
       name: "Observer",
       qualified_name: "Rx.Observables.Observer",
       signature: "rx.observables.observer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Observer    is Typed.Contracts.Observer'Class;",
       }   ,
       {
       name: "Operator",
       qualified_name: "Rx.Observables.Operator",
       signature: "rx.observables.operator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Operator  is Operate.Operator'Class;",
       }   ,
       {
       name: "Sink",
       qualified_name: "Rx.Observables.Sink",
       signature: "rx.observables.sink",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Sink        is Typed.Contracts.Sink'Class;",
       }   ,
       {
       name: "T",
       qualified_name: "Rx.Observables.T",
       signature: "rx.observables.t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype T           is Typed.Type_Traits.T;",
       }   ,
       {
       name: "T_List",
       qualified_name: "Rx.Observables.T_List",
       signature: "rx.observables.t_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype T_List                 is Collections.List;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Not_Same",
       qualified_name: "Rx.Observables.Default_Not_Same",
       signature: "rx.observables.default_not_same",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Not_Same : constant Typed.Actions.Comparator;",
       }   ,
   ]
,}
---
