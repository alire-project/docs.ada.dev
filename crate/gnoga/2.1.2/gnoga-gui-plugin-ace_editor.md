---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Plugin.Ace_Editor",
qualified_name: "Gnoga.Gui.Plugin.Ace_Editor",
signature: "gnoga.gui.plugin.ace_editor",
enclosing: "gnoga.gui.plugin",
is_private: false,
documentation: "Binding to the Ace Code Editor.\nAce is an embeddable code editor written in JavaScript.\nhttp://ace.c9.io/#nav=about\nAce is released under the BSD License.\nSome comments come from Ace documentation.",
documentation_snippet: "",
record_types:    [
       {
       name: "Position_Type",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Position_Type",
       signature: "gnoga.gui.plugin.ace_editor.position_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Position_Type is record\n   Row, Column : Integer;\nend record;",
       }   ,
       {
       name: "Range_Type",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Range_Type",
       signature: "gnoga.gui.plugin.ace_editor.range_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Range_Type is record\n   Start_Row, Start_Column, End_Row, End_Column : Integer;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Ace_Editor_Type",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Ace_Editor_Type",
       signature: "gnoga.gui.plugin.ace_editor.ace_editor_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ace_Editor_Type is new Gnoga.Gui.View.View_Type with private;",
       }   ,
       {
       name: "Anchor_Type",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Anchor_Type",
       signature: "gnoga.gui.plugin.ace_editor.anchor_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Anchor_Type is new Gnoga.Gui.Base.Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Ace_Editor_Access",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Ace_Editor_Access",
       signature: "gnoga.gui.plugin.ace_editor.ace_editor_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Ace_Editor_Access is access all Ace_Editor_Type;",
       }   ,
       {
       name: "Anchor_Access",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Anchor_Access",
       signature: "gnoga.gui.plugin.ace_editor.anchor_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Anchor_Access is access all Anchor_Type;",
       }   ,
       {
       name: "Pointer_To_Ace_Editor_Class",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Pointer_To_Ace_Editor_Class",
       signature: "gnoga.gui.plugin.ace_editor.pointer_to_ace_editor_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Ace_Editor_Class is access all Ace_Editor_Type'Class;",
       }   ,
       {
       name: "Pointer_To_Anchor_Class",
       qualified_name: "Gnoga.Gui.Plugin.Ace_Editor.Pointer_To_Anchor_Class",
       signature: "gnoga.gui.plugin.ace_editor.pointer_to_anchor_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Anchor_Class is access all Anchor_Type'Class;",
       }   ,
   ]
,}
---
