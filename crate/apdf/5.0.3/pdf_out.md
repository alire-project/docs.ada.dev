---
crate: apdf
layout: gnatdoc
gnatdoc: {
name: "PDF_Out",
qualified_name: "PDF_Out",
signature: "pdf_out",
enclosing: "",
is_private: false,
documentation: "---------------------------------------------------------------\n The abstract PDF output stream root type.                   --\n From this package, you can use the following derived types: --\n    * PDF_Out_File    : output in a file                     --\n    * PDF_Out_String  : output in a string                   --\n Of course you can define your own derived types.            --\n---------------------------------------------------------------",
documentation_snippet: "",
simple_types:    [
       {
       name: "Font_Type",
       qualified_name: "PDF_Out.Font_Type",
       signature: "pdf_out.font_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum Courier\n@enum Courier_Bold\n@enum Courier_Bold_Oblique\n@enum Courier_Oblique\n@enum Helvetica\n@enum Helvetica_Bold\n@enum Helvetica_Bold_Oblique\n@enum Helvetica_Oblique\n@enum Symbol\n@enum Times_Bold\n@enum Times_Bold_Italic\n@enum Times_Italic\n@enum Times_Roman\n@enum Zapf_Dingbats\n  Fonts imported into the PDF document\n@enum External_Font",
       documentation_snippet: "type Font_Type is\n   (\n    Courier,\n    Courier_Bold,\n    Courier_Bold_Oblique,\n    Courier_Oblique,\n    Helvetica,\n    Helvetica_Bold,\n    Helvetica_Bold_Oblique,\n    Helvetica_Oblique,\n    Symbol,\n    Times_Bold,\n    Times_Bold_Italic,\n    Times_Italic,\n    Times_Roman,\n    Zapf_Dingbats,\n    External_Font\n   );",
       }   ,
       {
       name: "Inside_path_rule",
       qualified_name: "PDF_Out.Inside_path_rule",
       signature: "pdf_out.inside_path_rule",
       enclosing: "",
       is_private: false,
       documentation: "Rule to determine how to fill areas within a (non-trivial) path.\nSee 8.5.3.3.2 and 8.5.3.3.3 of PDF specification\n\n@enum nonzero_winding_number\n@enum even_odd",
       documentation_snippet: "type Inside_path_rule is (nonzero_winding_number, even_odd);",
       }   ,
       {
       name: "PDF_type",
       qualified_name: "PDF_Out.PDF_type",
       signature: "pdf_out.pdf_type",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum PDF_1_3\n  PDF 1.3",
       documentation_snippet: "type PDF_type is (\n  PDF_1_3\n);",
       }   ,
       {
       name: "Rendering_Mode",
       qualified_name: "PDF_Out.Rendering_Mode",
       signature: "pdf_out.rendering_mode",
       enclosing: "",
       is_private: false,
       documentation: "\n@enum fill\n@enum stroke\n@enum fill_then_stroke\n@enum invisible\n  Same, but also add text to path for clipping.\n@enum fill_and_add_to_path\n@enum stroke_and_add_to_path\n@enum fill_then_stroke_and_add_to_path\n@enum add_to_path",
       documentation_snippet: "type Rendering_Mode is (\n  fill, stroke, fill_then_stroke, invisible,\n  fill_and_add_to_path,\n  stroke_and_add_to_path,\n  fill_then_stroke_and_add_to_path,\n  add_to_path\n);",
       }   ,
   ]
,record_types:    [
       {
       name: "Color_Type",
       qualified_name: "PDF_Out.Color_Type",
       signature: "pdf_out.color_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Color_Type is record\n  red, green, blue: Color_Value;\nend record;",
       }   ,
       {
       name: "Margins_Type",
       qualified_name: "PDF_Out.Margins_Type",
       signature: "pdf_out.margins_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Margins_Type is record\n  left, right, top, bottom: Real;\nend record;",
       }   ,
       {
       name: "Point",
       qualified_name: "PDF_Out.Point",
       signature: "pdf_out.point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Point is record\n  x, y : Real;\nend record;",
       }   ,
       {
       name: "Rectangle",
       qualified_name: "PDF_Out.Rectangle",
       signature: "pdf_out.rectangle",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Rectangle is record\n  x_min, y_min,\n  width, height : Real;\nend record;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "PDF_Out_File",
       qualified_name: "PDF_Out.PDF_Out_File",
       signature: "pdf_out.pdf_out_file",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PDF_Out_File is new PDF_Out_Stream with private;",
       }   ,
       {
       name: "PDF_Out_Stream",
       qualified_name: "PDF_Out.PDF_Out_Stream",
       signature: "pdf_out.pdf_out_stream",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PDF_Out_Stream is abstract tagged private;",
       }   ,
       {
       name: "PDF_Out_String",
       qualified_name: "PDF_Out.PDF_Out_String",
       signature: "pdf_out.pdf_out_string",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type PDF_Out_String is new PDF_Out_Stream with private;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Color_Value",
       qualified_name: "PDF_Out.Color_Value",
       signature: "pdf_out.color_value",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Color_Value is Real range 0.0 .. 1.0;",
       }   ,
       {
       name: "Path_Rendering_Mode",
       qualified_name: "PDF_Out.Path_Rendering_Mode",
       signature: "pdf_out.path_rendering_mode",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Path_Rendering_Mode is Rendering_Mode range fill .. fill_then_stroke;",
       }   ,
       {
       name: "Standard_Font_Type",
       qualified_name: "PDF_Out.Standard_Font_Type",
       signature: "pdf_out.standard_font_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Standard_Font_Type is Font_Type range Courier .. Zapf_Dingbats;",
       }   ,
   ]
,constants:    [
       {
       name: "A4_landscape",
       qualified_name: "PDF_Out.A4_landscape",
       signature: "pdf_out.a4_landscape",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "A4_landscape: constant Rectangle:= (0.0, 0.0, A4_portrait.height, A4_portrait.width);",
       }   ,
       {
       name: "A4_portrait",
       qualified_name: "PDF_Out.A4_portrait",
       signature: "pdf_out.a4_portrait",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "A4_portrait : constant Rectangle:= (0.0, 0.0, 21.0 * one_cm, 29.7 * one_cm);",
       }   ,
       {
       name: "black",
       qualified_name: "PDF_Out.black",
       signature: "pdf_out.black",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "black: constant Color_Type:= (0.0,0.0,0.0);",
       }   ,
       {
       name: "cm_2_5",
       qualified_name: "PDF_Out.cm_2_5",
       signature: "pdf_out.cm_2_5",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "cm_2_5   : constant:= one_cm * 2.5;",
       }   ,
       {
       name: "cm_2_5_margins",
       qualified_name: "PDF_Out.cm_2_5_margins",
       signature: "pdf_out.cm_2_5_margins",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "cm_2_5_margins: constant Margins_Type:= (cm_2_5, cm_2_5, cm_2_5, cm_2_5);",
       }   ,
       {
       name: "default_line_spacing",
       qualified_name: "PDF_Out.default_line_spacing",
       signature: "pdf_out.default_line_spacing",
       enclosing: "",
       is_private: false,
       documentation: "in Point (pt) units",
       documentation_snippet: "default_line_spacing: constant:= 1.2;",
       }   ,
       {
       name: "Default_PDF_type",
       qualified_name: "PDF_Out.Default_PDF_type",
       signature: "pdf_out.default_pdf_type",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Default_PDF_type: constant PDF_type:= PDF_1_3;",
       }   ,
       {
       name: "initial_line_width",
       qualified_name: "PDF_Out.initial_line_width",
       signature: "pdf_out.initial_line_width",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "initial_line_width: constant:= 1.0;",
       }   ,
       {
       name: "one_cm",
       qualified_name: "PDF_Out.one_cm",
       signature: "pdf_out.one_cm",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "one_cm   : constant:= 72.0 / 2.54;",
       }   ,
       {
       name: "one_inch",
       qualified_name: "PDF_Out.one_inch",
       signature: "pdf_out.one_inch",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "one_inch : constant:= 72.0;",
       }   ,
       {
       name: "reference",
       qualified_name: "PDF_Out.reference",
       signature: "pdf_out.reference",
       enclosing: "",
       is_private: false,
       documentation: "hopefully the latest version is at that URL ^",
       documentation_snippet: "reference : constant String:= \"05-Sep-2019\";",
       }   ,
       {
       name: "version",
       qualified_name: "PDF_Out.version",
       signature: "pdf_out.version",
       enclosing: "",
       is_private: false,
       documentation: "hopefully the latest version is at that URL ^",
       documentation_snippet: "version   : constant String:= \"005\";",
       }   ,
       {
       name: "web",
       qualified_name: "PDF_Out.web",
       signature: "pdf_out.web",
       enclosing: "",
       is_private: false,
       documentation: "hopefully the latest version is at that URL ^",
       documentation_snippet: "web       : constant String:= \"http://apdf.sf.net/\";",
       }   ,
   ]
,}
---
