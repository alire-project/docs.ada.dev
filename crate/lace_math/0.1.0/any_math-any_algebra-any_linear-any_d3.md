---
crate: lace_math
layout: gnatdoc
gnatdoc: {
name: "any_math.any_Algebra.any_linear.any_d3",
qualified_name: "any_math.any_Algebra.any_linear.any_d3",
signature: "any_math.any_algebra.any_linear.any_d3",
enclosing: "any_math.any_algebra.any_linear",
is_private: false,
documentation: "----------\n- Vector_3",
documentation_snippet: "",
simple_types:    [
       {
       name: "Euler",
       qualified_name: "any_math.any_Algebra.any_linear.any_d3.Euler",
       signature: "any_math.any_algebra.any_linear.any_d3.euler",
       enclosing: "",
       is_private: false,
       documentation: "\n1: Roll\n2: Pitch\n3: Yaw",
       documentation_snippet: "type Euler is new Vector_3;",
       }   ,
   ]
,record_types:    [
       {
       name: "Rectangle",
       qualified_name: "any_math.any_Algebra.any_linear.any_d3.Rectangle",
       signature: "any_math.any_algebra.any_linear.any_d3.rectangle",
       enclosing: "",
       is_private: false,
       documentation: "\n@field Min\n  Bottom left corner.\n@field Max\n  Upper right corner.",
       documentation_snippet: "type Rectangle is\n   record\n      Min : Integers (1 .. 2);\n      Max : Integers (1 .. 2);\n   end record;",
       }   ,
   ]
,constants:    [
       {
       name: "y_Up_to_z_Up",
       qualified_name: "any_math.any_Algebra.any_linear.any_d3.y_Up_to_z_Up",
       signature: "any_math.any_algebra.any_linear.any_d3.y_up_to_z_up",
       enclosing: "",
       is_private: false,
       documentation: "by a vector to change co-ordinate systems.",
       documentation_snippet: "y_Up_to_z_Up : constant Matrix_3x3;",
       }   ,
       {
       name: "z_Up_to_y_Up",
       qualified_name: "any_math.any_Algebra.any_linear.any_d3.z_Up_to_y_Up",
       signature: "any_math.any_algebra.any_linear.any_d3.z_up_to_y_up",
       enclosing: "",
       is_private: false,
       documentation: "by a vector to change co-ordinate systems.",
       documentation_snippet: "z_Up_to_y_Up : constant Matrix_3x3;",
       }   ,
   ]
,}
---
