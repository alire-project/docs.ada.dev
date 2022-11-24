---
crate: hal
layout: gnatdoc
gnatdoc: {
name: "HAL.Touch_Panel",
qualified_name: "HAL.Touch_Panel",
signature: "hal.touch_panel",
enclosing: "hal",
is_private: false,
documentation: "----------------------------------------------------------------------------\n                                                                          --\n                     Copyright (C) 2015-2016, AdaCore                     --\n                                                                          --\n  Redistribution and use in source and binary forms, with or without      --\n  modification, are permitted provided that the following conditions are  --\n  met:                                                                    --\n     1. Redistributions of source code must retain the above copyright    --\n        notice, this list of conditions and the following disclaimer.     --\n     2. Redistributions in binary form must reproduce the above copyright --\n        notice, this list of conditions and the following disclaimer in   --\n        the documentation and/or other materials provided with the        --\n        distribution.                                                     --\n     3. Neither the name of the copyright holder nor the names of its     --\n        contributors may be used to endorse or promote products derived   --\n        from this software without specific prior written permission.     --\n                                                                          --\n   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    --\n   \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      --\n   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  --\n   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT   --\n   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, --\n   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT       --\n   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  --\n   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  --\n   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT    --\n   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  --\n   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   --\n                                                                          --\n----------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Swap_State",
       qualified_name: "HAL.Touch_Panel.Swap_State",
       signature: "hal.touch_panel.swap_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Swap_State is new UInt3;",
       }   ,
   ]
,array_types:    [
       {
       name: "TP_State",
       qualified_name: "HAL.Touch_Panel.TP_State",
       signature: "hal.touch_panel.tp_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TP_State is array (Touch_Identifier range <>) of TP_Touch_State;",
       }   ,
   ]
,record_types:    [
       {
       name: "TP_Touch_State",
       qualified_name: "HAL.Touch_Panel.TP_Touch_State",
       signature: "hal.touch_panel.tp_touch_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type TP_Touch_State is record\n   X      : Natural;\n   Y      : Natural;\n   Weight : Natural;\nend record;",
       }   ,
   ]
,interface_types:    [
       {
       name: "Touch_Panel_Device",
       qualified_name: "HAL.Touch_Panel.Touch_Panel_Device",
       signature: "hal.touch_panel.touch_panel_device",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Touch_Panel_Device is limited interface;",
       }   ,
   ]
,access_types:    [
       {
       name: "Any_Touch_Panel",
       qualified_name: "HAL.Touch_Panel.Any_Touch_Panel",
       signature: "hal.touch_panel.any_touch_panel",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Any_Touch_Panel is access all Touch_Panel_Device'Class;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Touch_Identifier",
       qualified_name: "HAL.Touch_Panel.Touch_Identifier",
       signature: "hal.touch_panel.touch_identifier",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Touch_Identifier is Natural range 0 .. 10;",
       }   ,
   ]
,constants:    [
       {
       name: "Invert_X",
       qualified_name: "HAL.Touch_Panel.Invert_X",
       signature: "hal.touch_panel.invert_x",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invert_X : constant Swap_State;",
       }   ,
       {
       name: "Invert_Y",
       qualified_name: "HAL.Touch_Panel.Invert_Y",
       signature: "hal.touch_panel.invert_y",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invert_Y : constant Swap_State;",
       }   ,
       {
       name: "Null_Touch_State",
       qualified_name: "HAL.Touch_Panel.Null_Touch_State",
       signature: "hal.touch_panel.null_touch_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Touch_State : constant TP_Touch_State := (0, 0, 0);",
       }   ,
       {
       name: "Swap_XY",
       qualified_name: "HAL.Touch_Panel.Swap_XY",
       signature: "hal.touch_panel.swap_xy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Swap_XY  : constant Swap_State;",
       }   ,
   ]
,}
---
