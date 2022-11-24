---
crate: lvgl_ada_simulator
layout: gnatdoc
gnatdoc: {
name: "Lv.Objx.Label",
qualified_name: "Lv.Objx.Label",
signature: "lv.objx.label",
enclosing: "lv.objx",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Align_T",
       qualified_name: "Lv.Objx.Label.Align_T",
       signature: "lv.objx.label.align_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Align_T is (Align_Left, Align_Center, Align_Right);",
       }   ,
       {
       name: "Long_Mode_T",
       qualified_name: "Lv.Objx.Label.Long_Mode_T",
       signature: "lv.objx.label.long_mode_t",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Long_Expand\n  Expand the object size to the text size\n@enum Long_Break\n  Keep the object width, break the too long lines and expand the object height\n@enum Long_Scroll\n  Expand the object size and scroll the text on the parent (move the label object)\n@enum Long_Dot\n  Keep the size and write dots at the end if the text is too long\n@enum Long_Roll\n  Keep the size and roll the text infinitely\n@enum Long_Crop\n  Keep the size and crop the text out of it",
       documentation_snippet: "type Long_Mode_T is (Long_Expand,\n                     Long_Break,\n                     Long_Scroll,\n                     Long_Dot,\n                     Long_Roll,\n                     Long_Crop);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Instance",
       qualified_name: "Lv.Objx.Label.Instance",
       signature: "lv.objx.label.instance",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Instance is Obj_T;",
       }   ,
   ]
,constants:    [
       {
       name: "Lv_Label_Dot_Num",
       qualified_name: "Lv.Objx.Label.Lv_Label_Dot_Num",
       signature: "lv.objx.label.lv_label_dot_num",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lv_Label_Dot_Num  : constant := 3;",
       }   ,
       {
       name: "Lv_Label_Pos_Last",
       qualified_name: "Lv.Objx.Label.Lv_Label_Pos_Last",
       signature: "lv.objx.label.lv_label_pos_last",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Lv_Label_Pos_Last : constant := 16#FFFF#;",
       }   ,
   ]
,}
---
