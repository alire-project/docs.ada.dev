---
crate: dynamo
layout: gnatdoc
gnatdoc: {
name: "Gen.Model.List",
qualified_name: "Gen.Model.List",
signature: "gen.model.list",
enclosing: "gen.model",
is_private: false,
documentation: "Compare the two definitions.\n\n@formal T\n@formal T_Access",
documentation_snippet: "",
tagged_types:    [
       {
       name: "List_Definition",
       qualified_name: "Gen.Model.List.List_Definition",
       signature: "gen.model.list.list_definition",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type List_Definition is limited new Util.Beans.Basic.List_Bean with private\n  with Default_Iterator  => Iterate,\n  Iterator_Element  => T_Access,\n  Constant_Indexing => Element_Value;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Cursor",
       qualified_name: "Gen.Model.List.Cursor",
       signature: "gen.model.list.cursor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Cursor is Vectors.Cursor;",
       }   ,
       {
       name: "Vector",
       qualified_name: "Gen.Model.List.Vector",
       signature: "gen.model.list.vector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Vector is Vectors.Vector;",
       }   ,
   ]
,}
---
