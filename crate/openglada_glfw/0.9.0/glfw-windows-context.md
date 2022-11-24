---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Windows.Context",
qualified_name: "Glfw.Windows.Context",
signature: "glfw.windows.context",
enclosing: "glfw.windows",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "API_Kind",
       qualified_name: "Glfw.Windows.Context.API_Kind",
       signature: "glfw.windows.context.api_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type API_Kind is (OpenGL, OpenGL_ES);",
       }   ,
       {
       name: "OpenGL_Profile_Kind",
       qualified_name: "Glfw.Windows.Context.OpenGL_Profile_Kind",
       signature: "glfw.windows.context.opengl_profile_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type OpenGL_Profile_Kind is (System_Default, Core_Profile, Compat_Profile);",
       }   ,
       {
       name: "Robustness_Kind",
       qualified_name: "Glfw.Windows.Context.Robustness_Kind",
       signature: "glfw.windows.context.robustness_kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Robustness_Kind is (No_Robustness, No_Reset_Notification,\n                         Lose_Context_On_Reset);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Swap_Interval",
       qualified_name: "Glfw.Windows.Context.Swap_Interval",
       signature: "glfw.windows.context.swap_interval",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Swap_Interval is Interfaces.C.int;",
       }   ,
   ]
,}
---
