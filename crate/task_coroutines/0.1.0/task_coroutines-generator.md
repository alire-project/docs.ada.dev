---
crate: task_coroutines
layout: gnatdoc
gnatdoc: {
name: "Task_Coroutines.Generator",
qualified_name: "Task_Coroutines.Generator",
signature: "task_coroutines.generator",
enclosing: "task_coroutines",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Cursor_Type",
       qualified_name: "Task_Coroutines.Generator.Cursor_Type",
       signature: "task_coroutines.generator.cursor_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor_Type is null record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Inner_Control",
       qualified_name: "Task_Coroutines.Generator.Inner_Control",
       signature: "task_coroutines.generator.inner_control",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Inner_Control is tagged limited private;",
       }   ,
       {
       name: "Instance",
       qualified_name: "Task_Coroutines.Generator.Instance",
       signature: "task_coroutines.generator.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Instance\nis tagged limited private\n  with Iterable => (First       => First,\n                    Next        => Next,\n                    Has_Element => Has_Element,\n                    Element     => Element);",
       }   ,
   ]
,access_types:    [
       {
       name: "Generator_Proc",
       qualified_name: "Task_Coroutines.Generator.Generator_Proc",
       signature: "task_coroutines.generator.generator_proc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Generator_Proc is access procedure (Ctrl : in out Inner_Control'Class);",
       }   ,
   ]
,}
---
