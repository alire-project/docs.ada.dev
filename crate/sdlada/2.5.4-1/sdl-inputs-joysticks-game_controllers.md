---
crate: sdlada
layout: gnatdoc
gnatdoc: {
name: "SDL.Inputs.Joysticks.Game_Controllers",
qualified_name: "SDL.Inputs.Joysticks.Game_Controllers",
signature: "sdl.inputs.joysticks.game_controllers",
enclosing: "sdl.inputs.joysticks",
is_private: false,
documentation: "",
documentation_snippet: "",
simple_types:    [
       {
       name: "Bind_Types",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Bind_Types",
       signature: "sdl.inputs.joysticks.game_controllers.bind_types",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bind_Types is (None, Button, Axis, Hat) with\n  Convention => C;",
       }   ,
   ]
,record_types:    [
       {
       name: "Binding_Values",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Binding_Values",
       signature: "sdl.inputs.joysticks.game_controllers.binding_values",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Binding_Values (Which : Bind_Types := None) is\n   record\n      case Which is\n         when None =>\n            null;\n         when Button =>\n            Button : SDL.Events.Joysticks.Game_Controllers.Buttons;\n         when Axis =>\n            Axis   : SDL.Events.Joysticks.Game_Controllers.Axes;\n         when Hat =>\n            Hat    : Hat_Bindings;\n      end case;\n   end record with\n     Unchecked_Union;",
       }   ,
       {
       name: "Bindings",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Bindings",
       signature: "sdl.inputs.joysticks.game_controllers.bindings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bindings is\n   record\n      Which : Bind_Types;\n      Value : Binding_Values (None);\n   end record with\n     Convention => C;",
       }   ,
       {
       name: "Hat_Bindings",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Hat_Bindings",
       signature: "sdl.inputs.joysticks.game_controllers.hat_bindings",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Hat_Bindings is\n   record\n      Hat  : SDL.Events.Joysticks.Hats;\n      Mask : SDL.Events.Joysticks.Hat_Positions;\n   end record with\n     Convention => C;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Game_Controller",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Game_Controller",
       signature: "sdl.inputs.joysticks.game_controllers.game_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Game_Controller is new Ada.Finalization.Limited_Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Null_Game_Controller",
       qualified_name: "SDL.Inputs.Joysticks.Game_Controllers.Null_Game_Controller",
       signature: "sdl.inputs.joysticks.game_controllers.null_game_controller",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Game_Controller : constant Game_Controller;",
       }   ,
   ]
,}
---
