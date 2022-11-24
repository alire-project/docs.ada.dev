---
crate: wikiada
layout: gnatdoc
gnatdoc: {
name: "Wiki.Filters",
qualified_name: "Wiki.Filters",
signature: "wiki.filters",
enclosing: "wiki",
is_private: false,
documentation: "------------------------------\nFilter type\n------------------------------",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Filter_Chain",
       qualified_name: "Wiki.Filters.Filter_Chain",
       signature: "wiki.filters.filter_chain",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Chain is new Filter_Type with private;",
       }   ,
       {
       name: "Filter_Type",
       qualified_name: "Wiki.Filters.Filter_Type",
       signature: "wiki.filters.filter_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Type is limited new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Filter_Type_Access",
       qualified_name: "Wiki.Filters.Filter_Type_Access",
       signature: "wiki.filters.filter_type_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Type_Access is access all Filter_Type'Class;",
       }   ,
   ]
,}
---
