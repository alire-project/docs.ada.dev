---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Objects.Shaders",
qualified_name: "GL.Objects.Shaders",
signature: "gl.objects.shaders",
enclosing: "gl.objects",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Shader_Type",
       qualified_name: "GL.Objects.Shaders.Shader_Type",
       signature: "gl.objects.shaders.shader_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Shader_Type is (Fragment_Shader, Vertex_Shader, Geometry_Shader,\n                     Tess_Evaluation_Shader, Tess_Control_Shader);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Shader",
       qualified_name: "GL.Objects.Shaders.Shader",
       signature: "gl.objects.shaders.shader",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Shader (Kind : Shader_Type) is new GL_Object with private;",
       }   ,
   ]
,}
---
