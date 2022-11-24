---
crate: openglada_glfw
layout: gnatdoc
gnatdoc: {
name: "Glfw.Errors",
qualified_name: "Glfw.Errors",
signature: "glfw.errors",
enclosing: "glfw",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Kind",
       qualified_name: "Glfw.Errors.Kind",
       signature: "glfw.errors.kind",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Kind is (Not_Initialized,\n              No_Current_Context,\n              Invalid_Enum,\n              Invalid_Value,\n              Out_Of_Memory,\n              API_Unavailable,\n              Version_Unavailable,\n              Platform_Error,\n              Format_Unavailable);",
       }   ,
   ]
,access_types:    [
       {
       name: "Callback",
       qualified_name: "Glfw.Errors.Callback",
       signature: "glfw.errors.callback",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Callback is access procedure (Error : Kind; Description : String);",
       }   ,
   ]
,}
---
