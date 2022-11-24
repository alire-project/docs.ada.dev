---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Objects.Programs",
qualified_name: "GL.Objects.Programs",
signature: "gl.objects.programs",
enclosing: "gl.objects",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Active_Attribute",
       qualified_name: "GL.Objects.Programs.Active_Attribute",
       signature: "gl.objects.programs.active_attribute",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Active_Attribute is (Int_Type, Unsigned_Int_Type,\n                          Float_Vec2_Type, Float_Vec3_Type, Float_Vec4_Type,\n                          Int_Vec2_Type, Int_Vec3_Type, Int_Vec4_Type,\n                          Float_Mat2_Type, Float_Mat3_Type, Float_Mat4_Type,\n                          Float_Mat2x3_Type, Float_Mat2x4_Type,\n                          Float_Mat3x2_Type, Float_Mat3x4_Type,\n                          Float_Mat4x2_Type, Float_Mat4x3_Type,\n                          Unsigned_Int_Vec2_Type,\n                          Unsigned_Int_Vec3_Type, Unsigned_Int_Vec4_Type);",
       }   ,
       {
       name: "Buffer_Mode",
       qualified_name: "GL.Objects.Programs.Buffer_Mode",
       signature: "gl.objects.programs.buffer_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Buffer_Mode is (Interleaved_Attribs, Separate_Attribs);",
       }   ,
       {
       name: "Tessellation_Primitive_Mode",
       qualified_name: "GL.Objects.Programs.Tessellation_Primitive_Mode",
       signature: "gl.objects.programs.tessellation_primitive_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tessellation_Primitive_Mode is (Triangles, Quads, Isolines);",
       }   ,
       {
       name: "Tessellation_Spacing",
       qualified_name: "GL.Objects.Programs.Tessellation_Spacing",
       signature: "gl.objects.programs.tessellation_spacing",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Tessellation_Spacing is (Equal, Fractional_Odd, Fractional_Even);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Program",
       qualified_name: "GL.Objects.Programs.Program",
       signature: "gl.objects.programs.program",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Program is new GL_Object with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Subroutine_Index_Type",
       qualified_name: "GL.Objects.Programs.Subroutine_Index_Type",
       signature: "gl.objects.programs.subroutine_index_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Subroutine_Index_Type is UInt;",
       }   ,
       {
       name: "Uniform_Location_Type",
       qualified_name: "GL.Objects.Programs.Uniform_Location_Type",
       signature: "gl.objects.programs.uniform_location_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Uniform_Location_Type is Int range -1 .. Int'Last;",
       }   ,
   ]
,constants:    [
       {
       name: "Invalid_Index",
       qualified_name: "GL.Objects.Programs.Invalid_Index",
       signature: "gl.objects.programs.invalid_index",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Invalid_Index : constant Subroutine_Index_Type;",
       }   ,
   ]
,}
---
