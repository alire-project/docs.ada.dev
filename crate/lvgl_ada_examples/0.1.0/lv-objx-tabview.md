---
crate: lvgl_ada_examples
layout: gnatdoc
gnatdoc: {
name: "Lv.Objx.Tabview",
qualified_name: "Lv.Objx.Tabview",
signature: "lv.objx.tabview",
enclosing: "lv.objx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Btns_Pos_T",
       qualified_name: "Lv.Objx.Tabview.Btns_Pos_T",
       signature: "lv.objx.tabview.btns_pos_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Btns_Pos_T is (Pos_Top, Pos_Bottom);",
       }   ,
       {
       name: "Style_T",
       qualified_name: "Lv.Objx.Tabview.Style_T",
       signature: "lv.objx.tabview.style_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_T is\n  (Style_Bg,\n   Style_Indic,\n   Style_Btn_Bg,\n   Style_Btn_Rel,\n   Style_Btn_Pr,\n   Style_Btn_Tgl_Rel,\n   Style_Btn_Tgl_Pr);",
       }   ,
   ]
,access_types:    [
       {
       name: "Action_T",
       qualified_name: "Lv.Objx.Tabview.Action_T",
       signature: "lv.objx.tabview.action_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_T is access function\n  (Self   : access Instance;\n   Tab_Id : Uint16_T) return Res_T;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Instance",
       qualified_name: "Lv.Objx.Tabview.Instance",
       signature: "lv.objx.tabview.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Obj_T;",
       }   ,
   ]
,}
---
