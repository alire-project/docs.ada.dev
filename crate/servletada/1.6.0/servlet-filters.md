---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Filters",
qualified_name: "Servlet.Filters",
signature: "servlet.filters",
enclosing: "servlet",
is_private: false,
documentation: "------------------------------\nFilter interface\n------------------------------\nThe <b>Filter</b> interface defines one mandatory procedure through\nwhich the request/response pair are passed.\n\nThe <b>Filter</b> instance must be registered in the <b>Servlet_Registry</b>\nby using the <b>Add_Filter</b> procedure.  The same filter instance is used\nto process multiple requests possibly at the same time.",
documentation_snippet: "",
array_types:    [
       {
       name: "Filter_List",
       qualified_name: "Servlet.Filters.Filter_List",
       signature: "servlet.filters.filter_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_List is array (Natural range <>) of Filter_Access;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Filter",
       qualified_name: "Servlet.Filters.Filter",
       signature: "servlet.filters.filter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Filter_Access",
       qualified_name: "Servlet.Filters.Filter_Access",
       signature: "servlet.filters.filter_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_Access is access all Filter'Class;",
       }   ,
       {
       name: "Filter_List_Access",
       qualified_name: "Servlet.Filters.Filter_List_Access",
       signature: "servlet.filters.filter_list_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Filter_List_Access is access all Filter_List;",
       }   ,
   ]
,}
---
