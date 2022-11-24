---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Root.Operators",
qualified_name: "Iterators.Root.Operators",
signature: "iterators.root.operators",
enclosing: "iterators.root",
is_private: false,
documentation: "This public instance is a necessary evil to re-expose type-changing\noperators here:",
documentation_snippet: "",
packages:    [
       {
       name: "Linking",
       qualified_name: "Iterators.Root.Operators.Linking",
       signature: "iterators.root.operators.linking",
       enclosing: "iterators.root.operators",
       is_private: false,
       documentation: "Expose here the linking operators for Operators and Reducers. This is\nan \"use\"-intended package.",
       documentation_snippet: "",
       }   ,
   ]
,simple_types:    [
       {
       name: "Counter",
       qualified_name: "Iterators.Root.Operators.Counter",
       signature: "iterators.root.operators.counter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Counter (<>) is private;",
       }   ,
       {
       name: "Reducer",
       qualified_name: "Iterators.Root.Operators.Reducer",
       signature: "iterators.root.operators.reducer",
       enclosing: "",
       is_private: false,
       documentation: "Generic reduction, from a starting value and applying Reduce_Fn to each\nincoming element.",
       documentation_snippet: "type Reducer (<>) is private;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Chain",
       qualified_name: "Iterators.Root.Operators.Chain",
       signature: "iterators.root.operators.chain",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Chain is new Operators.Chain with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Const_Apply",
       qualified_name: "Iterators.Root.Operators.Const_Apply",
       signature: "iterators.root.operators.const_apply",
       enclosing: "",
       is_private: false,
       documentation: "These named access types allow having two For_Each with the same name.\nOtherwise, the \"in out\" is not enough to avoid the name clash.\n\n@param Element",
       documentation_snippet: "type Const_Apply is access procedure (Element : Any_Element);",
       }   ,
       {
       name: "Reduce_Fn_Access",
       qualified_name: "Iterators.Root.Operators.Reduce_Fn_Access",
       signature: "iterators.root.operators.reduce_fn_access",
       enclosing: "",
       is_private: false,
       documentation: "Generic reduction, from a starting value and applying Reduce_Fn to each\nincoming element.\n\n@param L\n@param R\n\n@return",
       documentation_snippet: "type Reduce_Fn_Access is\n  access function (L, R : Any_Element) return Any_Element;",
       }   ,
       {
       name: "Var_Apply",
       qualified_name: "Iterators.Root.Operators.Var_Apply",
       signature: "iterators.root.operators.var_apply",
       enclosing: "",
       is_private: false,
       documentation: "These named access types allow having two For_Each with the same name.\nOtherwise, the \"in out\" is not enough to avoid the name clash.\n\n@param Element",
       documentation_snippet: "type Var_Apply   is access procedure (Element : in out Any_Element);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Iterator",
       qualified_name: "Iterators.Root.Operators.Iterator",
       signature: "iterators.root.operators.iterator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Iterator is Root.Iterator;",
       }   ,
       {
       name: "Operator",
       qualified_name: "Iterators.Root.Operators.Operator",
       signature: "iterators.root.operators.operator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Operator is Operators.Operator;",
       }   ,
   ]
,}
---
