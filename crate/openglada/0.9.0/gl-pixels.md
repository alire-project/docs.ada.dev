---
crate: openglada
layout: gnatdoc
gnatdoc: {
name: "GL.Pixels",
qualified_name: "GL.Pixels",
signature: "gl.pixels",
enclosing: "gl",
is_private: false,
documentation: "part of OpenGLAda, (c) 2017 Felix Krause\nreleased under the terms of the MIT license, see the file \"COPYING\"",
documentation_snippet: "",
simple_types:    [
       {
       name: "Alignment",
       qualified_name: "GL.Pixels.Alignment",
       signature: "gl.pixels.alignment",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Alignment is (Bytes, Even_Bytes, Words, Double_Words);",
       }   ,
       {
       name: "Channel_Data_Type",
       qualified_name: "GL.Pixels.Channel_Data_Type",
       signature: "gl.pixels.channel_data_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Channel_Data_Type is (None, Int_Type, Unsigned_Int_Type, Float_Type,\n                           Unsigned_Normalized, Signed_Normalized);",
       }   ,
       {
       name: "Data_Format",
       qualified_name: "GL.Pixels.Data_Format",
       signature: "gl.pixels.data_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Format is (Stencil_Index, Depth_Component, Red,\n                     RGB, RGBA, BGR, BGRA, RG, RG_Integer, Depth_Stencil,\n                     Red_Integer, RGB_Integer, RGBA_Integer, BGR_Integer,\n                     BGRA_Integer);",
       }   ,
       {
       name: "Data_Type",
       qualified_name: "GL.Pixels.Data_Type",
       signature: "gl.pixels.data_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Data_Type is (Byte, Unsigned_Byte, Short, Unsigned_Short, Int,\n                   Unsigned_Int, Float, Bitmap, Unsigned_Byte_3_3_2,\n                   Unsigned_Short_4_4_4_4,\n                   Unsigned_Short_5_5_5_1,\n                   Unsigned_Int_8_8_8_8,\n                   Unsigned_Int_10_10_10_2,\n                   Unsigned_Byte_2_3_3_Rev,\n                   Unsigned_Short_5_6_5,\n                   Unsinged_Short_5_6_5_Rev,\n                   Unsigned_Short_4_4_4_4_Rev,\n                   Unsigned_Short_1_5_5_5_Rev,\n                   Unsigned_Int_8_8_8_8_Rev,\n                   Unsigned_Int_2_10_10_10_Rev);",
       }   ,
       {
       name: "Framebuffer_Format",
       qualified_name: "GL.Pixels.Framebuffer_Format",
       signature: "gl.pixels.framebuffer_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Framebuffer_Format is (Color_Index, Red, Green, Blue, Alpha, RGB, RGBA,\n                            Luminance, Luminance_Alpha, BGR, BGRA);",
       }   ,
       {
       name: "Internal_Format",
       qualified_name: "GL.Pixels.Internal_Format",
       signature: "gl.pixels.internal_format",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Internal_Format is (Depth_Component, Red, Alpha, RGB, RGBA, Luminance,\n                         Luminance_Alpha, R3_G3_B2, Alpha4, Alpha8, Alpha12,\n                         Alpha16, Luminance4, Luminance8, Luminance12,\n                         Luminance16, Luminance4_Alpha4, Luminance6_Alpha2,\n                         Luminance8_Alpha8, Luminance12_Alpha4,\n                         Luminance12_Alpha12, Luminance16_Alpha16,\n                         Intensity, Intensity4, Intensity8, Intensity12,\n                         Intensity16, RGB4, RGB5, RGB8, RGB10, RGB12, RGB16,\n                         RGBA2, RGBA4, RGB5_A1, RGBA8, RGB10_A2, RGBA12,\n                         RGBA16, Depth_Component16, Depth_Component24,\n                         Depth_Component32, Compressed_Red, Compressed_RG,\n                         RG, R8, R16, RG8, RG16, R16F, R32F, RG16F, RG32F,\n                         R8I, R8UI, R16I, R16UI, R32I, R32UI, RG8I, RG8UI,\n                         RG16I, RG16UI, RG32I, RG32UI,\n                         Compressed_RGB_S3TC_DXT1, Compressed_RGBA_S3TC_DXT1,\n                         Compressed_RGBA_S3TC_DXT3,\n                         Compressed_RGBA_S3TC_DXT5, Compressed_Alpha,\n                         Compressed_Luminance, Compressed_Luminance_Alpha,\n                         Compressed_Intensity, Compressed_RGB,\n                         Compressed_RGBA, RGBA32F, RGB32F, RGBA16F, RGB16F,\n                         Depth24_Stencil8,\n                         R11F_G11F_B10F, RGB9_E5, SRGB, SRGB8, SRGB_Alpha,\n                         SRGB8_Alpha8, SLuminance_Alpha, SLuminance8_Alpha8,\n                         SLuminance, SLuminance8, Compressed_SRGB,\n                         Compressed_SRGB_Alpha, Compressed_SRGB_S3TC_DXT1,\n                         Compressed_SRGB_Alpha_S3TC_DXT1,\n                         Compressed_SRGB_Alpha_S3TC_DXT3,\n                         Compressed_SRGB_Alpha_S3TC_DXT5,\n                         RGBA32UI, RGB32UI, RGBA16UI, RGB16UI, RGBA8UI,\n                         RGB8UI, RGBA32I, RGB32I, RGBA16I, RGB16I, RGBA8I,\n                         RGB8I, Compressed_Red_RGTC1,\n                         Compressed_Signed_Red_RGTC1, Compressed_RG_RGTC2,\n                         Compressed_Signed_RG_RGTC2,\n                         Compressed_RGBA_BPTC_Unorm,\n                         Compressed_SRGB_Alpha_BPTC_UNorm,\n                         Compressed_RGB_BPTC_Signed_Float,\n                         Compressed_RGB_BPTC_Unsigned_Float, R8_SNorm,\n                         RG8_SNorm, RGB8_SNorm, RGBA8_SNorm, R16_SNorm,\n                         RG16_SNorm, RGB16_SNorm, RGBA16_SNorm, RGB10_A2UI,\n                         Compressed_RGBA_ASTC_4x4, Compressed_RGBA_ASTC_5x4,\n                         Compressed_RGBA_ASTC_5x5, Compressed_RGBA_ASTC_6x5,\n                         Compressed_RGBA_ASTC_6x6, Compressed_RGBA_ASTC_8x5,\n                         Compressed_RGBA_ASTC_8x6, Compressed_RGBA_ASTC_8x8,\n                         Compressed_RGBA_ASTC_10x5,\n                         Compressed_RGBA_ASTC_10x6,\n                         Compressed_RGBA_ASTC_10x8,\n                         Compressed_RGBA_ASTC_10x10,\n                         Compressed_RGBA_ASTC_12x10,\n                         Compressed_RGBA_ASTC_12x12,\n                         Compressed_SRGB8_Alpha8_ASTC_4x4,\n                         Compressed_SRGB8_Alpha8_ASTC_5x4,\n                         Compressed_SRGB8_Alpha8_ASTC_5x5,\n                         Compressed_SRGB8_Alpha8_ASTC_6x5,\n                         Compressed_SRGB8_Alpha8_ASTC_6x6,\n                         Compressed_SRGB8_Alpha8_ASTC_8x5,\n                         Compressed_SRGB8_Alpha8_ASTC_8x6,\n                         Compressed_SRGB8_Alpha8_ASTC_8x8,\n                         Compressed_SRGB8_Alpha8_ASTC_10x5,\n                         Compressed_SRGB8_Alpha8_ASTC_10x6,\n                         Compressed_SRGB8_Alpha8_ASTC_10x8,\n                         Compressed_SRGB8_Alpha8_ASTC_10x10,\n                         Compressed_SRGB8_Alpha8_ASTC_12x10,\n                         Compressed_SRGB8_Alpha8_ASTC_12x12);",
       }   ,
   ]
,}
---
