---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Contexts",
qualified_name: "EL.Contexts",
signature: "el.contexts",
enclosing: "el",
is_private: false,
documentation: "The expression context provides information to resolve runtime\ninformation when evaluating an expression.  The context provides\na resolver whose role is to find variables given their name.",
documentation_snippet: "",
interface_types:    [
       {
       name: "ELContext",
       qualified_name: "EL.Contexts.ELContext",
       signature: "el.contexts.elcontext",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ELContext is limited interface;",
       }   ,
       {
       name: "ELResolver",
       qualified_name: "EL.Contexts.ELResolver",
       signature: "el.contexts.elresolver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ELResolver is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "ELContext_Access",
       qualified_name: "EL.Contexts.ELContext_Access",
       signature: "el.contexts.elcontext_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ELContext_Access is access all ELContext'Class;",
       }   ,
       {
       name: "ELResolver_Access",
       qualified_name: "EL.Contexts.ELResolver_Access",
       signature: "el.contexts.elresolver_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ELResolver_Access is access all ELResolver'Class;",
       }   ,
   ]
,}
---
