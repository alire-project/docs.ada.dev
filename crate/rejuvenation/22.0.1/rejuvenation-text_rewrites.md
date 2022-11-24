---
crate: rejuvenation
layout: gnatdoc
gnatdoc: {
name: "Rejuvenation.Text_Rewrites",
qualified_name: "Rejuvenation.Text_Rewrites",
signature: "rejuvenation.text_rewrites",
enclosing: "rejuvenation",
is_private: false,
documentation: "",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Text_Rewrite",
       qualified_name: "Rejuvenation.Text_Rewrites.Text_Rewrite",
       signature: "rejuvenation.text_rewrites.text_rewrite",
       enclosing: "",
       is_private: false,
       documentation: "The class Text_Rewrite collects multiple text rewrite operations, and\nafterwards applies them systematically. It combines two types of syntax\nfor specifying rewrites:\n  Abstract syntax: for locations in the original input\n  Concrete syntax: for any replacing texts\nThe abstract syntax is focused on physical AST nodes (= abstract syntax)\nfrom Libadalang.",
       documentation_snippet: "type Text_Rewrite is tagged private;",
       }   ,
       {
       name: "Text_Rewrite_Unit",
       qualified_name: "Rejuvenation.Text_Rewrites.Text_Rewrite_Unit",
       signature: "rejuvenation.text_rewrites.text_rewrite_unit",
       enclosing: "",
       is_private: false,
       documentation: "Text Rewrite for a Unit",
       documentation_snippet: "type Text_Rewrite_Unit is new Text_Rewrite with private;",
       }   ,
   ]
,}
---
