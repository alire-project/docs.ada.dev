---
crate: mathpaqs
layout: gnatdoc
gnatdoc: {
name: "Contours",
qualified_name: "Contours",
signature: "contours",
enclosing: "",
is_private: false,
documentation: "======================================================================\n\n     Contours.ads\n\n     CONREC is a contouring subroutine for rectangularly spaced data.\n\n     It emits calls to a line drawing subroutine supplied by the user\n     which draws a contour map corresponding to floating-point data on\n     a randomly spaced rectangular grid. The coordinates emitted are\n     in the same units given in the x() and y() arrays.\n\n     Any number of contour levels may be specified but they must be\n     in order of increasing value.\n\n     procedure ConRec(d,x,y,z)\n       d: matrix of data to contour\n       x: data matrix column coordinates\n       y: data matrix row coordinates\n       z: contour levels in increasing order\n\n       Vecout: user-defined line drawing procedure, of the form\n               ( x1, y1, x2, y2, z: Real );\n\n     There is often the requirement to distinguish each contour\n     line with a different colour or a different line style. This\n     can be done in many ways using the contour values z for a\n     particular line segment.\n\n     A demo is available in file: cr_demo.adb\n\n     Author: Paul D. Bourke\n     Ada version: 23.I.1999, Gautier de Montmollin\n\n     This is part of the Mathpaqs collection of mathematical packages.\n     Latest version may be available at:\n         home page:     http://mathpaqs.sf.net/\n         project page:  http://sf.net/projects/mathpaqs/\n         mirror:        https://github.com/svn2github/mathpaqs\n======================================================================\n\n@formal Real\n  User-defined line drawing procedure:\n@formal Vecout",
documentation_snippet: "",
array_types:    [
       {
       name: "Contour_data",
       qualified_name: "Contours.Contour_data",
       signature: "contours.contour_data",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Contour_data  is array ( Integer range <>, Integer range <> ) of Real;",
       }   ,
       {
       name: "Contour_level",
       qualified_name: "Contours.Contour_level",
       signature: "contours.contour_level",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Contour_level is array ( Integer range <> ) of Real;",
       }   ,
       {
       name: "Contour_pos",
       qualified_name: "Contours.Contour_pos",
       signature: "contours.contour_pos",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Contour_pos   is array ( Integer range <> ) of Real;",
       }   ,
   ]
,}
---
