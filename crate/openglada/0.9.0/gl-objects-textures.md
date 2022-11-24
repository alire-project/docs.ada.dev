---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Objects.Textures",
qualified_name: "GL.Objects.Textures",
signature: "gl.objects.textures",
enclosing: "gl.objects",
is_private: false,
documentation: "---------------------------------------------------------------------------\n                            Basic Types                                  --\n---------------------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Depth_Mode",
       qualified_name: "GL.Objects.Textures.Depth_Mode",
       signature: "gl.objects.textures.depth_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Depth_Mode is (Alpha, Luminance, Intensity);",
       }   ,
       {
       name: "Image_Source",
       qualified_name: "GL.Objects.Textures.Image_Source",
       signature: "gl.objects.textures.image_source",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Image_Source is new System.Address;",
       }   ,
       {
       name: "Minifying_Function",
       qualified_name: "GL.Objects.Textures.Minifying_Function",
       signature: "gl.objects.textures.minifying_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Minifying_Function is (Nearest, Linear, Nearest_Mipmap_Nearest,\n                            Linear_Mipmap_Nearest, Nearest_Mipmap_Linear,\n                            Linear_Mipmap_Linear);",
       }   ,
       {
       name: "Wrapping_Mode",
       qualified_name: "GL.Objects.Textures.Wrapping_Mode",
       signature: "gl.objects.textures.wrapping_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Wrapping_Mode is (Clamp, Repeat, Clamp_To_Border, Clamp_To_Edge,\n                       Mirrored_Repeat);",
       }   ,
   ]
,record_types:    [
       {
       name: "Texture_Proxy",
       qualified_name: "GL.Objects.Textures.Texture_Proxy",
       signature: "gl.objects.textures.texture_proxy",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Texture_Proxy (Kind : Low_Level.Enums.Texture_Kind) is\n  tagged limited null record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Texture",
       qualified_name: "GL.Objects.Textures.Texture",
       signature: "gl.objects.textures.texture",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Texture is new GL_Object with private;",
       }   ,
       {
       name: "Texture_Target",
       qualified_name: "GL.Objects.Textures.Texture_Target",
       signature: "gl.objects.textures.texture_target",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Texture_Target (Kind : Low_Level.Enums.Texture_Kind) is\n  new Texture_Proxy (Kind) with null record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Magnifying_Function",
       qualified_name: "GL.Objects.Textures.Magnifying_Function",
       signature: "gl.objects.textures.magnifying_function",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Magnifying_Function is Minifying_Function range Nearest .. Linear;",
       }   ,
       {
       name: "Mipmap_Level",
       qualified_name: "GL.Objects.Textures.Mipmap_Level",
       signature: "gl.objects.textures.mipmap_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Mipmap_Level is Int range 0 .. Int'Last;",
       }   ,
       {
       name: "Priority",
       qualified_name: "GL.Objects.Textures.Priority",
       signature: "gl.objects.textures.priority",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Priority is Double range 0.0 .. 1.0;",
       }   ,
       {
       name: "Texture_Unit",
       qualified_name: "GL.Objects.Textures.Texture_Unit",
       signature: "gl.objects.textures.texture_unit",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Texture_Unit is Int range 0 .. Int'Last;",
       }   ,
   ]
,}
---
