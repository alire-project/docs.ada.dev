---
crate: rp2040_hal
layout: gnatdoc
gnatdoc: {
name: "RP.Interpolator",
qualified_name: "RP.Interpolator",
signature: "rp.interpolator",
enclosing: "rp",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Lane",
       qualified_name: "RP.Interpolator.Lane",
       signature: "rp.interpolator.lane",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lane is range 0 .. 2;",
       }   ,
   ]
,array_types:    [
       {
       name: "ACCUM_Register",
       qualified_name: "RP.Interpolator.ACCUM_Register",
       signature: "rp.interpolator.accum_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ACCUM_Register  is array (Lane range 0 .. 1) of UInt32;",
       }   ,
       {
       name: "ADD_Register",
       qualified_name: "RP.Interpolator.ADD_Register",
       signature: "rp.interpolator.add_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type ADD_Register    is array (Lane range 0 .. 1) of UInt24\n   with Component_Size => 32;",
       }   ,
       {
       name: "CTRL_Register",
       qualified_name: "RP.Interpolator.CTRL_Register",
       signature: "rp.interpolator.ctrl_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type CTRL_Register   is array (Lane range 0 .. 1) of Lane_Config;",
       }   ,
       {
       name: "LANE_Register",
       qualified_name: "RP.Interpolator.LANE_Register",
       signature: "rp.interpolator.lane_register",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type LANE_Register   is array (Lane) of UInt32;",
       }   ,
   ]
,record_types:    [
       {
       name: "INTERP_Peripheral",
       qualified_name: "RP.Interpolator.INTERP_Peripheral",
       signature: "rp.interpolator.interp_peripheral",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type INTERP_Peripheral is record\n   ACCUM       : ACCUM_Register;\n   BASE        : LANE_Register;\n   POP         : LANE_Register;\n   PEEK        : LANE_Register;\n   CTRL        : CTRL_Register;\n   ADD         : ADD_Register;\n   BASE_1AND0  : UInt32;\nend record\n   with Volatile,\n        Size => 512;",
       }   ,
       {
       name: "Lane_Config",
       qualified_name: "RP.Interpolator.Lane_Config",
       signature: "rp.interpolator.lane_config",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Lane_Config is record\n   SHIFT          : UInt5   := 0;\n   MASK_LSB       : UInt5   := 0;\n   MASK_MSB       : UInt5   := 31;\n   SIGNED         : Boolean := False;\n   CROSS_INPUT    : Boolean := False;\n   CROSS_RESULT   : Boolean := False;\n   ADD_RAW        : Boolean := False;\n   FORCE_MSB      : UInt2   := 0;\n   BLEND          : Boolean := False;\n   CLAMP          : Boolean := False;\n   OVERF           : Boolean := False;\n   OVERF1          : Boolean := False;\n   OVERF0          : Boolean := False;\nend record\n   with Volatile_Full_Access,\n        Size => 32;",
       }   ,
   ]
,}
---
