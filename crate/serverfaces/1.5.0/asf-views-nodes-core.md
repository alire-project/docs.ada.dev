---
crate: serverfaces
layout: gnatdoc
gnatdoc: {
name: "ASF.Views.Nodes.Core",
qualified_name: "ASF.Views.Nodes.Core",
signature: "asf.views.nodes.core",
enclosing: "asf.views.nodes",
is_private: false,
documentation: "---------------------------------------------------------------------\n  asf-views-nodes-core -- Core nodes\n  Copyright (C) 2009 - 2021 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Choose_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Core.Choose_Tag_Node",
       signature: "asf.views.nodes.core.choose_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Choose_Tag_Node is new Tag_Node with private;",
       }   ,
       {
       name: "If_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Core.If_Tag_Node",
       signature: "asf.views.nodes.core.if_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type If_Tag_Node is new Tag_Node with private;",
       }   ,
       {
       name: "Otherwise_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Core.Otherwise_Tag_Node",
       signature: "asf.views.nodes.core.otherwise_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Otherwise_Tag_Node is new Tag_Node with null record;",
       }   ,
       {
       name: "Set_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Core.Set_Tag_Node",
       signature: "asf.views.nodes.core.set_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Set_Tag_Node is new Tag_Node with private;",
       }   ,
       {
       name: "When_Tag_Node",
       qualified_name: "ASF.Views.Nodes.Core.When_Tag_Node",
       signature: "asf.views.nodes.core.when_tag_node",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type When_Tag_Node is new If_Tag_Node with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Choose_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Core.Choose_Tag_Node_Access",
       signature: "asf.views.nodes.core.choose_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Choose_Tag_Node_Access is access all Choose_Tag_Node'Class;",
       }   ,
       {
       name: "If_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Core.If_Tag_Node_Access",
       signature: "asf.views.nodes.core.if_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type If_Tag_Node_Access is access all If_Tag_Node'Class;",
       }   ,
       {
       name: "Otherwise_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Core.Otherwise_Tag_Node_Access",
       signature: "asf.views.nodes.core.otherwise_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Otherwise_Tag_Node_Access is access all Otherwise_Tag_Node'Class;",
       }   ,
       {
       name: "Set_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Core.Set_Tag_Node_Access",
       signature: "asf.views.nodes.core.set_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Set_Tag_Node_Access is access all Set_Tag_Node'Class;",
       }   ,
       {
       name: "When_Tag_Node_Access",
       qualified_name: "ASF.Views.Nodes.Core.When_Tag_Node_Access",
       signature: "asf.views.nodes.core.when_tag_node_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type When_Tag_Node_Access is access all When_Tag_Node'Class;",
       }   ,
   ]
,constants:    [
       {
       name: "FN_URI",
       qualified_name: "ASF.Views.Nodes.Core.FN_URI",
       signature: "asf.views.nodes.core.fn_uri",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "FN_URI : constant String := \"http://java.sun.com/jsp/jstl/functions\";",
       }   ,
   ]
,}
---
