---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Random",
qualified_name: "Agpl.Random",
signature: "agpl.random",
enclosing: "agpl",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Random.Object",
       signature: "agpl.random.object",
       enclosing: "",
       is_private: false,
       documentation: "Use this object to have repeteability.\nUnless reset, this object has a default initialization which will make\nall runs identic.",
       documentation_snippet: "type Object is tagged limited private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Open_Uniformly_Distributed",
       qualified_name: "Agpl.Random.Open_Uniformly_Distributed",
       signature: "agpl.random.open_uniformly_distributed",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Open_Uniformly_Distributed is\n  Float range 0.0 .. Float'Pred (Uniformly_Distributed'Last);",
       }   ,
       {
       name: "Uniformly_Distributed",
       qualified_name: "Agpl.Random.Uniformly_Distributed",
       signature: "agpl.random.uniformly_distributed",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Uniformly_Distributed is\n  Ada.Numerics.Float_Random.Uniformly_Distributed;",
       }   ,
   ]
,}
---
