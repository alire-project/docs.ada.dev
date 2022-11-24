---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Plugins",
qualified_name: "Wiki.Plugins",
signature: "wiki.plugins",
enclosing: "wiki",
is_private: false,
documentation: "---------------------------------------------------------------------\n  wiki-plugins -- Wiki plugins\n  Copyright (C) 2016, 2018, 2020 Stephane Carrez\n  Written by Stephane Carrez (Stephane.Carrez@gmail.com)\n\n  Licensed under the Apache License, Version 2.0 (the \"License\");\n  you may not use this file except in compliance with the License.\n  You may obtain a copy of the License at\n\n      http://www.apache.org/licenses/LICENSE-2.0\n\n  Unless required by applicable law or agreed to in writing, software\n  distributed under the License is distributed on an \"AS IS\" BASIS,\n  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n  See the License for the specific language governing permissions and\n  limitations under the License.\n---------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Plugin_Context",
       qualified_name: "Wiki.Plugins.Plugin_Context",
       signature: "wiki.plugins.plugin_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plugin_Context is limited record\n   Previous    : access Plugin_Context;\n   Filters     : Wiki.Filters.Filter_Chain;\n   Factory     : Plugin_Factory_Access;\n   Variables   : Wiki.Attributes.Attribute_List;\n   Syntax      : Wiki.Wiki_Syntax;\n   Ident       : Wiki.Strings.UString;\n   Is_Hidden   : Boolean := False;\n   Is_Included : Boolean := False;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Plugin_Factory",
       qualified_name: "Wiki.Plugins.Plugin_Factory",
       signature: "wiki.plugins.plugin_factory",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plugin_Factory is limited interface;",
       }   ,
       {
       name: "Wiki_Plugin",
       qualified_name: "Wiki.Plugins.Wiki_Plugin",
       signature: "wiki.plugins.wiki_plugin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wiki_Plugin is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Plugin_Factory_Access",
       qualified_name: "Wiki.Plugins.Plugin_Factory_Access",
       signature: "wiki.plugins.plugin_factory_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Plugin_Factory_Access is access all Plugin_Factory'Class;",
       }   ,
       {
       name: "Wiki_Plugin_Access",
       qualified_name: "Wiki.Plugins.Wiki_Plugin_Access",
       signature: "wiki.plugins.wiki_plugin_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wiki_Plugin_Access is access all Wiki_Plugin'Class;",
       }   ,
   ]
,}
---
