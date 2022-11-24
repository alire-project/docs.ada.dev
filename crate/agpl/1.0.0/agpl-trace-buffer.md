---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Trace.Buffer",
qualified_name: "Agpl.Trace.Buffer",
signature: "agpl.trace.buffer",
enclosing: "agpl.trace",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Log_Entry",
       qualified_name: "Agpl.Trace.Buffer.Log_Entry",
       signature: "agpl.trace.buffer.log_entry",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Log_Entry is record\n   Level : Levels;\n   Text  : Ustring;\n   Sect  : Ustring;\n   Stamp : Ada.Calendar.Time;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Trace.Buffer.Object",
       signature: "agpl.trace.buffer.object",
       enclosing: "",
       is_private: false,
       documentation: "Stores at most Max_Length log messages",
       documentation_snippet: "type Object (Max_Length : Natural) is new Root.Object with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Access",
       qualified_name: "Agpl.Trace.Buffer.Object_Access",
       signature: "agpl.trace.buffer.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Access is access all Object'Class;",
       }   ,
   ]
,}
---
