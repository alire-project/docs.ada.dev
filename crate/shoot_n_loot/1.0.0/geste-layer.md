---
crate: shoot_n_loot
layout: gnatdoc
gnatdoc: {
name: "Layer",
qualified_name: "GESTE.Layer",
signature: "geste.layer",
enclosing: "geste",
is_private: false,
documentation: "",
documentation_snippet: "",
access_types:    [
       {
       name: "Const_Ref",
       qualified_name: "GESTE.Layer.Const_Ref",
       signature: "geste.layer.const_ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Const_Ref is access constant Class;",
       }   ,
       {
       name: "Ref",
       qualified_name: "GESTE.Layer.Ref",
       signature: "geste.layer.ref",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ref is access all Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Class",
       qualified_name: "GESTE.Layer.Class",
       signature: "geste.layer.class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Class is Instance'Class;",
       }   ,
       {
       name: "Instance",
       qualified_name: "GESTE.Layer.Instance",
       signature: "geste.layer.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Layer_Type;",
       }   ,
   ]
,}
---
