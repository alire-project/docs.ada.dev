---
crate: ayacc
layout: gnatdoc
gnatdoc: {
name: "Rule_Table",
qualified_name: "Rule_Table",
signature: "rule_table",
enclosing: "",
is_private: false,
documentation: "This package is used to store and access the rules\nof the input grammar.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Rule",
       qualified_name: "Rule_Table.Rule",
       signature: "rule_table.rule",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rule is range 0..Max_Rules - 1;",
       }   ,
   ]
,constants:    [
       {
       name: "Max_Rules",
       qualified_name: "Rule_Table.Max_Rules",
       signature: "rule_table.max_rules",
       enclosing: "",
       is_private: false,
       documentation: "An arbitrary upper bound.\nif you raise this above 3_000\nyou will also need to make\nchanges in parse_table_body\nand parse_template_file.",
       documentation_snippet: "Max_Rules  : constant := 1_000;",
       }   ,
   ]
,}
---
