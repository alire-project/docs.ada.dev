---
crate: elada
layout: gnatdoc
gnatdoc: {
name: "EL.Contexts.Default",
qualified_name: "EL.Contexts.Default",
signature: "el.contexts.default",
enclosing: "el.contexts",
is_private: false,
documentation: "------------------------------\nDefault Context\n------------------------------\nContext information for expression evaluation.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Default_Context",
       qualified_name: "EL.Contexts.Default.Default_Context",
       signature: "el.contexts.default.default_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_Context is new Ada.Finalization.Controlled and ELContext with private;",
       }   ,
       {
       name: "Default_ELResolver",
       qualified_name: "EL.Contexts.Default.Default_ELResolver",
       signature: "el.contexts.default.default_elresolver",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_ELResolver is new ELResolver with private;",
       }   ,
       {
       name: "Guarded_Context",
       qualified_name: "EL.Contexts.Default.Guarded_Context",
       signature: "el.contexts.default.guarded_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Guarded_Context (Handler : not null access\n                        procedure (Ex : in Ada.Exceptions.Exception_Occurrence);\n                      Context : ELContext_Access)\n  is new Ada.Finalization.Limited_Controlled and ELContext with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Default_Context_Access",
       qualified_name: "EL.Contexts.Default.Default_Context_Access",
       signature: "el.contexts.default.default_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_Context_Access is access all Default_Context'Class;",
       }   ,
       {
       name: "Default_ELResolver_Access",
       qualified_name: "EL.Contexts.Default.Default_ELResolver_Access",
       signature: "el.contexts.default.default_elresolver_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Default_ELResolver_Access is access all Default_ELResolver'Class;",
       }   ,
       {
       name: "Guarded_Context_Access",
       qualified_name: "EL.Contexts.Default.Guarded_Context_Access",
       signature: "el.contexts.default.guarded_context_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Guarded_Context_Access is access all Default_Context'Class;",
       }   ,
   ]
,}
---
