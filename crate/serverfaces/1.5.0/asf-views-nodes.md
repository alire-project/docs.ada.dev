---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Views.Nodes",
qualified_name: "ASF.Views.Nodes",
signature: "asf.views.nodes",
enclosing: "asf.views",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-views-nodes -- Facelet node tree representation\n  Copyright (C) 2009, 2010, 2011, 2012, 2013, 2014, 2018, 2022 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Cursor",
       qualified_name: "ASF.Views.Nodes.Cursor",
       signature: "asf.views.nodes.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor is private;",
       }   ,
       {
       name: "Name_Access",
       qualified_name: "ASF.Views.Nodes.Name_Access",
       signature: "asf.views.nodes.name_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Name_Access is new Util.Strings.Name_Access;",
       }   ,
       {
       name: "Tag_Attribute",
       qualified_name: "ASF.Views.Nodes.Tag_Attribute",
       signature: "asf.views.nodes.tag_attribute",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Attribute is limited private;",
       }   ,
   ]
,array_types:    [
       {
       name: "Expression_Access_Array",
       qualified_name: "ASF.Views.Nodes.Expression_Access_Array",
       signature: "asf.views.nodes.expression_access_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expression_Access_Array is array (Natural range <>) of EL.Expressions.Expression_Access;",
       }   ,
       {
       name: "Tag_Attribute_Array",
       qualified_name: "ASF.Views.Nodes.Tag_Attribute_Array",
       signature: "asf.views.nodes.tag_attribute_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Attribute_Array is array (Natural range <>) of aliased Tag_Attribute;",
       }   ,
   ]
,record_types:    [
       {
       name: "Binding_Type",
       qualified_name: "ASF.Views.Nodes.Binding_Type",
       signature: "asf.views.nodes.binding_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Type is record\n   Name      : Name_Access;\n   Component : ASF.Views.Nodes.Create_Access;\n   Tag       : ASF.Views.Nodes.Tag_Node_Create_Access;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Tag_Node",
       qualified_name: "ASF.Views.Nodes.Tag_Node",
       signature: "asf.views.nodes.tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Node is tagged limited private;",
       }   ,
       {
       name: "Text_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Text_Tag_Node",
       signature: "asf.views.nodes.text_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Tag_Node is new Tag_Node with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Binding_Access",
       qualified_name: "ASF.Views.Nodes.Binding_Access",
       signature: "asf.views.nodes.binding_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Access is access constant Binding_Type;",
       }   ,
       {
       name: "Create_Access",
       qualified_name: "ASF.Views.Nodes.Create_Access",
       signature: "asf.views.nodes.create_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Create_Access is access function return ASF.Components.Base.UIComponent_Access;",
       }   ,
       {
       name: "Expression_Access_Array_Access",
       qualified_name: "ASF.Views.Nodes.Expression_Access_Array_Access",
       signature: "asf.views.nodes.expression_access_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Expression_Access_Array_Access is access Expression_Access_Array;",
       }   ,
       {
       name: "Tag_Attribute_Access",
       qualified_name: "ASF.Views.Nodes.Tag_Attribute_Access",
       signature: "asf.views.nodes.tag_attribute_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Attribute_Access is access all Tag_Attribute;",
       }   ,
       {
       name: "Tag_Attribute_Array_Access",
       qualified_name: "ASF.Views.Nodes.Tag_Attribute_Array_Access",
       signature: "asf.views.nodes.tag_attribute_array_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Attribute_Array_Access is access Tag_Attribute_Array;",
       }   ,
       {
       name: "Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Tag_Node_Access",
       signature: "asf.views.nodes.tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Node_Access is access all Tag_Node'Class;",
       }   ,
       {
       name: "Tag_Node_Create_Access",
       qualified_name: "ASF.Views.Nodes.Tag_Node_Create_Access",
       signature: "asf.views.nodes.tag_node_create_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tag_Node_Create_Access is access\n  function (Binding    : in Binding_Type;\n            Line       : in Line_Info;\n            Parent     : in Tag_Node_Access;\n            Attributes : in Tag_Attribute_Array_Access) return Tag_Node_Access;",
       }   ,
       {
       name: "Text_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Text_Tag_Node_Access",
       signature: "asf.views.nodes.text_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Text_Tag_Node_Access is access all Text_Tag_Node;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Binding",
       qualified_name: "ASF.Views.Nodes.Null_Binding",
       signature: "asf.views.nodes.null_binding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Binding : constant Binding_Type := Binding_Type '(null, null, null);",
       }   ,
   ]
,}
---
