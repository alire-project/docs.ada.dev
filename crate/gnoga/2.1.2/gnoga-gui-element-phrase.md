---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Element.Phrase",
qualified_name: "Gnoga.Gui.Element.Phrase",
signature: "gnoga.gui.element.phrase",
enclosing: "gnoga.gui.element",
is_private: false,
documentation: "Phrase_Type is a View that describes an inline phrase section.\nMost of the time it is better to use these with in a Common.Span_Type\nor to style as desired.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Phrase_Description_Type",
       qualified_name: "Gnoga.Gui.Element.Phrase.Phrase_Description_Type",
       signature: "gnoga.gui.element.phrase.phrase_description_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phrase_Description_Type is\n  (Abbr, Code, Strong, Em, Dfn, Samp, Kbd, Var, Marked, Del, Ins, S, Q, Big, Small, Time, Tt, Cite, I, B, U, Sub,\n   Sup);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Phrase_Type",
       qualified_name: "Gnoga.Gui.Element.Phrase.Phrase_Type",
       signature: "gnoga.gui.element.phrase.phrase_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phrase_Type is new Gnoga.Gui.View.View_Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Phrase_Access",
       qualified_name: "Gnoga.Gui.Element.Phrase.Phrase_Access",
       signature: "gnoga.gui.element.phrase.phrase_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Phrase_Access is access all Phrase_Type;",
       }   ,
       {
       name: "Pointer_To_Phrase_Class",
       qualified_name: "Gnoga.Gui.Element.Phrase.Pointer_To_Phrase_Class",
       signature: "gnoga.gui.element.phrase.pointer_to_phrase_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Phrase_Class is access all Phrase_Type'Class;",
       }   ,
   ]
,}
---
