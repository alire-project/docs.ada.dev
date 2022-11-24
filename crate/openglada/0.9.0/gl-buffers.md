---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Buffers",
qualified_name: "GL.Buffers",
signature: "gl.buffers",
enclosing: "gl",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Color_Buffer_Selector",
       qualified_name: "GL.Buffers.Color_Buffer_Selector",
       signature: "gl.buffers.color_buffer_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Buffer_Selector is (None, Front_Left,\n                               Front_Right, Back_Left, Back_Right,\n                               Front, Back, Left, Right, Front_And_Back);",
       }   ,
       {
       name: "Explicit_Color_Buffer_Selector",
       qualified_name: "GL.Buffers.Explicit_Color_Buffer_Selector",
       signature: "gl.buffers.explicit_color_buffer_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Explicit_Color_Buffer_Selector is (None, Front_Left, Front_Right,\n                                        Back_Left, Back_Right,\n                                        Color_Attachment0,\n                                        Color_Attachment1,\n                                        Color_Attachment2,\n                                        Color_Attachment3,\n                                        Color_Attachment4,\n                                        Color_Attachment5,\n                                        Color_Attachment6,\n                                        Color_Attachment7,\n                                        Color_Attachment8,\n                                        Color_Attachment9,\n                                        Color_Attachment10,\n                                        Color_Attachment11,\n                                        Color_Attachment12,\n                                        Color_Attachment13,\n                                        Color_Attachment14,\n                                        Color_Attachment15);",
       }   ,
       {
       name: "Stencil_Action",
       qualified_name: "GL.Buffers.Stencil_Action",
       signature: "gl.buffers.stencil_action",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Stencil_Action is (Zero, Invert, Keep, Replace,\n                        Increment, Decrement,\n                        Increment_Wrap, Decrement_Wrap);",
       }   ,
   ]
,array_types:    [
       {
       name: "Explicit_Color_Buffer_List",
       qualified_name: "GL.Buffers.Explicit_Color_Buffer_List",
       signature: "gl.buffers.explicit_color_buffer_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Explicit_Color_Buffer_List is array (Draw_Buffer_Index range <>)\n  of Explicit_Color_Buffer_Selector;",
       }   ,
   ]
,record_types:    [
       {
       name: "Buffer_Bits",
       qualified_name: "GL.Buffers.Buffer_Bits",
       signature: "gl.buffers.buffer_bits",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer_Bits is record\n   Depth   : Boolean := False;\n   Accum   : Boolean := False;\n   Stencil : Boolean := False;\n   Color   : Boolean := False;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Base_Color_Buffer_Selector",
       qualified_name: "GL.Buffers.Base_Color_Buffer_Selector",
       signature: "gl.buffers.base_color_buffer_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Base_Color_Buffer_Selector is Color_Buffer_Selector\n  range Front .. Front_And_Back;",
       }   ,
       {
       name: "Depth",
       qualified_name: "GL.Buffers.Depth",
       signature: "gl.buffers.depth",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Depth is Double range 0.0 .. 1.0;",
       }   ,
       {
       name: "Draw_Buffer_Index",
       qualified_name: "GL.Buffers.Draw_Buffer_Index",
       signature: "gl.buffers.draw_buffer_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Draw_Buffer_Index is UInt range 0 .. 15;",
       }   ,
       {
       name: "Single_Face_Selector",
       qualified_name: "GL.Buffers.Single_Face_Selector",
       signature: "gl.buffers.single_face_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Single_Face_Selector is Culling.Face_Selector\n  range Culling.Front .. Culling.Back;",
       }   ,
       {
       name: "Stencil_Index",
       qualified_name: "GL.Buffers.Stencil_Index",
       signature: "gl.buffers.stencil_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Stencil_Index is Int;",
       }   ,
   ]
,}
---
