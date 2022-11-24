---
crate: asfml
layout: gnatdoc
gnatdoc: {
name: "Sf.Graphics.BlendMode",
qualified_name: "Sf.Graphics.BlendMode",
signature: "sf.graphics.blendmode",
enclosing: "sf.graphics",
is_private: false,
documentation: "//////////////////////////////////////////////////////////\n/ @brief Enumeration of the blending factors\n/\n//////////////////////////////////////////////////////////\n/< (0, 0, 0, 0)\n/< (1, 1, 1, 1)\n/< (src.r, src.g, src.b, src.a)\n/< (1, 1, 1, 1) - (src.r, src.g, src.b, src.a)\n/< (dst.r, dst.g, dst.b, dst.a)\n/< (1, 1, 1, 1) - (dst.r, dst.g, dst.b, dst.a)\n/< (src.a, src.a, src.a, src.a)\n/< (1, 1, 1, 1) - (src.a, src.a, src.a, src.a)\n/< (dst.a, dst.a, dst.a, dst.a)\n/< (1, 1, 1, 1) - (dst.a, dst.a, dst.a, dst.a)",
documentation_snippet: "",
simple_types:    [
       {
       name: "sfBlendEquation",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendEquation",
       signature: "sf.graphics.blendmode.sfblendequation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfBlendEquation is\n  (sfBlendEquationAdd,\n   sfBlendEquationSubtract,\n   sfBlendEquationReverseSubtract);",
       }   ,
       {
       name: "sfBlendFactor",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendFactor",
       signature: "sf.graphics.blendmode.sfblendfactor",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfBlendFactor is\n  (sfBlendFactorZero,\n   sfBlendFactorOne,\n   sfBlendFactorSrcColor,\n   sfBlendFactorOneMinusSrcColor,\n   sfBlendFactorDstColor,\n   sfBlendFactorOneMinusDstColor,\n   sfBlendFactorSrcAlpha,\n   sfBlendFactorOneMinusSrcAlpha,\n   sfBlendFactorDstAlpha,\n   sfBlendFactorOneMinusDstAlpha);",
       }   ,
   ]
,record_types:    [
       {
       name: "sfBlendMode",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendMode",
       signature: "sf.graphics.blendmode.sfblendmode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type sfBlendMode is record\n   colorSrcFactor : aliased sfBlendFactor;\n   colorDstFactor : aliased sfBlendFactor;\n   colorEquation : aliased sfBlendEquation;\n   alphaSrcFactor : aliased sfBlendFactor;\n   alphaDstFactor : aliased sfBlendFactor;\n   alphaEquation : aliased sfBlendEquation;\nend record;",
       }   ,
   ]
,variables:    [
       {
       name: "sfBlendAdd",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendAdd",
       signature: "sf.graphics.blendmode.sfblendadd",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfBlendAdd : aliased sfBlendMode;",
       }   ,
       {
       name: "sfBlendAlpha",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendAlpha",
       signature: "sf.graphics.blendmode.sfblendalpha",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfBlendAlpha : aliased sfBlendMode;",
       }   ,
       {
       name: "sfBlendMultiply",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendMultiply",
       signature: "sf.graphics.blendmode.sfblendmultiply",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfBlendMultiply : aliased sfBlendMode;",
       }   ,
       {
       name: "sfBlendNone",
       qualified_name: "Sf.Graphics.BlendMode.sfBlendNone",
       signature: "sf.graphics.blendmode.sfblendnone",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "sfBlendNone : aliased sfBlendMode;",
       }   ,
   ]
,}
---
