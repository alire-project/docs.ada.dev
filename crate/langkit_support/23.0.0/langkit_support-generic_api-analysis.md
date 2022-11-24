---
crate: langkit_support
layout: gnatdoc
gnatdoc: {
name: "Langkit_Support.Generic_API.Analysis",
qualified_name: "Langkit_Support.Generic_API.Analysis",
signature: "langkit_support.generic_api.analysis",
enclosing: "langkit_support.generic_api",
is_private: false,
documentation: "This package provides a generic API so that programs can work with the\n$.Analysis packages of all Langkit-generated libraries.\n\nNote that it is experimental at this stage, and thus not officially\nsupported.\n\nTODO??? Create a language-agnostic documentation for all the concepts\nreferenced here (context, unit, node, token, trivia, ...).",
documentation_snippet: "",
simple_types:    [
       {
       name: "Visit_Status",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Visit_Status",
       signature: "langkit_support.generic_api.analysis.visit_status",
       enclosing: "",
       is_private: false,
       documentation: "Helper type to control the node traversal process. See the ``Traverse``\nsubprograms below.\n\n@enum Into\n@enum Over\n@enum Stop",
       documentation_snippet: "type Visit_Status is (Into, Over, Stop);",
       }   ,
   ]
,array_types:    [
       {
       name: "Lk_Node_Array",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Lk_Node_Array",
       signature: "langkit_support.generic_api.analysis.lk_node_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lk_Node_Array is array (Positive range <>) of Lk_Node;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Lk_Context",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Lk_Context",
       signature: "langkit_support.generic_api.analysis.lk_context",
       enclosing: "",
       is_private: false,
       documentation: "Reference types to actual context/unit/node/token objects. Only\n``Lk_Context`` and ``Lk_Unit`` are strong references (designated object\nlives as long as the reference exists): ``Lk_Node`` and ``Lk_Token_Ref``\nare weak references (designated object may be destroyed even if there\nare still references to it, but usage of such a stale reference is\nproperly rejected).",
       documentation_snippet: "type Lk_Context is tagged private;",
       }   ,
       {
       name: "Lk_Node",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Lk_Node",
       signature: "langkit_support.generic_api.analysis.lk_node",
       enclosing: "",
       is_private: false,
       documentation: "Reference types to actual context/unit/node/token objects. Only\n``Lk_Context`` and ``Lk_Unit`` are strong references (designated object\nlives as long as the reference exists): ``Lk_Node`` and ``Lk_Token_Ref``\nare weak references (designated object may be destroyed even if there\nare still references to it, but usage of such a stale reference is\nproperly rejected).",
       documentation_snippet: "type Lk_Node is tagged private;",
       }   ,
       {
       name: "Lk_Token",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Lk_Token",
       signature: "langkit_support.generic_api.analysis.lk_token",
       enclosing: "",
       is_private: false,
       documentation: "Reference types to actual context/unit/node/token objects. Only\n``Lk_Context`` and ``Lk_Unit`` are strong references (designated object\nlives as long as the reference exists): ``Lk_Node`` and ``Lk_Token_Ref``\nare weak references (designated object may be destroyed even if there\nare still references to it, but usage of such a stale reference is\nproperly rejected).",
       documentation_snippet: "type Lk_Token is tagged private;",
       }   ,
       {
       name: "Lk_Unit",
       qualified_name: "Langkit_Support.Generic_API.Analysis.Lk_Unit",
       signature: "langkit_support.generic_api.analysis.lk_unit",
       enclosing: "",
       is_private: false,
       documentation: "Reference types to actual context/unit/node/token objects. Only\n``Lk_Context`` and ``Lk_Unit`` are strong references (designated object\nlives as long as the reference exists): ``Lk_Node`` and ``Lk_Token_Ref``\nare weak references (designated object may be destroyed even if there\nare still references to it, but usage of such a stale reference is\nproperly rejected).",
       documentation_snippet: "type Lk_Unit is new Langkit_Support.Text.Text_Buffer_Ifc with private;",
       }   ,
   ]
,constants:    [
       {
       name: "No_Lk_Context",
       qualified_name: "Langkit_Support.Generic_API.Analysis.No_Lk_Context",
       signature: "langkit_support.generic_api.analysis.no_lk_context",
       enclosing: "",
       is_private: false,
       documentation: "Special value to mean the absence of analysis context",
       documentation_snippet: "No_Lk_Context : constant Lk_Context;",
       }   ,
       {
       name: "No_Lk_Node",
       qualified_name: "Langkit_Support.Generic_API.Analysis.No_Lk_Node",
       signature: "langkit_support.generic_api.analysis.no_lk_node",
       enclosing: "",
       is_private: false,
       documentation: "Special value to mean the absence of analysis node",
       documentation_snippet: "No_Lk_Node : constant Lk_Node;",
       }   ,
       {
       name: "No_Lk_Token",
       qualified_name: "Langkit_Support.Generic_API.Analysis.No_Lk_Token",
       signature: "langkit_support.generic_api.analysis.no_lk_token",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "No_Lk_Token : constant Lk_Token;",
       }   ,
       {
       name: "No_Lk_Unit",
       qualified_name: "Langkit_Support.Generic_API.Analysis.No_Lk_Unit",
       signature: "langkit_support.generic_api.analysis.no_lk_unit",
       enclosing: "",
       is_private: false,
       documentation: "Special value to mean the absence of analysis unit",
       documentation_snippet: "No_Lk_Unit : constant Lk_Unit;",
       }   ,
   ]
,}
---
