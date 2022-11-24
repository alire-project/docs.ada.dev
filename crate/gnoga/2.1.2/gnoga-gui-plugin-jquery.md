---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Plugin.jQuery",
qualified_name: "Gnoga.Gui.Plugin.jQuery",
signature: "gnoga.gui.plugin.jquery",
enclosing: "gnoga.gui.plugin",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  jQuery_Type\n-----------------------------------------------------------------------\n  Binding to allow for general jQuery use outside of Gnoga Objects",
documentation_snippet: "",
tagged_types:    [
       {
       name: "jQuery_Type",
       qualified_name: "Gnoga.Gui.Plugin.jQuery.jQuery_Type",
       signature: "gnoga.gui.plugin.jquery.jquery_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type jQuery_Type is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "jQuery_Access",
       qualified_name: "Gnoga.Gui.Plugin.jQuery.jQuery_Access",
       signature: "gnoga.gui.plugin.jquery.jquery_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type jQuery_Access is access all jQuery_Type;",
       }   ,
       {
       name: "Pointer_To_jQuery_Class",
       qualified_name: "Gnoga.Gui.Plugin.jQuery.Pointer_To_jQuery_Class",
       signature: "gnoga.gui.plugin.jquery.pointer_to_jquery_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_jQuery_Class is access all jQuery_Type'Class;",
       }   ,
   ]
,}
---
