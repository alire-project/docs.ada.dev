---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Low_Level",
qualified_name: "GL.Low_Level",
signature: "gl.low_level",
enclosing: "gl",
is_private: false,
documentation: "This package contains some low-level types that are used by the raw C\ninterface of the OpenGL API. They are converted to types that are easier\nto handle by the wrapper and thus are not needed for using the wrapper.\nHowever, they might be used by other APIs that use OpenGL and thus are\nexposed publicly here.",
documentation_snippet: "",
simple_types:    [
       {
       name: "Bool",
       qualified_name: "GL.Low_Level.Bool",
       signature: "gl.low_level.bool",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bool is new Boolean;",
       }   ,
   ]
,array_types:    [
       {
       name: "Char_Access_Array",
       qualified_name: "GL.Low_Level.Char_Access_Array",
       signature: "gl.low_level.char_access_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Char_Access_Array is array (Size range <>) of access C.char;",
       }   ,
   ]
,access_types:    [
       {
       name: "Bool_Access",
       qualified_name: "GL.Low_Level.Bool_Access",
       signature: "gl.low_level.bool_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bool_Access is access all Bool;",
       }   ,
       {
       name: "Size_Access",
       qualified_name: "GL.Low_Level.Size_Access",
       signature: "gl.low_level.size_access",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Size_Access is access all Types.Size;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Bitfield",
       qualified_name: "GL.Low_Level.Bitfield",
       signature: "gl.low_level.bitfield",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Bitfield is C.unsigned;",
       }   ,
       {
       name: "Enum",
       qualified_name: "GL.Low_Level.Enum",
       signature: "gl.low_level.enum",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Enum is C.unsigned;",
       }   ,
       {
       name: "IntPtr",
       qualified_name: "GL.Low_Level.IntPtr",
       signature: "gl.low_level.intptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype IntPtr is C.long;",
       }   ,
       {
       name: "SizeIPtr",
       qualified_name: "GL.Low_Level.SizeIPtr",
       signature: "gl.low_level.sizeiptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype SizeIPtr is C.long;",
       }   ,
       {
       name: "Zero",
       qualified_name: "GL.Low_Level.Zero",
       signature: "gl.low_level.zero",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Zero is Int range 0 .. 0;",
       }   ,
   ]
,}
---
