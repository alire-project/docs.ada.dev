---
crate: freetypeada
layout: gnatdoc
gnatdoc: {
name: "FT.Faces",
qualified_name: "FT.Faces",
signature: "ft.faces",
enclosing: "ft",
is_private: false,
documentation: "reference-counted smart pointer",
documentation_snippet: "",
simple_types:    [
       {
       name: "Char_Index_Type",
       qualified_name: "FT.Faces.Char_Index_Type",
       signature: "ft.faces.char_index_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Char_Index_Type is new UInt;",
       }   ,
       {
       name: "Encoding",
       qualified_name: "FT.Faces.Encoding",
       signature: "ft.faces.encoding",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Encoding is (None, Adobe_Custom, Adobe_Expert, Adobe_Standard,\n                  Apple_Roman, Big5, GB2312, Johab, Adobe_Latin_1,\n                  Old_Latin_2, SJIS, MS_Symbol, Unicode, Wansung);",
       }   ,
       {
       name: "Face_Index_Type",
       qualified_name: "FT.Faces.Face_Index_Type",
       signature: "ft.faces.face_index_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Face_Index_Type is new Interfaces.C.long;",
       }   ,
       {
       name: "Load_Flag",
       qualified_name: "FT.Faces.Load_Flag",
       signature: "ft.faces.load_flag",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Load_Flag is (Load_Default, Load_No_Scale, Load_No_Hinting, Load_Render,\n                   Load_No_Bitmap, Load_Vertical_Layout, Load_Force_Autohint,\n                   Load_Crop_Bitmap, Load_Pedantic, Load_Advance_Only,\n                   Load_Ignore_Global_Advance_Width, Load_No_Recourse,\n                   Load_Ignore_Transform, Load_Monochrome, Load_Linear_Design,\n                   Load_SBits_Only, Load_No_Autohint, Load_Load_Colour,\n                   Load_Compute_Metrics, Load_Bitmap_Metrics_Only);",
       }   ,
       {
       name: "Render_Mode",
       qualified_name: "FT.Faces.Render_Mode",
       signature: "ft.faces.render_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Render_Mode is (Render_Mode_Normal, Render_Mode_Light,\n                     Render_Mode_Mono, Render_Mode_LCD,\n                     Render_Mode_LCD_V, Render_Mode_Max);",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Face_Reference",
       qualified_name: "FT.Faces.Face_Reference",
       signature: "ft.faces.face_reference",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Face_Reference is new Ada.Finalization.Controlled with private;",
       }   ,
   ]
,constants:    [
       {
       name: "Undefined_Character_Code",
       qualified_name: "FT.Faces.Undefined_Character_Code",
       signature: "ft.faces.undefined_character_code",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Undefined_Character_Code : constant Char_Index_Type;",
       }   ,
   ]
,}
---
