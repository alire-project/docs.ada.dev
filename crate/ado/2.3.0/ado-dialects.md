---
crate: ado
layout: gnatdoc
gnatdoc: {
name: "ADO.Dialects",
qualified_name: "ADO.Dialects",
signature: "ado.dialects",
enclosing: "ado",
is_private: false,
documentation: "--------------------\nSQL Dialect\n--------------------\nThe <b>Dialect</b> defines the specific characteristics that must be\ntaken into account when building the SQL statement.  This includes:\n<ul>\n  <li>The definition of reserved keywords that must be escaped</li>\n  <li>How to escape those keywords</li>\n  <li>How to escape special characters</li>\n</ul>",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Dialect",
       qualified_name: "ADO.Dialects.Dialect",
       signature: "ado.dialects.dialect",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Dialect is abstract tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Dialect_Access",
       qualified_name: "ADO.Dialects.Dialect_Access",
       signature: "ado.dialects.dialect_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Dialect_Access is access all Dialect'Class;",
       }   ,
   ]
,}
---
