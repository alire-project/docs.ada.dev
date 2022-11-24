---
crate: gnoga
layout: gnatdoc
gnatdoc: {
name: "Gnoga.Gui.Element.Style_Block",
qualified_name: "Gnoga.Gui.Element.Style_Block",
signature: "gnoga.gui.element.style_block",
enclosing: "gnoga.gui.element",
is_private: false,
documentation: "Style elements are for creating CSS styles. In general it is better\nto create CSS style sheets as external files and load with\nWindow_Type.Document.Load_CSS or use element properties. However\nit is possible to generate CSS style sheets in Gnoga. They can be\nadded like any element to views, windows, etc.",
documentation_snippet: "",
tagged_types:    [
       {
       name: "Style_Type",
       qualified_name: "Gnoga.Gui.Element.Style_Block.Style_Type",
       signature: "gnoga.gui.element.style_block.style_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_Type is new Element_Type with private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Pointer_To_Style_Class",
       qualified_name: "Gnoga.Gui.Element.Style_Block.Pointer_To_Style_Class",
       signature: "gnoga.gui.element.style_block.pointer_to_style_class",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Pointer_To_Style_Class is access all Style_Type'Class;",
       }   ,
       {
       name: "Style_Access",
       qualified_name: "Gnoga.Gui.Element.Style_Block.Style_Access",
       signature: "gnoga.gui.element.style_block.style_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_Access is access all Style_Type;",
       }   ,
   ]
,}
---
