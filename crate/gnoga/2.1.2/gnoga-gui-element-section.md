---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Element.Section",
qualified_name: "Gnoga.Gui.Element.Section",
signature: "gnoga.gui.element.section",
enclosing: "gnoga.gui.element",
is_private: false,
documentation: "Section_Type is a View that describes a semantic section.\nPractically there is no difference with View_Type other than\ntheir underlying tag for styling purposes. Some sections\nhave some default styling, e.g. as address being italic.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Section_Description_Type",
       qualified_name: "Gnoga.Gui.Element.Section.Section_Description_Type",
       signature: "gnoga.gui.element.section.section_description_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Section_Description_Type is\n  (Address, Article, Aside, Header, Main, Nav, P, Pre, Section, BlockQuote, H1, H2, H3, H4, H5, H6, HGroup);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Section_Type",
       qualified_name: "Gnoga.Gui.Element.Section.Section_Type",
       signature: "gnoga.gui.element.section.section_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Section_Type is new Gnoga.Gui.View.View_Base_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer_To_Section_Class",
       qualified_name: "Gnoga.Gui.Element.Section.Pointer_To_Section_Class",
       signature: "gnoga.gui.element.section.pointer_to_section_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Section_Class is access all Section_Type'Class;",
       }   ,
       {
       name: "Section_Access",
       qualified_name: "Gnoga.Gui.Element.Section.Section_Access",
       signature: "gnoga.gui.element.section.section_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Section_Access is access all Section_Type;",
       }   ,
   ]
,}
---
