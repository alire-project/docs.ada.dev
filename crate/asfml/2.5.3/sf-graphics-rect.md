---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.Rect",
qualified_name: "Sf.Graphics.Rect",
signature: "sf.graphics.rect",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ sfFloatRect and sfIntRect are utility classes for\n/ manipulating rectangles.\n//////////////////////////////////////////////////////////",
documentation_snippet: "",
record_types:    [
       {
       name: "sfFloatRect",
       qualified_name: "Sf.Graphics.Rect.sfFloatRect",
       signature: "sf.graphics.rect.sffloatrect",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfFloatRect is record\n   left   : aliased Float;\n   top    : aliased Float;\n   width  : aliased Float;\n   height : aliased Float;\nend record;",
       }   ,
       {
       name: "sfIntRect",
       qualified_name: "Sf.Graphics.Rect.sfIntRect",
       signature: "sf.graphics.rect.sfintrect",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfIntRect is record\n   left   : aliased Integer;\n   top    : aliased Integer;\n   width  : aliased Integer;\n   height : aliased Integer;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "sfNullRectangle",
       qualified_name: "Sf.Graphics.Rect.sfNullRectangle",
       signature: "sf.graphics.rect.sfnullrectangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfNullRectangle : aliased constant sfIntRect;",
       }   ,
   ]
,}
---
