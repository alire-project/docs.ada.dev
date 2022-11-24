---
crate: rejuvenation
layout: gnatdoc
gnatdoc: {
name: "Rejuvenation.Match_Patterns",
qualified_name: "Rejuvenation.Match_Patterns",
signature: "rejuvenation.match_patterns",
enclosing: "rejuvenation",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Match_Pattern",
       qualified_name: "Rejuvenation.Match_Patterns.Match_Pattern",
       signature: "rejuvenation.match_patterns.match_pattern",
       enclosing: "",
       is_private: false,
       documentation: "The class Match_Pattern represents a single occurrence of an AST pattern\nin an AST instance. An AST pattern or AST instance is a list of physical\nAST nodes from Libadalang.\n\nAST patterns are expressed as code snippets that can contain\nplaceholders that can be mapped to AST nodes from the AST instance.\nIf a placeholder occurs multiple times, then the string values of the\nmapped AST nodes must be identical.\n\nTo show diagnosis information about non-matches on the console, use:\n  Rejuvenation.Match_Pattern.DIAGNOSE := True;",
       documentation_snippet: "type Match_Pattern is tagged private;",
       }   ,
   ]
,variables:    [
       {
       name: "DIAGNOSE",
       qualified_name: "Rejuvenation.Match_Patterns.DIAGNOSE",
       signature: "rejuvenation.match_patterns.diagnose",
       enclosing: "",
       is_private: false,
       documentation: "Flag that indicates whether diagnosis information about non-matches is\ndisplayed on the console.",
       documentation_snippet: "DIAGNOSE : Boolean := False;",
       }   ,
   ]
,}
---
