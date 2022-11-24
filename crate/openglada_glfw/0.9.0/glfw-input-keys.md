---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Input.Keys",
qualified_name: "Glfw.Input.Keys",
signature: "glfw.input.keys",
enclosing: "glfw.input",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Action",
       qualified_name: "Glfw.Input.Keys.Action",
       signature: "glfw.input.keys.action",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Action is (Release, Press, Repeat);",
       }   ,
       {
       name: "Key",
       qualified_name: "Glfw.Input.Keys.Key",
       signature: "glfw.input.keys.key",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Key is (Unknown,\n             Space,\n             Apostrophe,\n             Comma,\n             Minus,\n             Period,\n             Slash,\n             Key_0,\n             Key_1,\n             Key_2,\n             Key_3,\n             Key_4,\n             Key_5,\n             Key_6,\n             Key_7,\n             Key_8,\n             Key_9,\n             Semicolon,\n             Equal,\n             A,\n             B,\n             C,\n             D,\n             E,\n             F,\n             G,\n             H,\n             I,\n             J,\n             K,\n             L,\n             M,\n             N,\n             O,\n             P,\n             Q,\n             R,\n             S,\n             T,\n             U,\n             V,\n             W,\n             X,\n             Y,\n             Z,\n             Left_Bracket,\n             Backslash,\n             Right_Bracket,\n             Grave_Accent,\n             World_1,\n             World_2,\n             Escape,\n             Enter,\n             Tab,\n             Backspace,\n             Insert,\n             Delete,\n             Right,\n             Left,\n             Down,\n             Up,\n             Page_Up,\n             Page_Down,\n             Home,\n             Key_End,\n             Caps_Lock,\n             Scroll_Lock,\n             Print_Screen,\n             Pause,\n             F1,\n             F2,\n             F3,\n             F4,\n             F5,\n             F6,\n             F7,\n             F8,\n             F9,\n             F10,\n             F11,\n             F12,\n             F13,\n             F14,\n             F15,\n             F16,\n             F17,\n             F18,\n             F19,\n             F20,\n             F21,\n             F22,\n             F23,\n             F24,\n             F25,\n             Numpad_0,\n             Numpad_1,\n             Numpad_2,\n             Numpad_3,\n             Numpad_4,\n             Numpad_5,\n             Numpad_6,\n             Numpad_7,\n             Numpad_8,\n             Numpad_9,\n             Numpad_Decimal,\n             Numpad_Divide,\n             Numpad_Multiply,\n             Numpad_Substract,\n             Numpad_Add,\n             Numpad_Enter,\n             Numpad_Equal,\n             Left_Shift,\n             Left_Control,\n             Left_Alt,\n             Left_Super,\n             Right_Shift,\n             Right_Control,\n             Right_Alt,\n             Right_Super,\n             Menu);",
       }   ,
       {
       name: "Scancode",
       qualified_name: "Glfw.Input.Keys.Scancode",
       signature: "glfw.input.keys.scancode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Scancode is new Interfaces.C.int;",
       }   ,
   ]
,record_types:    [
       {
       name: "Modifiers",
       qualified_name: "Glfw.Input.Keys.Modifiers",
       signature: "glfw.input.keys.modifiers",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Modifiers is record\n   Shift   : Boolean;\n   Control : Boolean;\n   Alt     : Boolean;\n   Super   : Boolean;\nend record;",
       }   ,
   ]
,}
---
