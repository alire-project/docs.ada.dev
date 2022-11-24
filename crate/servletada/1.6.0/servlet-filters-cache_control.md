---
crate: servletada
layout: gnatdoc
gnatdoc: {
name: "Servlet.Filters.Cache_Control",
qualified_name: "Servlet.Filters.Cache_Control",
signature: "servlet.filters.cache_control",
enclosing: "servlet.filters",
is_private: false,
documentation: "Filter configuration parameter, when not empty, add a Vary header in the response.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Cache_Control_Filter",
       qualified_name: "Servlet.Filters.Cache_Control.Cache_Control_Filter",
       signature: "servlet.filters.cache_control.cache_control_filter",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cache_Control_Filter is new Servlet.Filters.Filter with record\n   Vary                 : Ada.Strings.Unbounded.Unbounded_String;\n   Cache_Control_Header : Ada.Strings.Unbounded.Unbounded_String;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "CACHE_CONTROL_PARAM",
       qualified_name: "Servlet.Filters.Cache_Control.CACHE_CONTROL_PARAM",
       signature: "servlet.filters.cache_control.cache_control_param",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "CACHE_CONTROL_PARAM  : constant String := \"header.cache-control\";",
       }   ,
       {
       name: "VARY_HEADER_PARAM",
       qualified_name: "Servlet.Filters.Cache_Control.VARY_HEADER_PARAM",
       signature: "servlet.filters.cache_control.vary_header_param",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "VARY_HEADER_PARAM    : constant String := \"header.vary\";",
       }   ,
   ]
,}
---
