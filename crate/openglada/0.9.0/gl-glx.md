---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.GLX",
qualified_name: "GL.GLX",
signature: "gl.glx",
enclosing: "gl",
is_private: false,
documentation: "needed types from Xlib",
documentation_snippet: "",
simple_types:    [
       {
       name: "Display_Pointer",
       qualified_name: "GL.GLX.Display_Pointer",
       signature: "gl.glx.display_pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Display_Pointer is new System.Address;",
       }   ,
       {
       name: "GLX_Context",
       qualified_name: "GL.GLX.GLX_Context",
       signature: "gl.glx.glx_context",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GLX_Context is new System.Address;",
       }   ,
       {
       name: "GLX_Drawable",
       qualified_name: "GL.GLX.GLX_Drawable",
       signature: "gl.glx.glx_drawable",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type GLX_Drawable    is new XID;",
       }   ,
       {
       name: "Screen_Depth",
       qualified_name: "GL.GLX.Screen_Depth",
       signature: "gl.glx.screen_depth",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Screen_Depth    is new Natural;",
       }   ,
       {
       name: "Screen_Number",
       qualified_name: "GL.GLX.Screen_Number",
       signature: "gl.glx.screen_number",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Screen_Number   is new Natural;",
       }   ,
       {
       name: "Visual_ID",
       qualified_name: "GL.GLX.Visual_ID",
       signature: "gl.glx.visual_id",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Visual_ID       is new XID;",
       }   ,
       {
       name: "XID",
       qualified_name: "GL.GLX.XID",
       signature: "gl.glx.xid",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type XID is new Interfaces.C.unsigned_long;",
       }   ,
   ]
,record_types:    [
       {
       name: "X_Visual_Info",
       qualified_name: "GL.GLX.X_Visual_Info",
       signature: "gl.glx.x_visual_info",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type X_Visual_Info is record\n   Visual        : System.Address;\n   Visual_Ident  : Visual_ID;\n   Screen        : Screen_Number;\n   Depth         : Screen_Depth;\n   Class         : Integer;\n   Red_Mask      : Long_Integer;\n   Green_Mask    : Long_Integer;\n   Blue_Mask     : Long_Integer;\n   Colormap_Size : Natural;\n   Bits_Per_RGB  : Natural;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "X_Visual_Info_Pointer",
       qualified_name: "GL.GLX.X_Visual_Info_Pointer",
       signature: "gl.glx.x_visual_info_pointer",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type X_Visual_Info_Pointer is access all X_Visual_Info;",
       }   ,
   ]
,}
---
