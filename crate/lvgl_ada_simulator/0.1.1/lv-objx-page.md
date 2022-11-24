---
crate: lvgl_ada_simulator
layout: gnatdoc
gnatdoc: {
name: "Lv.Objx.Page",
qualified_name: "Lv.Objx.Page",
signature: "lv.objx.page",
enclosing: "lv.objx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Mode_T",
       qualified_name: "Lv.Objx.Page.Mode_T",
       signature: "lv.objx.page.mode_t",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Sb_Mode_Off\n  Never show scrollbars\n@enum Sb_Mode_On\n  Always show scrollbars\n@enum Sb_Mode_Drag\n  Show scrollbars when page is being dragged\n@enum Sb_Mode_Auto\n  Show scrollbars when the scrollable container is large enough to be scrolled\n@enum Sb_Mode_Hide\n  Hide the scroll bar temporally\n@enum Sb_Mode_Unhide\n  Unhide the previously hidden scrollbar. Recover it's type too",
       documentation_snippet: "type Mode_T is\n  (Sb_Mode_Off,\n   Sb_Mode_On,\n   Sb_Mode_Drag,\n   Sb_Mode_Auto,\n   Sb_Mode_Hide,\n   Sb_Mode_Unhide);",
       }   ,
       {
       name: "Style_T",
       qualified_name: "Lv.Objx.Page.Style_T",
       signature: "lv.objx.page.style_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_T is (Style_Bg,\n                 Style_Scrl,\n                 Style_Sb);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Instance",
       qualified_name: "Lv.Objx.Page.Instance",
       signature: "lv.objx.page.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Obj_T;",
       }   ,
   ]
,}
---
