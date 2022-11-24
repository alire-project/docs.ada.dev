---
crate: iterators
layout: gnatdoc
gnatdoc: {
name: "Iterators.Meta",
qualified_name: "Iterators.Meta",
signature: "iterators.meta",
enclosing: "iterators",
is_private: false,
documentation: "Iterators of iterators. Created by a few specific operators like Buffer,\nWindow...",
documentation_snippet: "",
packages:    [
       {
       name: "Linking",
       qualified_name: "Iterators.Meta.Linking",
       signature: "iterators.meta.linking",
       enclosing: "iterators.meta",
       is_private: false,
       documentation: "-----------\n Linking --\n-----------",
       documentation_snippet: "",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Chain_From_Meta",
       qualified_name: "Iterators.Meta.Chain_From_Meta",
       signature: "iterators.meta.chain_from_meta",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Chain_From_Meta is new Meta2iter.Chain with null record;",
       }   ,
       {
       name: "Chain_To_Meta",
       qualified_name: "Iterators.Meta.Chain_To_Meta",
       signature: "iterators.meta.chain_to_meta",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Chain_To_Meta is new Iter2meta.Chain with null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Meta_Operator",
       qualified_name: "Iterators.Meta.Meta_Operator",
       signature: "iterators.meta.meta_operator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Meta_Operator is Iter2meta.Operator;",
       }   ,
   ]
,}
---
