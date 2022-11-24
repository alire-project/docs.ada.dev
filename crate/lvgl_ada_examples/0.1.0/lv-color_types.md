---
crate: lvgl_ada_examples
layout: gnatdoc
gnatdoc: {
name: "Lv.Color_Types",
qualified_name: "Lv.Color_Types",
signature: "lv.color_types",
enclosing: "lv",
is_private: false,
documentation: "",
documentation_snippet: "",
record_types:    [
       {
       name: "Color_T",
       qualified_name: "Lv.Color_Types.Color_T",
       signature: "lv.color_types.color_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_T (Discr : unsigned := 0) is record\n   case Discr is\n      when 0 =>\n         Comp : aliased Color_T_Comp;\n      when others =>\n         Full : aliased Color_Int_T;\n   end case;\nend record\n  with Pack, Object_Size => 32;",
       }   ,
       {
       name: "Color_T_Comp",
       qualified_name: "Lv.Color_Types.Color_T_Comp",
       signature: "lv.color_types.color_t_comp",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_T_Comp is record\n   Blue  : aliased Uint8_T;\n   Green : aliased Uint8_T;\n   Red   : aliased Uint8_T;\n   Alpha : aliased Uint8_T;\nend record\nwith Pack, Object_Size => 32;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Color_Int_T",
       qualified_name: "Lv.Color_Types.Color_Int_T",
       signature: "lv.color_types.color_int_t",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Color_Int_T is Uint32_T;",
       }   ,
   ]
,}
---
