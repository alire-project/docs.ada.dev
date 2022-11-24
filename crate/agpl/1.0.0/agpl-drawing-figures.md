---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Drawing.Figures",
qualified_name: "Agpl.Drawing.Figures",
signature: "agpl.drawing.figures",
enclosing: "agpl.drawing",
is_private: false,
documentation: "",
documentation_snippet: "",
array_types:    [
       {
       name: "Float_Array",
       qualified_name: "Agpl.Drawing.Figures.Float_Array",
       signature: "agpl.drawing.figures.float_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Float_Array is array (Positive range <>) of Float;",
       }   ,
   ]
,tagged_types:    [
       {
       name: "Bivariate_Ellipse",
       qualified_name: "Agpl.Drawing.Figures.Bivariate_Ellipse",
       signature: "agpl.drawing.figures.bivariate_ellipse",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Bivariate_Ellipse (<>) is new Drawable with private;",
       }   ,
       {
       name: "Float_List",
       qualified_name: "Agpl.Drawing.Figures.Float_List",
       signature: "agpl.drawing.figures.float_list",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Float_List is new Float_Lists.List with null record;",
       }   ,
       {
       name: "Vprogress",
       qualified_name: "Agpl.Drawing.Figures.Vprogress",
       signature: "agpl.drawing.figures.vprogress",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vprogress is new Drawable with record\n   X, Y,\n   Width,\n   Height,\n   Max,\n   Val        : Float;\n   Text_Above : Boolean := True;\n   Show_Pct   : Boolean := True;\nend record;",
       }   ,
   ]
,subtypes:    [
       {
       name: "Confidence",
       qualified_name: "Agpl.Drawing.Figures.Confidence",
       signature: "agpl.drawing.figures.confidence",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Confidence is Float range 0.0 .. 1.0;",
       }   ,
       {
       name: "Cov2d",
       qualified_name: "Agpl.Drawing.Figures.Cov2d",
       signature: "agpl.drawing.figures.cov2d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Cov2d is Ra.Real_Matrix (1 .. 2, 1 .. 2);",
       }   ,
       {
       name: "Point",
       qualified_name: "Agpl.Drawing.Figures.Point",
       signature: "agpl.drawing.figures.point",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "subtype Point is Ra.Real_Vector (1 .. 2);",
       }   ,
   ]
,}
---
