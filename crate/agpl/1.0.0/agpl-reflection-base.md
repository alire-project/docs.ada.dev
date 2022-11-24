---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Base",
qualified_name: "Agpl.Reflection.Base",
signature: "agpl.reflection.base",
enclosing: "agpl.reflection",
is_private: false,
documentation: "These types are thread safe by default... protected and heavyweight.\n\n@formal Basetype\n@formal Value\n@formal Image",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Reflection.Base.Object",
       signature: "agpl.reflection.base.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Name  : Name_Access) is limited\nnew Ada.Finalization.Limited_Controlled\n  and Datum with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Name_Access",
       qualified_name: "Agpl.Reflection.Base.Name_Access",
       signature: "agpl.reflection.base.name_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Name_Access is access String;",
       }   ,
   ]
,}
---
