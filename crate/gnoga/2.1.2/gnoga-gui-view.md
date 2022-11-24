---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.View",
qualified_name: "Gnoga.Gui.View",
signature: "gnoga.gui.view",
enclosing: "gnoga.gui",
is_private: false,
documentation: "-----------------------------------------------------------------------\n  View_Base_Types\n-----------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "View_Base_Type",
       qualified_name: "Gnoga.Gui.View.View_Base_Type",
       signature: "gnoga.gui.view.view_base_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Base_Type is new Gnoga.Gui.Element.Element_Type with private;",
       }   ,
       {
       name: "View_Type",
       qualified_name: "Gnoga.Gui.View.View_Type",
       signature: "gnoga.gui.view.view_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Type is new View_Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer_To_View_Base_Class",
       qualified_name: "Gnoga.Gui.View.Pointer_To_View_Base_Class",
       signature: "gnoga.gui.view.pointer_to_view_base_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_View_Base_Class is access all View_Base_Type'Class;",
       }   ,
       {
       name: "Pointer_To_View_Class",
       qualified_name: "Gnoga.Gui.View.Pointer_To_View_Class",
       signature: "gnoga.gui.view.pointer_to_view_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_View_Class is access all View_Type'Class;",
       }   ,
       {
       name: "View_Access",
       qualified_name: "Gnoga.Gui.View.View_Access",
       signature: "gnoga.gui.view.view_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Access is access all View_Type;",
       }   ,
       {
       name: "View_Base_Access",
       qualified_name: "Gnoga.Gui.View.View_Base_Access",
       signature: "gnoga.gui.view.view_base_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type View_Base_Access is access all View_Base_Type;",
       }   ,
   ]
,}
---
