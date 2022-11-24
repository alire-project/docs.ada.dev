---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Debug.Timer",
qualified_name: "Agpl.Debug.Timer",
signature: "agpl.debug.timer",
enclosing: "agpl.debug",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Debug.Timer.Object",
       signature: "agpl.debug.timer.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (\n   Id           : access String            := Unknown_Context'Access;\n   Trace        : Agpl.Trace.Object_Access := Agpl.Trace.Null_Object;\n   Deadline     : Natural                  := 10_000;\n   Always_Raise : Boolean                  := False)\nis limited private;",
       }   ,
   ]
,variables:    [
       {
       name: "Unknown_Context",
       qualified_name: "Agpl.Debug.Timer.Unknown_Context",
       signature: "agpl.debug.timer.unknown_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Unknown_Context : aliased String := \"Unknown context\";",
       }   ,
   ]
,}
---
