---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Input.Mouse",
qualified_name: "Glfw.Input.Mouse",
signature: "glfw.input.mouse",
enclosing: "glfw.input",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Button",
       qualified_name: "Glfw.Input.Mouse.Button",
       signature: "glfw.input.mouse.button",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Button is new Interfaces.C.int range 0 .. 7;",
       }   ,
       {
       name: "Cursor_Mode",
       qualified_name: "Glfw.Input.Mouse.Cursor_Mode",
       signature: "glfw.input.mouse.cursor_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Cursor_Mode is (Normal, Hidden, Disabled);",
       }   ,
       {
       name: "Enter_Action",
       qualified_name: "Glfw.Input.Mouse.Enter_Action",
       signature: "glfw.input.mouse.enter_action",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Enter_Action is (Leaving, Entering);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Coordinate",
       qualified_name: "Glfw.Input.Mouse.Coordinate",
       signature: "glfw.input.mouse.coordinate",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Coordinate is Interfaces.C.double;",
       }   ,
       {
       name: "Scroll_Offset",
       qualified_name: "Glfw.Input.Mouse.Scroll_Offset",
       signature: "glfw.input.mouse.scroll_offset",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Scroll_Offset is Interfaces.C.double;",
       }   ,
   ]
,constants:    [
       {
       name: "Left_Button",
       qualified_name: "Glfw.Input.Mouse.Left_Button",
       signature: "glfw.input.mouse.left_button",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Left_Button   : constant := 0;",
       }   ,
       {
       name: "Middle_Button",
       qualified_name: "Glfw.Input.Mouse.Middle_Button",
       signature: "glfw.input.mouse.middle_button",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Middle_Button : constant := 2;",
       }   ,
       {
       name: "Right_Button",
       qualified_name: "Glfw.Input.Mouse.Right_Button",
       signature: "glfw.input.mouse.right_button",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Right_Button  : constant := 1;",
       }   ,
   ]
,}
---
