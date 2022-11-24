---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Events.Joysticks.Game_Controllers",
qualified_name: "SDL.Events.Joysticks.Game_Controllers",
signature: "sdl.events.joysticks.game_controllers",
enclosing: "sdl.events.joysticks",
is_private: false,
documentation: "------------------------------------------------------------------------------------------------------------------\n  Copyright (c) 2013-2020, Luke A. Guest\n\n  This software is provided 'as-is', without any express or implied\n  warranty. In no event will the authors be held liable for any damages\n  arising from the use of this software.\n\n  Permission is granted to anyone to use this software for any purpose,\n  including commercial applications, and to alter it and redistribute it\n  freely, subject to the following restrictions:\n\n     1. The origin of this software must not be misrepresented; you must not\n     claim that you wrote the original software. If you use this software\n     in a product, an acknowledgment in the product documentation would be\n     appreciated but is not required.\n\n     2. Altered source versions must be plainly marked as such, and must not be\n     misrepresented as being the original software.\n\n     3. This notice may not be removed or altered from any source\n     distribution.\n------------------------------------------------------------------------------------------------------------------\n  SDL.Events.Joysticks.Game_Controllers\n\n  Game controller specific events.\n------------------------------------------------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Axes",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.Axes",
       signature: "sdl.events.joysticks.game_controllers.axes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axes is (Invalid,\n              Left_X,\n              Left_Y,\n              Right_X,\n              Right_Y,\n              Trigger_Left,\n              Trigger_Right) with\n  Convention => C;",
       }   ,
       {
       name: "Buttons",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.Buttons",
       signature: "sdl.events.joysticks.game_controllers.buttons",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buttons is (Invalid,\n                 A,\n                 B,\n                 X,\n                 Y,\n                 Back,\n                 Guide,\n                 Start,\n                 Left_Stick,\n                 Right_Stick,\n                 Left_Shoulder,\n                 Right_Shoulder,\n                 D_Pad_Up,\n                 D_Pad_Down,\n                 D_Pad_Left,\n                 D_Pad_Right) with\n  Convention => C;",
       }   ,
       {
       name: "LR_Axes_Values",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.LR_Axes_Values",
       signature: "sdl.events.joysticks.game_controllers.lr_axes_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type LR_Axes_Values is range -32768 .. 32767 with\n  Convention => C,\n  Size       => 16;",
       }   ,
       {
       name: "Trigger_Axes_Values",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.Trigger_Axes_Values",
       signature: "sdl.events.joysticks.game_controllers.trigger_axes_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Trigger_Axes_Values is range 0 .. 32767 with\n  Convention => C,\n  Size       => 16;",
       }   ,
   ]
,subtypes:    [
       {
       name: "LR_Axes",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.LR_Axes",
       signature: "sdl.events.joysticks.game_controllers.lr_axes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype LR_Axes      is Axes range Left_X .. Right_Y;",
       }   ,
       {
       name: "Trigger_Axes",
       qualified_name: "SDL.Events.Joysticks.Game_Controllers.Trigger_Axes",
       signature: "sdl.events.joysticks.game_controllers.trigger_axes",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Trigger_Axes is Axes range Trigger_Left .. Trigger_Right;",
       }   ,
   ]
,}
---
