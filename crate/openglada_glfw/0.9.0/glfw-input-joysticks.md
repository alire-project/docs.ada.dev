---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Input.Joysticks",
qualified_name: "Glfw.Input.Joysticks",
signature: "glfw.input.joysticks",
enclosing: "glfw.input",
is_private: false,
documentation: "GLFW supports up to 16 joysticks; they are indexed from 1 to 16.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Axis_Position",
       qualified_name: "Glfw.Input.Joysticks.Axis_Position",
       signature: "glfw.input.joysticks.axis_position",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis_Position is new Interfaces.C.C_float range -1.0 .. 1.0;",
       }   ,
       {
       name: "Joystick_Button_State",
       qualified_name: "Glfw.Input.Joysticks.Joystick_Button_State",
       signature: "glfw.input.joysticks.joystick_button_state",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Joystick_Button_State is new Button_State;",
       }   ,
       {
       name: "Joystick_Index",
       qualified_name: "Glfw.Input.Joysticks.Joystick_Index",
       signature: "glfw.input.joysticks.joystick_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Joystick_Index is range 1 .. 16;",
       }   ,
   ]
,array_types:    [
       {
       name: "Axis_Positions",
       qualified_name: "Glfw.Input.Joysticks.Axis_Positions",
       signature: "glfw.input.joysticks.axis_positions",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Axis_Positions is array (Positive range <>) of aliased Axis_Position;",
       }   ,
       {
       name: "Joystick_Button_States",
       qualified_name: "Glfw.Input.Joysticks.Joystick_Button_States",
       signature: "glfw.input.joysticks.joystick_button_states",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Joystick_Button_States is array (Positive range <>) of\n  aliased Joystick_Button_State;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Joystick",
       qualified_name: "Glfw.Input.Joysticks.Joystick",
       signature: "glfw.input.joysticks.joystick",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Joystick is tagged private;",
       }   ,
   ]
,}
---
