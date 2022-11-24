---
crate: agpl
layout: gnatdoc
gnatdoc: {
name: "Agpl.Transf2D",
qualified_name: "Agpl.Transf2D",
signature: "agpl.transf2d",
enclosing: "agpl",
is_private: false,
documentation: "Transformations for translations/rotations in a 2D environment.\nDoing Matrix * Vector' cause the described effects.\nDoing Vector * Matrix  cause ???\n\n@formal Real",
documentation_snippet: "",
simple_types:    [
       {
       name: "Pose",
       qualified_name: "Agpl.Transf2D.Pose",
       signature: "agpl.transf2d.pose",
       enclosing: "",
       is_private: false,
       documentation: "X, Y, Angle, Homogeneous component.",
       documentation_snippet: "type Pose is new Real_Array (1 .. 4);",
       }   ,
       {
       name: "Transformation",
       qualified_name: "Agpl.Transf2D.Transformation",
       signature: "agpl.transf2d.transformation",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Transformation is new Real_Matrix (1 .. 4, 1 .. 4);",
       }   ,
   ]
,array_types:    [
       {
       name: "Real_Array",
       qualified_name: "Agpl.Transf2D.Real_Array",
       signature: "agpl.transf2d.real_array",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Real_Array  is array (Integer'Base range <>) of Real;",
       }   ,
       {
       name: "Real_Matrix",
       qualified_name: "Agpl.Transf2D.Real_Matrix",
       signature: "agpl.transf2d.real_matrix",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Real_Matrix is array (Integer'Base range <>,\n                           Integer'Base range <>) of Real;",
       }   ,
   ]
,constants:    [
       {
       name: "A",
       qualified_name: "Agpl.Transf2D.A",
       signature: "agpl.transf2d.a",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "A : constant := Pose'First + 2;",
       }   ,
       {
       name: "H",
       qualified_name: "Agpl.Transf2D.H",
       signature: "agpl.transf2d.h",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "H : constant := Pose'Last;",
       }   ,
       {
       name: "Identity",
       qualified_name: "Agpl.Transf2D.Identity",
       signature: "agpl.transf2d.identity",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Identity : constant Transformation;",
       }   ,
       {
       name: "Null_Pose",
       qualified_name: "Agpl.Transf2D.Null_Pose",
       signature: "agpl.transf2d.null_pose",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Null_Pose : constant Pose := (X => 0.0, Y => 0.0, A => 0.0, H => 1.0);",
       }   ,
       {
       name: "X",
       qualified_name: "Agpl.Transf2D.X",
       signature: "agpl.transf2d.x",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "X : constant := Pose'First;",
       }   ,
       {
       name: "Y",
       qualified_name: "Agpl.Transf2D.Y",
       signature: "agpl.transf2d.y",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Y : constant := Pose'First + 1;",
       }   ,
   ]
,variables:    [
       {
       name: "Origin",
       qualified_name: "Agpl.Transf2D.Origin",
       signature: "agpl.transf2d.origin",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Origin    :          Pose renames Null_Pose;",
       }   ,
   ]
,}
---
