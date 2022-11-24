---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Post_Processing_Contexts_Function_Access",
qualified_name: "Post_Processing_Contexts_Function_Access",
signature: "post_processing_contexts_function_access",
enclosing: "",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Post_Processing_Context_Function_Access",
       qualified_name: "Post_Processing_Contexts_Function_Access.Post_Processing_Context_Function_Access",
       signature: "post_processing_contexts_function_access.post_processing_context_function_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Post_Processing_Context_Function_Access is\n  new Post_Processing_Context with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Access_Function_Get_Post_Processing_Context",
       qualified_name: "Post_Processing_Contexts_Function_Access.Access_Function_Get_Post_Processing_Context",
       signature: "post_processing_contexts_function_access.access_function_get_post_processing_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Access_Function_Get_Post_Processing_Context is\nnot null access function (Unit : Analysis_Unit) return Node_List.Vector;",
       }   ,
   ]
,}
---
