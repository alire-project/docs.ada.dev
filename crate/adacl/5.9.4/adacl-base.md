---
crate: adacl
layout: gnatdoc
gnatdoc: {
name: "AdaCL.Base",
qualified_name: "AdaCL.Base",
signature: "adacl.base",
enclosing: "adacl",
is_private: false,
documentation: "\nBase class for all non limited AdaCL classes - which is currently. all\nAdaCL Classes. Limited Objects are so limiting ;-).",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "AdaCL.Base.Object",
       signature: "adacl.base.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is abstract new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Class",
       qualified_name: "AdaCL.Base.Object_Class",
       signature: "adacl.base.object_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Class is access Object'Class;",
       }   ,
   ]
,}
---
