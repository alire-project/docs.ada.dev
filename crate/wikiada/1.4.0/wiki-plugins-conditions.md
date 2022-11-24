---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Plugins.Conditions",
qualified_name: "Wiki.Plugins.Conditions",
signature: "wiki.plugins.conditions",
enclosing: "wiki.plugins",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Condition_Depth",
       qualified_name: "Wiki.Plugins.Conditions.Condition_Depth",
       signature: "wiki.plugins.conditions.condition_depth",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Condition_Depth is new Natural range 0 .. MAX_CONDITION_DEPTH;",
       }   ,
       {
       name: "Condition_Type",
       qualified_name: "Wiki.Plugins.Conditions.Condition_Type",
       signature: "wiki.plugins.conditions.condition_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Condition_Type is (CONDITION_IF, CONDITION_ELSIF, CONDITION_ELSE, CONDITION_END);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Condition_Plugin",
       qualified_name: "Wiki.Plugins.Conditions.Condition_Plugin",
       signature: "wiki.plugins.conditions.condition_plugin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Condition_Plugin is new Wiki_Plugin with private;",
       }   ,
   ]
,constants:    [
       {
       name: "MAX_CONDITION_DEPTH",
       qualified_name: "Wiki.Plugins.Conditions.MAX_CONDITION_DEPTH",
       signature: "wiki.plugins.conditions.max_condition_depth",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "MAX_CONDITION_DEPTH : constant Natural := 31;",
       }   ,
   ]
,}
---
