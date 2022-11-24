---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Plugin.JSTree",
qualified_name: "Gnoga.Gui.Plugin.JSTree",
signature: "gnoga.gui.plugin.jstree",
enclosing: "gnoga.gui.plugin",
is_private: false,
documentation: "JSTree Ada API is inspired from a JQuery plugin to create dropdown trees from <ul> lists.\nhttps://github.com/vakata/jstree\nJSTree is released under the (http://opensource.org/licenses/MIT) MIT License.\nSome comments come from JSTree documentation.\nBoth static and dynamic set of API are proposed. Don't mix them.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Plugins_Enum",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Plugins_Enum",
       signature: "gnoga.gui.plugin.jstree.plugins_enum",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum CheckBox\n  Renders a checkbox icon in front of each node, making multi-selection easy.\n@enum ContextMenu\n  Makes it possible to right click nodes and shows a list of\n  configurable actions in a menu.\n@enum DragAndDrop\n  Makes it possible to drag and drop tree nodes and rearrange the tree.\n@enum Sort\n  Automatically arranges all sibling nodes according to a comparison function,\n  which defaults to alphabetical order.\n@enum Unique\n  Enforces that no nodes with the same name can coexist as siblings\n  prevents renaming and moving nodes to a parent,\n  which already contains a node with the same name.\n@enum WholeRow",
       documentation_snippet: "type Plugins_Enum is (CheckBox,\nContextMenu,\nDragAndDrop,\nSort,\nUnique,\nWholeRow\n   );",
       }   ,
   ]
,array_types:    [
       {
       name: "Plugins_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Plugins_Type",
       signature: "gnoga.gui.plugin.jstree.plugins_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plugins_Type is array (Plugins_Enum) of Boolean with\n   Default_Component_Value => False;",
       }   ,
   ]
,record_types:    [
       {
       name: "Core_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Core_Type",
       signature: "gnoga.gui.plugin.jstree.core_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Core_Type is record\n   Animation : Natural := 200;\n   Multiple : Boolean := True;\n   Force_Text : Boolean := False;\n   DblClick_Toggle : Boolean := True;\n   Themes : Themes_Type;\nend record;",
       }   ,
       {
       name: "Option_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Option_Type",
       signature: "gnoga.gui.plugin.jstree.option_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Option_Type is record\n   Core    : Core_Type;\n   Plugins : Plugins_Type;\nend record;",
       }   ,
       {
       name: "Themes_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Themes_Type",
       signature: "gnoga.gui.plugin.jstree.themes_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Themes_Type is record\n   Dots : Boolean := True;\n   Icons : Boolean := True;\n   Stripes : Boolean := False;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "JSTree_Item_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.JSTree_Item_Type",
       signature: "gnoga.gui.plugin.jstree.jstree_item_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JSTree_Item_Type is new Gnoga.Gui.Element.List.List_Item_Type with private;",
       }   ,
       {
       name: "JSTree_Type",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.JSTree_Type",
       signature: "gnoga.gui.plugin.jstree.jstree_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JSTree_Type is new Gnoga.Gui.Element.List.Unordered_List_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "JSTree_Access",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.JSTree_Access",
       signature: "gnoga.gui.plugin.jstree.jstree_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JSTree_Access is access all JSTree_Type;",
       }   ,
       {
       name: "JSTree_Event",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.JSTree_Event",
       signature: "gnoga.gui.plugin.jstree.jstree_event",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JSTree_Event is access procedure\n  (Object : in out Gnoga.Gui.Base.Base_Type'Class;\n   Node   : in     String);",
       }   ,
       {
       name: "JSTree_Item_Access",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.JSTree_Item_Access",
       signature: "gnoga.gui.plugin.jstree.jstree_item_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type JSTree_Item_Access is access all JSTree_Item_Type;",
       }   ,
       {
       name: "Pointer_To_JSTree_Class",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Pointer_To_JSTree_Class",
       signature: "gnoga.gui.plugin.jstree.pointer_to_jstree_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_JSTree_Class is access all JSTree_Type'Class;",
       }   ,
       {
       name: "Pointer_To_JSTree_Item_Class",
       qualified_name: "Gnoga.Gui.Plugin.JSTree.Pointer_To_JSTree_Item_Class",
       signature: "gnoga.gui.plugin.jstree.pointer_to_jstree_item_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_JSTree_Item_Class is access all JSTree_Item_Type'Class;",
       }   ,
   ]
,}
---
