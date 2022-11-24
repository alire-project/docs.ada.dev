---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Trace",
qualified_name: "Agpl.Trace",
signature: "agpl.trace",
enclosing: "agpl",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Levels",
       qualified_name: "Agpl.Trace.Levels",
       signature: "agpl.trace.levels",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Never\n@enum Debug\n@enum Informative\n@enum Warning\n  From here up, always logged even if section not enabled\n@enum Error\n@enum Always",
       documentation_snippet: "type Levels is (Never,\n                Debug,\n                Informative,\n                Warning,\n                Error,\n                Always);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Logger",
       qualified_name: "Agpl.Trace.Logger",
       signature: "agpl.trace.logger",
       enclosing: "",
       is_private: false,
       documentation: "Used to log inline in declarative blocks...\n\n@field Text\n@field Level",
       documentation_snippet: "type Logger (Text  : String_Access;\n             Level : Levels) is new Ada.Finalization.Limited_Controlled\nwith null record;",
       }   ,
       {
       name: "Object",
       qualified_name: "Agpl.Trace.Object",
       signature: "agpl.trace.object",
       enclosing: "",
       is_private: false,
       documentation: "null record;\n Should be an interface but the gnat bug with containers prevents it",
       documentation_snippet: "type Object is abstract tagged limited private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Decorator",
       qualified_name: "Agpl.Trace.Decorator",
       signature: "agpl.trace.decorator",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Decorator is access function (Text    : in String;\n                                   Level   : in Levels;\n                                   Section : in String) return String;",
       }   ,
       {
       name: "Object_Access",
       qualified_name: "Agpl.Trace.Object_Access",
       signature: "agpl.trace.object_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Access is access all Object'Class;",
       }   ,
       {
       name: "String_Access",
       qualified_name: "Agpl.Trace.String_Access",
       signature: "agpl.trace.string_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type String_Access is access all String;",
       }   ,
   ]
,subtypes:    [
       {
       name: "All_Levels",
       qualified_name: "Agpl.Trace.All_Levels",
       signature: "agpl.trace.all_levels",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype All_Levels     is Levels     range Never .. Always;",
       }   ,
       {
       name: "Warning_levels",
       qualified_name: "Agpl.Trace.Warning_levels",
       signature: "agpl.trace.warning_levels",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Warning_levels is All_Levels range Debug .. Error;",
       }   ,
   ]
,constants:    [
       {
       name: "Master_Switch",
       qualified_name: "Agpl.Trace.Master_Switch",
       signature: "agpl.trace.master_switch",
       enclosing: "",
       is_private: false,
       documentation: "when this is true, *EVERYTHING* will be traced.",
       documentation_snippet: "Master_Switch : constant Boolean := False;",
       }   ,
       {
       name: "Null_Object",
       qualified_name: "Agpl.Trace.Null_Object",
       signature: "agpl.trace.null_object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Object : constant Object_Access := null;",
       }   ,
   ]
,variables:    [
       {
       name: "Enabled",
       qualified_name: "Agpl.Trace.Enabled",
       signature: "agpl.trace.enabled",
       enclosing: "",
       is_private: false,
       documentation: "Inlining shall cause no calls when this is false.\nI have tested this; if this doesn't work something has gone wrong.",
       documentation_snippet: "Enabled : Boolean renames Trace_Is.Enabled;",
       }   ,
   ]
,}
---
