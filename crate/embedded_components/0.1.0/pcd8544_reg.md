---
crate: embedded_components
layout: gnatdoc
gnatdoc: {
name: "PCD8544_Reg",
qualified_name: "PCD8544_Reg",
signature: "pcd8544_reg",
enclosing: "",
is_private: false,
documentation: "Basic mode",
documentation_snippet: "",
simple_types:    [
       {
       name: "PCD8544_Address_Mode",
       qualified_name: "PCD8544_Reg.PCD8544_Address_Mode",
       signature: "pcd8544_reg.pcd8544_address_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PCD8544_Address_Mode is (Horizontal, Vertical);",
       }   ,
   ]
,record_types:    [
       {
       name: "PCD8544_Display_Register",
       qualified_name: "PCD8544_Reg.PCD8544_Display_Register",
       signature: "pcd8544_reg.pcd8544_display_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PCD8544_Display_Register is record\n   Enable    : Boolean := False;\n   Invert    : Boolean := False;\n   Reserved1 : Boolean := False;\n   Reserved2 : Boolean := False;\nend record;",
       }   ,
       {
       name: "PCD8544_Function_Register",
       qualified_name: "PCD8544_Reg.PCD8544_Function_Register",
       signature: "pcd8544_reg.pcd8544_function_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PCD8544_Function_Register is record\n   Power_Down    : Boolean              := True;\n   Address_Mode  : PCD8544_Address_Mode := Horizontal;\n   Extended_Mode : Boolean              := False;\n   Reserved      : Boolean              := False;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "PCD8544_CMD_DISPLAY",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_DISPLAY",
       signature: "pcd8544_reg.pcd8544_cmd_display",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_DISPLAY  : constant := 2#0000_1000#;",
       }   ,
       {
       name: "PCD8544_CMD_FUNCTION",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_FUNCTION",
       signature: "pcd8544_reg.pcd8544_cmd_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_FUNCTION : constant := 2#0010_0000#;",
       }   ,
       {
       name: "PCD8544_CMD_SET_BIAS",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_SET_BIAS",
       signature: "pcd8544_reg.pcd8544_cmd_set_bias",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_SET_BIAS : constant := 2#0001_0000#;",
       }   ,
       {
       name: "PCD8544_CMD_SET_TC",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_SET_TC",
       signature: "pcd8544_reg.pcd8544_cmd_set_tc",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_SET_TC   : constant := 2#0000_0100#;",
       }   ,
       {
       name: "PCD8544_CMD_SET_VOP",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_SET_VOP",
       signature: "pcd8544_reg.pcd8544_cmd_set_vop",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_SET_VOP  : constant := 2#1000_0000#;",
       }   ,
       {
       name: "PCD8544_CMD_SET_X",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_SET_X",
       signature: "pcd8544_reg.pcd8544_cmd_set_x",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_SET_X    : constant := 2#1000_0000#;",
       }   ,
       {
       name: "PCD8544_CMD_SET_Y",
       qualified_name: "PCD8544_Reg.PCD8544_CMD_SET_Y",
       signature: "pcd8544_reg.pcd8544_cmd_set_y",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "PCD8544_CMD_SET_Y    : constant := 2#0100_0000#;",
       }   ,
   ]
,}
---
