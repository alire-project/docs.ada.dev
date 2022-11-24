---
crate: eagle_lander
layout: gnatdoc
gnatdoc: {
name: "Geom",
qualified_name: "Geom",
signature: "geom",
enclosing: "",
is_private: false,
documentation: "-----------------------------------------------------------------------------\n                                                                           --\n                               Eagle Lander                                --\n                                                                           --\n         Copyright (C) 2015 Fabien Chouteau (chouteau@adacore.com)         --\n                                                                           --\n    Eagle Lander is free software: you can redistribute it and/or modify   --\n    it under the terms of the GNU General Public License as published by   --\n    the Free Software Foundation, either version 3 of the License, or      --\n    (at your option) any later version.                                    --\n                                                                           --\n    Eagle Lander is distributed in the hope that it will be useful,        --\n    but WITHOUT ANY WARRANTY; without even the implied warranty of         --\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          --\n    GNU General Public License for more details.                           --\n                                                                           --\n    You should have received a copy of the GNU General Public License      --\n    along with Eagle Lander.  If not, see <http://www.gnu.org/licenses/>.  --\n                                                                           --\n-----------------------------------------------------------------------------",
documentation_snippet: "",
record_types:    [
       {
       name: "Vector2D",
       qualified_name: "Geom.Vector2D",
       signature: "geom.vector2d",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "type Vector2D is record\n   X, Y : Gdouble;\nend record;",
       }   ,
   ]
,constants:    [
       {
       name: "Vector2D_Zero",
       qualified_name: "Geom.Vector2D_Zero",
       signature: "geom.vector2d_zero",
       enclosing: "",
       is_private: false,
       documentation: "",
       documentation_snippet: "Vector2D_Zero : constant Vector2D := (X => 0.0, Y => 0.0);",
       }   ,
   ]
,}
---
