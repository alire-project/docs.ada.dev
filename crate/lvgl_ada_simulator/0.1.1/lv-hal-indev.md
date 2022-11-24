---
crate: lvgl_ada_simulator
layout: gnatdoc
gnatdoc: {
name: "Lv.Hal.Indev",
qualified_name: "Lv.Hal.Indev",
signature: "lv.hal.indev",
enclosing: "lv.hal",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Indev_State_T",
       qualified_name: "Lv.Hal.Indev.Indev_State_T",
       signature: "lv.hal.indev.indev_state_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_State_T is (State_Rel, State_Pr);",
       }   ,
       {
       name: "Indev_T",
       qualified_name: "Lv.Hal.Indev.Indev_T",
       signature: "lv.hal.indev.indev_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_T is private;",
       }   ,
       {
       name: "Indev_Type_T",
       qualified_name: "Lv.Hal.Indev.Indev_Type_T",
       signature: "lv.hal.indev.indev_type_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_Type_T is (Type_None,\n                      Type_Pointer,\n                      Type_Keypad,\n                      Type_Button,\n                      Type_Encoder);",
       }   ,
   ]
,record_types:    [
       {
       name: "Indev_Data_T",
       qualified_name: "Lv.Hal.Indev.Indev_Data_T",
       signature: "lv.hal.indev.indev_data_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_Data_T is record\n   Union     : aliased Indev_Data_T_Union;\n   User_Data : System.Address;\n   State     : aliased Indev_State_T;\nend record;",
       }   ,
       {
       name: "Indev_Data_T_Union",
       qualified_name: "Lv.Hal.Indev.Indev_Data_T_Union",
       signature: "lv.hal.indev.indev_data_t_union",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_Data_T_Union (Discr : unsigned := 0) is record\n   case Discr is\n      when 0 =>\n         Point : aliased Lv.Area.Point_T;\n      when 1 =>\n         Key : aliased Uint32_T;\n      when 2 =>\n         Btn : aliased Uint32_T;\n      when others =>\n         Enc_Diff : aliased Int16_T;\n   end case;\nend record;",
       }   ,
       {
       name: "Indev_Drv_T",
       qualified_name: "Lv.Hal.Indev.Indev_Drv_T",
       signature: "lv.hal.indev.indev_drv_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Indev_Drv_T is record\n   C_Type    : aliased Indev_Type_T;\n   Read      : access function (Data : access Indev_Data_T) return U_Bool;\n   User_Data : System.Address;\nend record;",
       }   ,
   ]
,}
---
