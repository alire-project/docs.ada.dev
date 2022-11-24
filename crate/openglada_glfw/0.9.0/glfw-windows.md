---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Windows",
qualified_name: "Glfw.Windows",
signature: "glfw.windows",
enclosing: "glfw",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
packages:    [
       {
       name: "Callbacks",
       qualified_name: "Glfw.Windows.Callbacks",
       signature: "glfw.windows.callbacks",
       enclosing: "glfw.windows",
       is_private: false,
       documentation: "avoid pollution of Glfw.Windows package with symbols",
       documentation_snippet: "",
simple_types:           [
              {
              name: "Kind",
              qualified_name: "Glfw.Windows.Callbacks.Kind",
              signature: "glfw.windows.callbacks.kind",
              enclosing: "",
              is_private: false,
              documentation: "",
              documentation_snippet: "type Kind is (Position, Size, Close, Refresh, Focus, Iconify,\n              Framebuffer_Size, Mouse_Button, Mouse_Position,\n              Mouse_Scroll, Mouse_Enter, Key, Char);",
              }          ,
          ]
,       }   ,
   ]
,tagged_types:    [
       {
       name: "Window",
       qualified_name: "Glfw.Windows.Window",
       signature: "glfw.windows.window",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Window is tagged private;",
       }   ,
   ]
,access_types:    [
       {
       name: "Window_Reference",
       qualified_name: "Glfw.Windows.Window_Reference",
       signature: "glfw.windows.window_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Window_Reference is not null access all Window;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Coordinate",
       qualified_name: "Glfw.Windows.Coordinate",
       signature: "glfw.windows.coordinate",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Coordinate is Interfaces.C.int;",
       }   ,
   ]
,}
---
