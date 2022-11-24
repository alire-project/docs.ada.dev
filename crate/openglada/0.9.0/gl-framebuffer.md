---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Framebuffer",
qualified_name: "GL.Framebuffer",
signature: "gl.framebuffer",
enclosing: "gl",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Logic_Op",
       qualified_name: "GL.Framebuffer.Logic_Op",
       signature: "gl.framebuffer.logic_op",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Logic_Op is (Clear, And_Op, And_Reverse, Copy, And_Inverted, Noop,\n                  Xor_Op, Or_Op, Nor, Equiv, Invert, Or_Reverse,\n                  Copy_Inverted, Or_Inverted, Nand, Set);",
       }   ,
   ]
,subtypes:    [
       {
       name: "Read_Buffer_Selector",
       qualified_name: "GL.Framebuffer.Read_Buffer_Selector",
       signature: "gl.framebuffer.read_buffer_selector",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Read_Buffer_Selector is Buffers.Color_Buffer_Selector range\n  Buffers.None .. Buffers.Right;",
       }   ,
   ]
,}
---
