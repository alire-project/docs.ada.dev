---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.RenderStates",
qualified_name: "Sf.Graphics.RenderStates",
signature: "sf.graphics.renderstates",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Define the states used for drawing to a RenderTarget\n/\n//////////////////////////////////////////////////////////\n/< Blending mode\n/< Transform\n/< Texture\n/< Shader",
documentation_snippet: "",
record_types:    [
       {
       name: "sfRenderStates",
       qualified_name: "Sf.Graphics.RenderStates.sfRenderStates",
       signature: "sf.graphics.renderstates.sfrenderstates",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfRenderStates is record\n   blendMode : aliased Sf.Graphics.BlendMode.sfBlendMode;\n   transform : aliased Sf.Graphics.Transform.sfTransform;\n   texture : sfTexture_Ptr;\n   shader : sfShader_Ptr;\nend record;",
       }   ,
   ]
,access_types:    [
       {
       name: "sfRenderStates_Ptr",
       qualified_name: "Sf.Graphics.RenderStates.sfRenderStates_Ptr",
       signature: "sf.graphics.renderstates.sfrenderstates_ptr",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfRenderStates_Ptr is access all sfRenderStates;",
       }   ,
   ]
,}
---
