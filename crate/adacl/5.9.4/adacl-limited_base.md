---
crate: adacl
layout: gnatdoc
gnatdoc: {
name: "AdaCL.Limited_Base",
qualified_name: "AdaCL.Limited_Base",
signature: "adacl.limited_base",
enclosing: "adacl",
is_private: false,
documentation: "\nBase Class for Limited Object. In AdaCL great care is taken to make all\nclasses non limited so this base class is not actualy used yet.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "AdaCL.Limited_Base.Object",
       signature: "adacl.limited_base.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object is abstract new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Object_Class",
       qualified_name: "AdaCL.Limited_Base.Object_Class",
       signature: "adacl.limited_base.object_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object_Class is access Object'Class;",
       }   ,
   ]
,}
---
