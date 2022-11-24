---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Contexts.Facelets",
qualified_name: "ASF.Contexts.Facelets",
signature: "asf.contexts.facelets",
enclosing: "asf.contexts",
is_private: false,
documentation: "------------------------------\nFacelet context\n------------------------------\nThe <b>Facelet_Context</b> defines a context used exclusively when\nbuilding the component tree from the facelet nodes.  It allows to\ncompose the component tree by using other facelet fragments.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Facelet_Context",
       qualified_name: "ASF.Contexts.Facelets.Facelet_Context",
       signature: "asf.contexts.facelets.facelet_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Facelet_Context is abstract tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Facelet_Context_Access",
       qualified_name: "ASF.Contexts.Facelets.Facelet_Context_Access",
       signature: "asf.contexts.facelets.facelet_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Facelet_Context_Access is access all Facelet_Context'Class;",
       }   ,
   ]
,}
---
