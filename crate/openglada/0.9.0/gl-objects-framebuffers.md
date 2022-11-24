---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Objects.Framebuffers",
qualified_name: "GL.Objects.Framebuffers",
signature: "gl.objects.framebuffers",
enclosing: "gl.objects",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Attachment_Point",
       qualified_name: "GL.Objects.Framebuffers.Attachment_Point",
       signature: "gl.objects.framebuffers.attachment_point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attachment_Point is (Depth_Stencil_Attachment,\n                          Color_Attachment_0, Color_Attachment_1,\n                          Color_Attachment_2, Color_Attachment_3,\n                          Color_Attachment_4, Color_Attachment_5,\n                          Color_Attachment_6, Color_Attachment_7,\n                          Color_Attachment_8, Color_Attachment_9,\n                          Color_Attachment_10, Color_Attachment_11,\n                          Color_Attachment_12, Color_Attachment_13,\n                          Color_Attachment_14, Color_Attachment_15,\n                          Depth_Attachment, Stencil_Attachment);",
       }   ,
       {
       name: "Framebuffer_Status",
       qualified_name: "GL.Objects.Framebuffers.Framebuffer_Status",
       signature: "gl.objects.framebuffers.framebuffer_status",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Framebuffer_Status is (Undefined, Complete, Incomplete_Attachment,\n                            Incomplete_Missing_Attachment,\n                            Incomplete_Draw_Buffer, Incomplete_Read_Buffer,\n                            Unsupported, Incomplete_Multisample,\n                            Incomplete_Layer_Targets);",
       }   ,
   ]
,array_types:    [
       {
       name: "Attachment_List",
       qualified_name: "GL.Objects.Framebuffers.Attachment_List",
       signature: "gl.objects.framebuffers.attachment_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Attachment_List is array (Positive range <>) of Attachment_Point;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Framebuffer",
       qualified_name: "GL.Objects.Framebuffers.Framebuffer",
       signature: "gl.objects.framebuffers.framebuffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Framebuffer is new GL_Object with private;",
       }   ,
       {
       name: "Framebuffer_Target",
       qualified_name: "GL.Objects.Framebuffers.Framebuffer_Target",
       signature: "gl.objects.framebuffers.framebuffer_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Framebuffer_Target (<>) is tagged limited private;",
       }   ,
   ]
,constants:    [
       {
       name: "Default_Framebuffer",
       qualified_name: "GL.Objects.Framebuffers.Default_Framebuffer",
       signature: "gl.objects.framebuffers.default_framebuffer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_Framebuffer : constant Framebuffer;",
       }   ,
       {
       name: "Draw_Target",
       qualified_name: "GL.Objects.Framebuffers.Draw_Target",
       signature: "gl.objects.framebuffers.draw_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Draw_Target : constant Framebuffer_Target;",
       }   ,
       {
       name: "Read_And_Draw_Target",
       qualified_name: "GL.Objects.Framebuffers.Read_And_Draw_Target",
       signature: "gl.objects.framebuffers.read_and_draw_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Read_And_Draw_Target : constant Framebuffer_Target;",
       }   ,
       {
       name: "Read_Target",
       qualified_name: "GL.Objects.Framebuffers.Read_Target",
       signature: "gl.objects.framebuffers.read_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Read_Target  : constant Framebuffer_Target;",
       }   ,
   ]
,}
---
