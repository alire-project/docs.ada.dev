---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Window",
qualified_name: "Gnoga.Gui.Window",
signature: "gnoga.gui.window",
enclosing: "gnoga.gui",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  Window_Type\n-----------------------------------------------------------------------\n  Window_Type is the class encapsulating an individual Gnoga browser\n  window or tab.",
documentation_snippet: "",
record_types:    [
       {
       name: "Storage_Event_Record",
       qualified_name: "Gnoga.Gui.Window.Storage_Event_Record",
       signature: "gnoga.gui.window.storage_event_record",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Event_Record is record\n   Name      : String;\n   Old_Value : String;\n   New_Value : String;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Window_Type",
       qualified_name: "Gnoga.Gui.Window.Window_Type",
       signature: "gnoga.gui.window.window_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Window_Type is new Gnoga.Gui.Base.Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer_To_Window_Class",
       qualified_name: "Gnoga.Gui.Window.Pointer_To_Window_Class",
       signature: "gnoga.gui.window.pointer_to_window_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Window_Class is access all Window_Type'Class;",
       }   ,
       {
       name: "Storage_Event",
       qualified_name: "Gnoga.Gui.Window.Storage_Event",
       signature: "gnoga.gui.window.storage_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Storage_Event is access procedure\n  (Object        : in out Gnoga.Gui.Base.Base_Type'Class;\n   Storage_Event : in     Storage_Event_Record);",
       }   ,
       {
       name: "Window_Access",
       qualified_name: "Gnoga.Gui.Window.Window_Access",
       signature: "gnoga.gui.window.window_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Window_Access is access all Window_Type;",
       }   ,
   ]
,}
---
