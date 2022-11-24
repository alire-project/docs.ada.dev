---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Models.Selects",
qualified_name: "ASF.Models.Selects",
signature: "asf.models.selects",
enclosing: "asf.models",
is_private: false,
documentation: "------------------------------\nSelect Item\n------------------------------\nThe <b>Select_Item</b> type describes a single option of a list of options\nused by the <b>UISelectOne</b> or <b>UISelectMany</b> components.\nThe select item contains:\n<ul>\n  <li>A label\n  <li>A value\n  <li>A description\n  <li>Whether the select item is disabled or not\n  <li>Whether the label is escaped or not\n</ul>\nAn application creates the <b>Select_Item</b> instances and passes them\nto the ASF components through an <b>Util.Beans.Objects.Object</b> value.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Select_Item",
       qualified_name: "ASF.Models.Selects.Select_Item",
       signature: "asf.models.selects.select_item",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Select_Item is new Util.Beans.Basic.Readonly_Bean with private;",
       }   ,
       {
       name: "Select_Item_List",
       qualified_name: "ASF.Models.Selects.Select_Item_List",
       signature: "asf.models.selects.select_item_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Select_Item_List is new Util.Beans.Basic.List_Bean with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Select_Item_Access",
       qualified_name: "ASF.Models.Selects.Select_Item_Access",
       signature: "asf.models.selects.select_item_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Select_Item_Access is access all Select_Item;",
       }   ,
       {
       name: "Select_Item_List_Access",
       qualified_name: "ASF.Models.Selects.Select_Item_List_Access",
       signature: "asf.models.selects.select_item_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Select_Item_List_Access is access all Select_Item_List;",
       }   ,
   ]
,}
---
