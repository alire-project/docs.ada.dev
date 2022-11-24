---
crate: lvgl_ada_simulator
layout: gnatdoc
gnatdoc: {
name: "Lv.Objx.Btnm",
qualified_name: "Lv.Objx.Btnm",
signature: "lv.objx.btnm",
enclosing: "lv.objx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Style_T",
       qualified_name: "Lv.Objx.Btnm.Style_T",
       signature: "lv.objx.btnm.style_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Style_T is (Style_Bg,\n                 Style_Rel,\n                 Style_Pr,\n                 Style_Tgl_Rel,\n                 Style_Tgl_Pr,\n                 Style_Ina);",
       }   ,
   ]
,access_types:    [
       {
       name: "Action_T",
       qualified_name: "Lv.Objx.Btnm.Action_T",
       signature: "lv.objx.btnm.action_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action_T is access function\n  (Self : Instance;\n   Txt  : Interfaces.C.Strings.chars_ptr) return Res_T;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Instance",
       qualified_name: "Lv.Objx.Btnm.Instance",
       signature: "lv.objx.btnm.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Obj_T;",
       }   ,
   ]
,constants:    [
       {
       name: "Btnm_Ctrl_Code",
       qualified_name: "Lv.Objx.Btnm.Btnm_Ctrl_Code",
       signature: "lv.objx.btnm.btnm_ctrl_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Ctrl_Code           : constant := 16#80#;",
       }   ,
       {
       name: "Btnm_Ctrl_Mask",
       qualified_name: "Lv.Objx.Btnm.Btnm_Ctrl_Mask",
       signature: "lv.objx.btnm.btnm_ctrl_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Ctrl_Mask           : constant := 16#C0#;",
       }   ,
       {
       name: "Btnm_Hide_Mask",
       qualified_name: "Lv.Objx.Btnm.Btnm_Hide_Mask",
       signature: "lv.objx.btnm.btnm_hide_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Hide_Mask           : constant := 16#08#;",
       }   ,
       {
       name: "Btnm_Inactive_Mask",
       qualified_name: "Lv.Objx.Btnm.Btnm_Inactive_Mask",
       signature: "lv.objx.btnm.btnm_inactive_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Inactive_Mask       : constant := 16#20#;",
       }   ,
       {
       name: "Btnm_Pr_None",
       qualified_name: "Lv.Objx.Btnm.Btnm_Pr_None",
       signature: "lv.objx.btnm.btnm_pr_none",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Pr_None             : constant := 16#FFFF#;",
       }   ,
       {
       name: "Btnm_Repeat_Disable_Mask",
       qualified_name: "Lv.Objx.Btnm.Btnm_Repeat_Disable_Mask",
       signature: "lv.objx.btnm.btnm_repeat_disable_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Repeat_Disable_Mask : constant := 16#10#;",
       }   ,
       {
       name: "Btnm_Width_Mask",
       qualified_name: "Lv.Objx.Btnm.Btnm_Width_Mask",
       signature: "lv.objx.btnm.btnm_width_mask",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Btnm_Width_Mask          : constant := 16#07#;",
       }   ,
   ]
,}
---
