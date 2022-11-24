---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Server.Migration",
qualified_name: "Gnoga.Server.Migration",
signature: "gnoga.server.migration",
enclosing: "gnoga.server",
is_private: false,
documentation: "Migrations are used to manage the evolution of a database schema\neach change to the base schema should be coded as an Add_Migration_Up\nfor the change needed for the schema and as an Add_Migration_Down\nfor how the change would be backed out.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Migration_Collection",
       qualified_name: "Gnoga.Server.Migration.Migration_Collection",
       signature: "gnoga.server.migration.migration_collection",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Migration_Collection is tagged limited private;",
       }   ,
   ]
,}
---
