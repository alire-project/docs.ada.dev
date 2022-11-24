---
crate: rewriters
layout: gnatdoc
gnatdoc: {
name: "Match_Accepters_Function_Access",
qualified_name: "Match_Accepters_Function_Access",
signature: "match_accepters_function_access",
enclosing: "",
is_private: false,
documentation: "TODO:  create Match_Accepters for some simple regular occuring matches\nsuch that is match_accepter will be less often used.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Match_Accepter_Function_Access",
       qualified_name: "Match_Accepters_Function_Access.Match_Accepter_Function_Access",
       signature: "match_accepters_function_access.match_accepter_function_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Match_Accepter_Function_Access is new Match_Accepter with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Access_Function_Is_Match_Acceptable",
       qualified_name: "Match_Accepters_Function_Access.Access_Function_Is_Match_Acceptable",
       signature: "match_accepters_function_access.access_function_is_match_acceptable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Access_Function_Is_Match_Acceptable is\nnot null access function (M_P : Match_Pattern) return Boolean;",
       }   ,
   ]
,}
---
