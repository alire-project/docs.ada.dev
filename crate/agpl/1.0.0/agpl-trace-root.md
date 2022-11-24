---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Trace.Root",
qualified_name: "Agpl.Trace.Root",
signature: "agpl.trace.root",
enclosing: "agpl.trace",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Trace.Root.Object",
       signature: "agpl.trace.root.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is limited new Trace.Object with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Access",
       qualified_name: "Agpl.Trace.Root.Object_Access",
       signature: "agpl.trace.root.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Access is access all Object'Class;",
       }   ,
   ]
,variables:    [
       {
       name: "Bypass_Section_Level",
       qualified_name: "Agpl.Trace.Root.Bypass_Section_Level",
       signature: "agpl.trace.root.bypass_section_level",
       enclosing: "",
       is_private: false,
       documentation: ">= this is logged regardless of section",
       documentation_snippet: "Bypass_Section_Level : Levels := Warning;",
       }   ,
   ]
,}
---
