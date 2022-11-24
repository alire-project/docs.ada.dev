---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Reflection",
qualified_name: "Agpl.Reflection",
signature: "agpl.reflection",
enclosing: "agpl",
is_private: false,
documentation: "See child Booleans package for an example of usage...\nNote that accessed values should be at library level...",
documentation_snippet: "",
packages:    [
       {
       name: "Base",
       qualified_name: "Agpl.Reflection.Base",
       signature: "agpl.reflection.base",
       enclosing: "agpl.reflection",
       is_private: false,
       documentation: "These types are thread safe by default... protected and heavyweight.\n\n@formal Basetype\n@formal Value\n@formal Image",
       documentation_snippet: "",
tagged_types:           [
              {
              name: "Object",
              qualified_name: "Agpl.Reflection.Base.Object",
              signature: "agpl.reflection.base.object",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Object (Name  : Name_Access) is limited\nnew Ada.Finalization.Limited_Controlled\n  and Datum with private;",
              }          ,
          ]
,access_types:           [
              {
              name: "Name_Access",
              qualified_name: "Agpl.Reflection.Base.Name_Access",
              signature: "agpl.reflection.base.name_access",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Name_Access is access String;",
              }          ,
          ]
,       }   ,
   ]
,interface_types:    [
       {
       name: "Datum",
       qualified_name: "Agpl.Reflection.Datum",
       signature: "agpl.reflection.datum",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Datum is limited interface;",
       }   ,
   ]
,}
---
