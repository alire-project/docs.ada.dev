---
crate: rxada
layout: gnatdoc
gnatdoc: {
name: "Rx.Debug",
qualified_name: "Rx.Debug",
signature: "rx.debug",
enclosing: "rx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Levels",
       qualified_name: "Rx.Debug.Levels",
       signature: "rx.debug.levels",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Impl\n  Implementation detail, for debugging\n@enum Note\n  Highly chatty\n@enum Info\n  Out-of-usual\n@enum Warn\n  Shouldn't happen but not critical (?)\n@enum Error\n  Something is definitely not working as expected",
       documentation_snippet: "type Levels is (Impl,\n                Note,\n                Info,\n                Warn,\n                Error\n                );",
       }   ,
   ]
,constants:    [
       {
       name: "Level",
       qualified_name: "Rx.Debug.Level",
       signature: "rx.debug.level",
       enclosing: "",
       is_private: false,
       documentation: "Minimum level a message has to have for it to be printed",
       documentation_snippet: "Level : constant Levels := Info;",
       }   ,
       {
       name: "Serialize_Trace",
       qualified_name: "Rx.Debug.Serialize_Trace",
       signature: "rx.debug.serialize_trace",
       enclosing: "",
       is_private: false,
       documentation: "This introduces a protected call, so use only for debugging purposes!",
       documentation_snippet: "Serialize_Trace : constant Boolean := True;",
       }   ,
   ]
,}
---
