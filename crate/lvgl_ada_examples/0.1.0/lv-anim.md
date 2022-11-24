---
crate: lvgl_ada_examples
layout: gnatdoc
gnatdoc: {
name: "Lv.Anim",
qualified_name: "Lv.Anim",
signature: "lv.anim",
enclosing: "lv",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "U_Lv_Anim_T",
       qualified_name: "Lv.Anim.U_Lv_Anim_T",
       signature: "lv.anim.u_lv_anim_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type U_Lv_Anim_T is record\n   Var            : System.Address;\n   Fp             : Fp_T;\n   End_Cb         : Cb_T;\n   Path           : Path_T;\n   Start          : aliased Int32_T;\n   C_End          : aliased Int32_T;\n   Time           : aliased Uint16_T;\n   Act_Time       : aliased Int16_T;\n   Playback_Pause : aliased Uint16_T;\n   Repeat_Pause   : aliased Uint16_T;\n   Playback       : Extensions.Unsigned_1;\n   Repeat         : Extensions.Unsigned_1;\n   Playback_Now   : Extensions.Unsigned_1;\n   Has_Run        : Extensions.Unsigned_1;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "Cb_T",
       qualified_name: "Lv.Anim.Cb_T",
       signature: "lv.anim.cb_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cb_T is access procedure (Arg1 : System.Address);",
       }   ,
       {
       name: "Fp_T",
       qualified_name: "Lv.Anim.Fp_T",
       signature: "lv.anim.fp_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Fp_T is access procedure (Arg1 : System.Address; Arg2 : Int32_T);",
       }   ,
       {
       name: "Path_T",
       qualified_name: "Lv.Anim.Path_T",
       signature: "lv.anim.path_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Path_T is access function (Arg1 : System.Address) return Int32_T;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Anim_T",
       qualified_name: "Lv.Anim.Anim_T",
       signature: "lv.anim.anim_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Anim_T is U_Lv_Anim_T;",
       }   ,
   ]
,}
---
