---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Drawing.Predrawer",
qualified_name: "Agpl.Drawing.Predrawer",
signature: "agpl.drawing.predrawer",
enclosing: "agpl.drawing",
is_private: false,
documentation: "A helper drawable to perform some preliminary actions on a drawable.\nE.g. change color",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Object",
       qualified_name: "Agpl.Drawing.Predrawer.Object",
       signature: "agpl.drawing.predrawer.object",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Object (Prepare :                 Prepare_Procedure;\n             Target  : access constant Drawable'Class)\n  is new Drawable with null record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Prepare_Procedure",
       qualified_name: "Agpl.Drawing.Predrawer.Prepare_Procedure",
       signature: "agpl.drawing.predrawer.prepare_procedure",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Prepare_Procedure is access procedure (Dest   : in out Drawer'Class;\n                                            Target :        Drawable'Class);",
       }   ,
   ]
,}
---
